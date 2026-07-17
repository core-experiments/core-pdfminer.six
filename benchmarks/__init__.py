"""ASV benchmark suite for core-pdfminer.six."""

import importlib
import sys

try:
    importlib.import_module("core_pdfminer_six")
except ModuleNotFoundError as exc:
    if exc.name != "core_pdfminer_six":
        raise
    # The pinned upstream baseline predates our namespace rename. Alias it only
    # inside ASV so the same benchmark suite can measure both distributions.
    sys.modules["core_pdfminer_six"] = importlib.import_module("pdfminer")
