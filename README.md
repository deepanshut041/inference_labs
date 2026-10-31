# Inference Labs

Build inference systems from first principles, beginning with [tinyserve](tinyserve/README.md). Each project is an ordinary folder in this independent collection repository, registered at `ai_projects/projects/inference_labs/`. The local bare origin is workspace `.ai/repositories/inference_labs.git`.

Commit collection changes here, push them to the local origin, then update the collection pointer in `ai_projects`. Shared tutorials and learning checkpoints live in the Projects Docs repository.

TinyServe currently has verified Python boilerplate and workspace/TUI launchers. The learner will write its model execution, cache, scheduler, kernels and serving behavior. No inference implementation or performance result is delivered by setup.

## Run from a standalone checkout

Only Git, uv and the project's Python dependencies are needed. After cloning this collection, run:

```bash
cd tinyserve
uv sync --frozen
uv run --frozen python src/check_setup.py
uv run --frozen python -m tinyserve status
uv run --frozen pytest -q
uv build
```

The collection does not require `ai_projects`, shared Docs or the workspace CLI to run. Each future project must provide the same native setup/run/test/build route in its own README.

Inside the full AI workspace, the optional CLI/TUI invokes the same source: `./ai run tinyserve --entrypoint check`, or Projects → Inference Labs → tinyserve. Run that command from workspace home. See [TinyServe's README](tinyserve/README.md) for both routes and the pending engine implementation.
