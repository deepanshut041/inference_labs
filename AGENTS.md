# Inference Labs ownership

This independent collection repository owns the ordinary project folders under `ai_projects/projects/inference_labs`. Follow the workspace and Projects instructions. Do not create a nested repository for tinyserve. Commit collection changes here, push to the local bare origin `.ai/repositories/inference_labs.git`, then update the gitlink in ai_projects.

TinyServe is a learner-built project inspired by https://github.com/priyammaz/tinyserve. The current request authorizes boilerplate, environment, checks and TUI integration only. The learner explicitly wants to implement the inference engine themselves. Do not copy the upstream engine, fill in serving/cache/scheduler/kernel logic, download models or launch GPU jobs as part of setup.

Keep dependencies minimal until the runtime/hardware is selected. Record setup verification separately from model correctness, performance, learner review and hosted/GPU execution. Keep environments, weights, runs, credentials and personal study records ignored. Use the shared workspace launcher and argument arrays; preserve other projects and learning checkpoints.
