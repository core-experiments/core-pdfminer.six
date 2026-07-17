from __future__ import annotations

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SAMPLES = REPOSITORY_ROOT / "samples"


def sample_path(relative_path: str) -> Path:
    path = SAMPLES / relative_path
    if not path.is_file():
        raise FileNotFoundError(f"Benchmark fixture is unavailable: {path}")
    return path
