"""Check the environment and installed setup package."""
from tinyserve.cli import main

if __name__ == "__main__":
    raise SystemExit(main(["check"]))
