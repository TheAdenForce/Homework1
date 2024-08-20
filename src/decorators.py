import logging
from typing import Any, Callable, Optional

logging.basicConfig(level=logging.INFO)


def log(filename: Optional[str] = None) -> Callable[..., Any]: