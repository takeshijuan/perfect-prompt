"""Runnable checks for the routing-eval contract; no model calls."""

import contextlib
import io
import json
import shutil
import tempfile
from pathlib import Path

import validate_skill as validator


def check_routing_evals():
    original = validator.SKILL_DIR
    with tempfile.TemporaryDirectory() as directory:
        validator.SKILL_DIR = Path(directory) / "perfect-prompt"
        try:
            shutil.copytree(original, validator.SKILL_DIR)
            path = validator.SKILL_DIR / "evals" / "evals.json"
            data = json.loads(path.read_text())
            validator.validate_evals()
            for cases in [
                [],
                [{"prompt": "review PR#1", "should_trigger": "false"}],
                [{"prompt": "rewrite this prompt", "should_trigger": True}],
            ]:
                data["trigger_evals"] = cases
                path.write_text(json.dumps(data))
                with contextlib.redirect_stderr(io.StringIO()):
                    try:
                        validator.validate_evals()
                    except SystemExit as error:
                        assert error.code == 1
                    else:
                        raise AssertionError("invalid routing evals were accepted")
        finally:
            validator.SKILL_DIR = original
    print("ok: routing eval validation accepts valid cases and rejects invalid cases")


if __name__ == "__main__":
    check_routing_evals()
