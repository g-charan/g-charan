# Charan Gutti

I write the library instead of importing it, then benchmark the result against
the library. Nine times so far: a time-series database, an LSM tree, an API
gateway, a Nasdaq order book, a vector index, an RTMP server, a compiler to
WebAssembly, a RAG service and an LLM inference engine. Go, Java, C++, Python
and TypeScript, standard library first. Every number in one of my READMEs comes
from a test or benchmark in that repository, and when the number is bad the
README says so.

B.Tech in Computer Science, ICFAI Tech Hyderabad, 2026. Looking for backend,
systems, platform or AI engineering work, in Hyderabad or remote.

[cgportfolio.vercel.app](https://cgportfolio.vercel.app) ·
[charan.gutti@gmail.com](mailto:charan.gutti@gmail.com) ·
[linkedin.com/in/Charan-Gutti](https://linkedin.com/in/Charan-Gutti)

## Right now

Six of the projects run on one small EC2 instance and report on themselves.
These lines are rewritten every six hours by [`build_readme.py`](build_readme.py),
which reads each demo's own `/metrics` or `/stats`.

<!-- live starts -->
_Fetched 2026-09-04 20:49 UTC._

- **go-tsdb** did not answer (URLError).
- **jlsm** did not answer (URLError).
- **jgate** did not answer (URLError).
- **rtmp-server** did not answer (URLError).
- **ragmeter** did not answer (URLError).
- **paged-llama** did not answer (URLError).
<!-- live ends -->

If one says it did not answer, the box is having a bad day; the code is still
here.

## The projects

Every number below came from a benchmark or test in the repository, on an
Apple M4 Max. Re-run them; they will differ on your hardware.

| Project | What it is | The number worth quoting | Live |
|---|---|---|---|
| [go-tsdb](https://github.com/g-charan/go-tsdb) | Time-series database in Go: Gorilla compression, WAL, Prometheus-compatible endpoint | 14.4 M samples/sec ingest, 4.2x compression on real telemetry | [Grafana](https://tsdb.35-154-87-88.sslip.io) |
| [jlsm](https://github.com/g-charan/jlsm) | LSM-tree key-value engine in Java, speaking the Redis wire protocol | 77.8 k SET/sec and 137 k GET/sec, cross-checked with `redis-benchmark` | [dashboard](https://jlsm.35-154-87-88.sslip.io) |
| [jgate](https://github.com/g-charan/jgate) | Netty API gateway: JWT on the event loop, token bucket in Redis Lua, three replicas on Kubernetes | 36 k req/sec, +0.08 ms p50 over the backend; a 60-request burst across 3 replicas gets one bucket through, not three | [rate limits](https://gateway.35-154-87-88.sslip.io) |
| [orderbook-cpp](https://github.com/g-charan/orderbook-cpp) | ITCH 5.0 parser and limit order book in C++23 | 18.9 M messages/sec, p99 166 ns, 800x better worst case than `std::map` | |
| [hnsw-cpp](https://github.com/g-charan/hnsw-cpp) | HNSW vector index in C++23 with NEON kernels | 1.68x hnswlib's throughput at 0.99 recall on SIFT1M | [demo](https://g-charan.github.io/hnsw-cpp/) |
| [rtmp-server](https://github.com/g-charan/rtmp-server) | RTMP ingest to HLS in Go: handshake, chunk stream and MPEG-TS muxer | 1,000 concurrent publishers, 0 dropped, 2.46 s to first playable segment | [player](https://live.35-154-87-88.sslip.io) |
| [wasm-forge](https://github.com/g-charan/wasm-forge) | A language that compiles to real WebAssembly, in TypeScript | 1,988 lines/ms end to end; output verified against the browser's own runtime | [playground](https://g-charan.github.io/wasm-forge/) |
| [ragmeter](https://github.com/g-charan/ragmeter) | RAG question answering over HotpotQA with a LangGraph agent and an eval harness, on hnsw-cpp | 0.81 recall@10; retrieval lifts exact match from 10.0% to 24.3%; CI fails if recall drops | [ask it](https://rag.35-154-87-88.sslip.io) |
| [paged-llama](https://github.com/g-charan/paged-llama) | Llama + PagedAttention reimplemented in C++23, served over an OpenAI-compatible API | Logits match Hugging Face to 4e-4; 406 tok/s aggregate at 32 streams, 3.2x behind llama.cpp and says why | [API](https://llm.35-154-87-88.sslip.io/v1/models) |

The stack that serves them is [portfolio-deploy](https://github.com/g-charan/portfolio-deploy) — the host in Terraform,
then Caddy, `docker compose`, and two sidecars that generate traffic so the demos
have something to show.

## What they taught me

- **A benchmark you cannot lose is marketing.** paged-llama ships the llama.cpp
  comparison it loses by 3.2x and explains why. hnsw-cpp says its lead over
  hnswlib disappears with SIMD turned off.
- **The differential test is the test.** orderbook-cpp replays a million
  messages through its book and a `std::map` book and compares after every one.
  paged-llama holds its logits to the `transformers` reference. wasm-forge makes
  the interpreter, the `.wasm` binary and the browser agree.
- **Let a tool that knows nothing about your code check your code.** jlsm's
  numbers come from `redis-benchmark`, rtmp-server's from `ffprobe`, go-tsdb's
  from a stock Prometheus scraping it, and the Terraform for the demo host was
  imported from the running box until `plan` said "No changes".
- **The paper's number is for the paper's data.** go-tsdb gets 4.2x
  compression, not Gorilla's 10x, and working out why was the interesting part.
- **For anything with a model in it, the eval harness is the product.**
  ragmeter's README lists its numbers and then says which ones to distrust.

## Stack

- **Languages:** C++, Java, Go, TypeScript, Python, SQL
- **Systems:** TCP sockets, concurrency, lock-free data structures, mmap, write-ahead logs, SIMD (NEON), event loops, RTMP / MPEG-TS
- **Machine learning:** RAG, LangGraph / LangChain, LLM inference and serving, Hugging Face Transformers, PyTorch, INT8 quantization, KV cache / PagedAttention, vector search (HNSW, pgvector), LLM-as-judge evaluation
- **Backend:** Netty, Redis, PostgreSQL, Node.js, FastAPI, REST APIs, JWT authentication
- **Frontend:** React, Next.js, React Native, Flutter, Tailwind CSS
- **Infrastructure:** Docker, Docker Compose, Kubernetes, Terraform, GitHub Actions, Prometheus, Grafana, AWS EC2, Linux, Git


