# scanner.py
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class ScanResult:
    source: str          # e.g. "system", "network", "file", "agent"
    payload: Any         # raw data (string, bytes, dict, etc.)
    metadata: Dict[str, Any]

class Scanner:
    """
    The Scanner is the sensory organ.
    It does NOT interpret, it only collects.
    """

    def __init__(self):
        self.sources = []

    def register_source(self, name: str, fn):
        """
        fn: () -> List[ScanResult]
        You can plug in any sensor here: logs, APIs, files, etc.
        """
        self.sources.append((name, fn))

    def scan(self) -> List[ScanResult]:
        results: List[ScanResult] = []
        for name, fn in self.sources:
            try:
                data = fn()
                results.extend(data)
            except Exception as e:
                results.append(
                    ScanResult(
                        source=name,
                        payload=str(e),
                        metadata={"error": True}
                    )
                )
        return results
