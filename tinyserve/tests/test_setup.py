"""Setup interfaces only; model and serving tests belong to later implementation."""
import json
from pathlib import Path
import subprocess
import sys

import pytest

from tinyserve.cli import main


@pytest.mark.parametrize("command", ["status", "config", "check"])
def test_module_runs_from_an_unrelated_directory(command, tmp_path):
    result = subprocess.run([sys.executable, "-m", "tinyserve", command], cwd=tmp_path,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    output = json.loads(result.stdout)
    if command == "check":
        assert output["ok"] and all(output["checks"].values())
    elif command == "config":
        assert output["runtime"]["device"] == "unselected"
        assert output["runtime"]["model_id"] == ""
    else:
        assert output["state"] == "boilerplate"
        assert output["implementation_owner"] == "learner"


@pytest.mark.parametrize("arguments", [["serve"], ["generate"], ["status", "--model", "anything"]])
def test_unimplemented_or_unknown_commands_fail(arguments):
    with pytest.raises(SystemExit) as error:
        main(arguments)
    assert error.value.code == 2


def test_setup_checks_fail_on_an_unsupported_python(monkeypatch, capsys):
    monkeypatch.setattr(sys, "version_info", (3, 11, 0))
    assert main(["check"]) == 1
    assert json.loads(capsys.readouterr().out)["checks"]["python_3_12"] is False


@pytest.mark.parametrize("script", ["status.py", "check_setup.py", "show_config.py"])
def test_direct_tui_scripts(script, tmp_path):
    source = Path(__file__).resolve().parents[1] / "src" / script
    result = subprocess.run([sys.executable, str(source)], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert isinstance(json.loads(result.stdout), dict)
