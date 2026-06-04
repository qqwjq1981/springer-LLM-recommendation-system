"""
API config loader shared by all chapter notebooks.

Replaces the path `./../../../Curify/curify_api.yaml` that the published
notebooks originally hard-coded (which only resolved on the author's local
machine). The loader now searches several reasonable locations and gives a
clear error if none are found, so a reader who clones the repo and follows
the README setup can run any notebook without touching paths.

Usage from inside a notebook:

    import sys
    sys.path.insert(0, "..")  # add tutorials/ to import path
    from _config import load_api_config

    data = load_api_config()
    openai_api_key = data["openai"]["api_key"]
"""
from __future__ import annotations

import os
import yaml
from pathlib import Path
from typing import Any


_SEARCH_RELATIVE = (
    Path("curify_api.yaml"),
    Path("config") / "curify_api.yaml",
)


def _candidates() -> list[Path]:
    out: list[Path] = []
    env = os.environ.get("CURIFY_API_YAML")
    if env:
        out.append(Path(env).expanduser())

    # Walk from cwd upwards looking for repo-root markers (presence of a
    # `tutorials/` dir). This lets the loader work no matter which chapter
    # the notebook is in.
    here = Path.cwd().resolve()
    for parent in (here, *here.parents):
        if (parent / "tutorials").is_dir():
            for rel in _SEARCH_RELATIVE:
                out.append(parent / rel)
            break
        for rel in _SEARCH_RELATIVE:
            out.append(parent / rel)

    # Legacy author-local path — kept last so existing local setups still work.
    out.append(Path("./../../../Curify/curify_api.yaml"))
    return out


def load_api_config() -> dict[str, Any]:
    """Locate and load curify_api.yaml. Raises FileNotFoundError with setup
    instructions if no copy is found."""
    tried: list[str] = []
    for c in _candidates():
        try:
            if c.is_file():
                with open(c, "r") as f:
                    return yaml.safe_load(f) or {}
        except OSError:
            pass
        tried.append(str(c))

    raise FileNotFoundError(
        "curify_api.yaml not found. To fix:\n"
        "  1. cp config/curify_api.example.yaml curify_api.yaml\n"
        "  2. Open curify_api.yaml and fill in your API keys.\n"
        "  3. Re-run the notebook.\n"
        "Or set the CURIFY_API_YAML environment variable to point at an "
        "existing copy.\n"
        f"Paths searched (in order):\n  - " + "\n  - ".join(tried)
    )
