"""The vulnerability knowledge base: which product versions have which known vulnerabilities.

The bundled file is a small teaching sample (ADR-0002). A production tool would load a full feed,
such as NVD or OSV, through the same interface.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from importlib import resources
from pathlib import Path


def version_key(version: str) -> tuple[int, ...]:
    """Turn a version string into a comparable tuple.

    '2.4.49' -> (2, 4, 49); OpenSSH '8.9p1' -> (8, 9, 1); ProFTPD '1.3.5a' -> (1, 3, 5, 1).
    Good enough for the products we fingerprint, not a general solution.
    """
    v = re.sub(r"p(?=\d)", ".", version.lower())            # OpenSSH portable release: 8.9p1
    v = re.sub(r"(?<=\d)([a-z])$", lambda m: f".{ord(m.group(1)) - 96}", v)  # letter suffix: 1.3.5a
    return tuple(int(n) for n in re.findall(r"\d+", v))


@dataclass(frozen=True)
class Vulnerability:
    id: str
    product: str
    introduced: str          # first affected version
    fixed: str               # first version that is not affected
    cvss: float
    title: str
    remediation: str

    def affects(self, product: str | None, version: str | None) -> bool:
        if product != self.product or not version:
            return False
        v = version_key(version)
        return version_key(self.introduced) <= v < version_key(self.fixed)


class KnowledgeBase:
    def __init__(self, vulnerabilities: list[Vulnerability]):
        self.vulnerabilities = vulnerabilities

    @classmethod
    def load(cls, path: str | Path | None = None) -> KnowledgeBase:
        if path is None:
            text = resources.files("netwarden.data").joinpath("vulns.json").read_text(encoding="utf-8")
        else:
            text = Path(path).read_text(encoding="utf-8")
        return cls([Vulnerability(**v) for v in json.loads(text)])

    def lookup(self, product: str | None, version: str | None) -> list[Vulnerability]:
        return [v for v in self.vulnerabilities if v.affects(product, version)]
