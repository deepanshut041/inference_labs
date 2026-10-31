"""Environment and project information; the inference engine is learner-owned."""
from __future__ import annotations

import argparse
from importlib.metadata import version
from importlib.resources import files
import json
import sys
import tomllib


def configuration() -> dict:
    return tomllib.loads(files("tinyserve").joinpath("project.toml").read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="TinyServe boilerplate; inference implementation pending.")
    parser.add_argument("command", nargs="?", choices=("status", "check", "config"), default="status")
    args = parser.parse_args(argv)
    config = configuration()
    if args.command == "config":
        result = config
    elif args.command == "check":
        checks = {
            "python_3_12": sys.version_info[:2] == (3, 12),
            "installed_package": version("tinyserve") == "0.1.0",
            "packaged_configuration": config["project"]["name"] == "tinyserve",
        }
        result = {"project": "tinyserve", "scope": "setup only", "checks": checks,
                  "ok": all(checks.values()), "python": sys.version.split()[0]}
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    else:
        result = {"project": "tinyserve", "state": config["project"]["state"],
                  "implementation_owner": config["project"]["implementation_owner"],
                  "reference": config["project"]["reference_url"],
                  "pending": config["project"]["planned_features"],
                  "next_action": "Choose a small model and execution device, then define the one-request contract."}
    print(json.dumps(result, indent=2))
    return 0
