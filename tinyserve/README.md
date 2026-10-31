# tinyserve

I will build a small, readable LLM inference engine myself, using [priyammaz/tinyserve](https://github.com/priyammaz/tinyserve) as the reference. The goal is to understand model execution, paged KV storage, prefix reuse, continuous batching and an OpenAI-compatible streaming API, then consider optimized kernels and parallel execution.

**Current state: boilerplate ready; engine implementation pending.** Setup provides a Python package, locked development environment, configuration, setup checks and TUI launchers. The engine and kernel files contain only starting-point docstrings. No upstream implementation has been copied, no model is downloaded, and no inference or GPU compatibility has been established.

This is an ordinary project folder owned by the Inference Labs collection, without its own nested Git repository. Reference reviewed on 2026-10-30 at commit [`32854e9`](https://github.com/priyammaz/tinyserve/tree/32854e9ac4c43f64b6577adcff155e8c593b0aad). The reference's CUDA/Triton path is a future hardware decision; the scaffold runs on CPU without those dependencies.

## Run independently

From this project folder in a standalone Inference Labs checkout. The workspace CLI and sibling repositories are optional.

```bash
uv sync --frozen
uv run --frozen tinyserve status
uv run --frozen python -m tinyserve check
uv run --frozen python src/show_config.py
uv run --frozen pytest -q
uv build
```

Python is pinned to 3.12.13. Runtime dependencies are intentionally empty; development uses the locked pytest version. Select and lock the model/runtime dependencies during implementation. The installed command and configuration also work from an unrelated working directory.

## Run from the workspace

```bash
./ai setup tinyserve
./ai run tinyserve --entrypoint status
./ai run tinyserve --entrypoint check
./ai run tinyserve --entrypoint config
./ai test tinyserve
./ai build tinyserve
./ai tui
```

In the TUI, open **Projects → Inference Labs → tinyserve**. Choose Project status, Check setup or Show configuration, then Run (`g`). Setup env, Checks and Build pkg use the same project and environment. Checks currently validate setup only.

Workspace actions use `.ai/envs/tinyserve/` and write build outputs to `.ai/builds/tinyserve/`. They do not start a server. From another directory use the absolute path to the workspace's `ai` launcher.

## Files and first implementation step

- `src/tinyserve/serve.py`: the learner's starting file for model execution, cache, scheduling and HTTP serving.
- `src/tinyserve/tinykernels.py`: a reserved place for later kernel work.
- `src/tinyserve/cli.py`: setup status/check/config commands.
- `src/tinyserve/project.toml`: reference, scope and unselected model/device.
- `src/{status,check_setup,show_config}.py`: direct TUI entry scripts.
- `tests/test_setup.py`: setup interface and failure checks; engine tests come with implementation.

Next, choose a small model and CPU/GPU runtime, define one-request input/output and KV-state contracts, then implement and independently check a plain single-request reference. Add cache, batching and HTTP streaming in later increments; optimize only after reference parity. Models, kernels, GPU execution, benchmarks and learner understanding remain pending.

Keep weights, datasets, runs, checkpoints and credentials ignored. Personal learning records go in ignored `docs/phases/` and `docs/implementation/`. The shared [Projects checkpoint](../../../docs/guide/resume.md) retains its existing learner gates.
