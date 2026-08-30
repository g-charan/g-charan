"""Rewrite the "Right now" block of README.md from the demos' own endpoints.

Every demo already exposes what it is doing (Prometheus text, a JSON stats
route, an HLS playlist). This reads those and writes a few plain sentences
between the markers. A demo that does not answer is reported as such rather
than failing the run; the free-tier box is allowed a bad day.
"""
import json
import re
import urllib.request
from datetime import datetime, timezone

HOST = "35-154-87-88.sslip.io"
START, END = "<!-- live starts -->", "<!-- live ends -->"


def get(url, timeout=20):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read().decode()


def prom(text):
    """Prometheus text format -> {'name{labels}': value}."""
    out = {}
    for line in text.splitlines():
        if line and not line.startswith("#"):
            key, val = line.split()[:2]
            out[key] = float(val)
    return out


def hours(seconds):
    d, h = divmod(int(seconds) // 3600, 24)
    return f"{d} d {h} h" if d else f"{h} h"


def n(x):
    x = int(x)
    return f"{x/1e6:.1f} M" if x >= 1e6 else f"{x:,}"


def plural(count, word):
    return f"{int(count):,} {word}{'' if int(count) == 1 else 's'}"


def tsdb():
    m = prom(get(f"https://tsdb.{HOST}/metrics"))
    return (f"**go-tsdb** holds {n(m['tsdb_samples'])} samples across {int(m['tsdb_series'])} series, "
            f"up {hours(m['tsdb_uptime_seconds'])}; Prometheus is scraping it and the box it "
            f"runs on is at load {m['node_load1']:.2f}.")


def jlsm():
    s = json.loads(get(f"https://jlsm.{HOST}/stats"))
    return (f"**jlsm** has taken {n(s['writes'])} writes and {n(s['reads'])} reads from a "
            f"`redis-benchmark` sidecar in {hours(s['uptime_seconds'])}, through {s['flushes']:,} "
            f"flushes and {s['compactions']:,} compactions; the Bloom filters turned away "
            f"{n(s['bloom_rejects'])} disk lookups.")


def jgate():
    req = urllib.request.Request(f"https://gateway.{HOST}/admin/stats")
    with urllib.request.urlopen(req, timeout=20) as r:
        line = r.readline().decode()  # first server-sent event
    s = json.loads(line.removeprefix("data:"))
    return (f"**jgate** has seen {s['requests']:,} requests: {s['proxied']:,} proxied, "
            f"{s['rateLimited']:,} rate-limited by the Lua token bucket, {s['unauthorized']:,} "
            f"rejected for a bad JWT.")


def rtmp():
    pl = get(f"https://live.{HOST}/hls/test.m3u8")
    segs = pl.count("#EXTINF")
    seq = re.search(r"#EXT-X-MEDIA-SEQUENCE:(\d+)", pl)
    return (f"**rtmp-server** is muxing an ffmpeg test stream into MPEG-TS: {segs} segments in "
            f"the playlist, sequence number {int(seq.group(1)):,}.")


def ragmeter():
    h = json.loads(get(f"https://rag.{HOST}/health"))
    m = prom(get(f"https://rag.{HOST}/metrics"))
    asked = sum(v for k, v in m.items() if k.startswith("ragmeter_requests_total"))
    return (f"**ragmeter** has {h['chunks']:,} chunks in its hnsw-cpp index and has answered "
            f"{plural(asked, 'question')} from visitors, generating through paged-llama "
            f"(`{h['model']}`).")


def paged_llama():
    m = prom(get(f"https://llm.{HOST}/metrics"))
    done = sum(v for k, v in m.items() if k.startswith("pl_requests_total"))
    return (f"**paged-llama** has finished {plural(done, 'completion')} and generated "
            f"{n(m['pl_generated_tokens_total'])} tokens; {int(m['pl_kv_blocks_used'])} of "
            f"{int(m['pl_kv_blocks_total'])} KV blocks are in use and the prefix cache holds "
            f"{int(m['pl_prefix_cache_entries'])} blocks.")


def main():
    lines = []
    for name, fn in [("go-tsdb", tsdb), ("jlsm", jlsm), ("jgate", jgate),
                     ("rtmp-server", rtmp), ("ragmeter", ragmeter), ("paged-llama", paged_llama)]:
        try:
            lines.append("- " + fn())
        except Exception as e:  # noqa: BLE001 - any failure is a fact worth printing
            lines.append(f"- **{name}** did not answer ({type(e).__name__}).")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = f"{START}\n_Fetched {stamp}._\n\n" + "\n".join(lines) + f"\n{END}"
    readme = open("README.md").read()
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, readme, flags=re.S)
    if new != readme:
        open("README.md", "w").write(new)
    print(block)


if __name__ == "__main__":
    main()
