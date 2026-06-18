# parser.py
from dataclasses import dataclass
from typing import Any, Dict, Optional
from scanner import ScanResult

@dataclass
class ParsedItem:
    kind: str            # e.g. "event", "alert", "metric", "message"
    data: Dict[str, Any] # normalized structure
    confidence: float    # 0.0–1.0
    raw: ScanResult

class Parser:
    """
    The Parser converts raw ScanResult into structured ParsedItem.
    One parser can handle multiple formats via small handlers.
    """

    def __init__(self):
        self.handlers = []  # list of (name, fn)

    def register_handler(self, name: str, fn):
        """
        fn: (ScanResult) -> Optional[ParsedItem]
        If fn can't handle it, return None.
        """
        self.handlers.append((name, fn))

    def parse(self, scan_result: ScanResult) -> Optional[ParsedItem]:
        for name, fn in self.handlers:
            item = fn(scan_result)
            if item is not None:
                return item
        # fallback: unknown structure
        return ParsedItem(
            kind="unknown",
            data={"payload": scan_result.payload},
            confidence=0.1,
            raw=scan_result
        )
