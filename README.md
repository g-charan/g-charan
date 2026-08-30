# Charan Gutti

Software engineer in Hyderabad, B.Tech in Computer Science (ICFAI Tech, 2026).
Open to backend, systems, platform and AI engineering roles, on-site in
Hyderabad or remote.

I learn things by building them without the library that usually does the
work: storage engines, protocol servers, an order book, a compiler, a vector
index, a RAG service and an LLM inference engine, each written on the standard
library, benchmarked against the established implementation, and most of them
running live.

[cgportfolio.vercel.app](https://cgportfolio.vercel.app) ·
[charan.gutti@gmail.com](mailto:charan.gutti@gmail.com) ·
[linkedin.com/in/Charan-Gutti](https://linkedin.com/in/Charan-Gutti)

## Projects

Every number came from a benchmark or test in the repository, on an Apple M4
Max. Re-run them; they will differ on your hardware.

| Project | What it is | The number worth quoting | Live |
|---|---|---|---|
| [go-tsdb](https://github.com/g-charan/go-tsdb) | Time-series database in Go: Gorilla compression, WAL, Prometheus-compatible endpoint | 14.4 M samples/sec ingest, 4.2x compression on real telemetry | [Grafana](https://tsdb.35-154-87-88.sslip.io) |
| [jlsm](https://github.com/g-charan/jlsm) | LSM-tree key-value engine in Java, speaking the Redis wire protocol | 77.8 k SET/sec and 137 k GET/sec, cross-checked with `redis-benchmark` | [dashboard](https://jlsm.35-154-87-88.sslip.io) |
| [jgate](https://github.com/g-charan/jgate) | Netty API gateway: JWT on the event loop, token bucket in Redis Lua | 36 k req/sec, +0.08 ms p50 over talking to the backend directly | [rate limits](https://gateway.35-154-87-88.sslip.io) |
| [orderbook-cpp](https://github.com/g-charan/orderbook-cpp) | ITCH 5.0 parser and limit order book in C++23 | 18.9 M messages/sec, p99 166 ns, 800x better worst case than `std::map` | |
| [hnsw-cpp](https://github.com/g-charan/hnsw-cpp) | HNSW vector index in C++23 with NEON kernels | 1.68x hnswlib's throughput at 0.99 recall on SIFT1M | [demo](https://g-charan.github.io/hnsw-cpp/) |
| [rtmp-server](https://github.com/g-charan/rtmp-server) | RTMP ingest to HLS in Go: handshake, chunk stream and MPEG-TS muxer | 1,000 concurrent publishers, 0 dropped, 2.46 s to first playable segment | [player](https://live.35-154-87-88.sslip.io) |
| [wasm-forge](https://github.com/g-charan/wasm-forge) | A language that compiles to real WebAssembly, in TypeScript | 1,988 lines/ms end to end; output verified against the browser's own runtime | [playground](https://g-charan.github.io/wasm-forge/) |
| [ragmeter](https://github.com/g-charan/ragmeter) | RAG question answering over HotpotQA with a LangGraph agent and an eval harness, on hnsw-cpp | 0.81 recall@10; retrieval lifts exact match from 10.0% to 24.3%; CI fails if recall drops | [ask it](https://rag.35-154-87-88.sslip.io) |
| [paged-llama](https://github.com/g-charan/paged-llama) | Llama + PagedAttention reimplemented in C++23, served over an OpenAI-compatible API | Logits match Hugging Face to 4e-4; 406 tok/s aggregate at 32 streams, 3.2x behind llama.cpp and says why | [API](https://llm.35-154-87-88.sslip.io/v1/models) |

The demos run on one EC2 instance behind Caddy; the stack that serves them is
[portfolio-deploy](https://github.com/g-charan/portfolio-deploy).

## Stack

- **Languages:** C++, Java, Go, TypeScript, Python, SQL
- **Systems:** TCP sockets, concurrency, lock-free data structures, mmap, write-ahead logs, SIMD (NEON), event loops, RTMP / MPEG-TS
- **Machine learning:** RAG, LangGraph / LangChain, LLM inference and serving, Hugging Face Transformers, PyTorch, INT8 quantization, KV cache / PagedAttention, vector search (HNSW, pgvector), LLM-as-judge evaluation
- **Backend:** Netty, Redis, PostgreSQL, Node.js, FastAPI, REST APIs, JWT authentication
- **Frontend:** React, Next.js, React Native, Flutter, Tailwind CSS
- **Infrastructure:** Docker, Docker Compose, GitHub Actions, Prometheus, Grafana, AWS EC2, Linux, Git

## Experience

- **EFILOS Technologies** — Frontend Engineer (part-time), Jun 2025 – Aug 2026
- **Pi Exploration Inc** — Software Developer Intern (remote), Jan 2026 – Jun 2026
- **Gigsearch** — Full Stack Developer Intern, Jun 2024 – Aug 2024

Four pull requests merged into [Orn](https://github.com/pabloosabaterr/Orn),
an open-source compiler in C: source-location tracking through the lexer and
parser, negative-float parsing, comment support. State-level finalist, Smart
India Hackathon 2024.

Earlier work: [CodeScribe](https://github.com/g-charan/CodeScribe) (commit
messages from a diff), [Cryptic](https://github.com/g-charan/Cryptic) (peer-to-peer
chat over WebRTC), and the rest of the repositories here.
