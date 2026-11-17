"""A tiny publish/subscribe event bus (observer pattern).

The engine announces what happens; the CLI, a logger or a future GUI decide what to do about it.
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

from .models import Finding, Host, ScanResult


@dataclass(frozen=True)
class ScanStarted:
    hosts: int
    ports: int


@dataclass(frozen=True)
class HostFound:
    host: Host


@dataclass(frozen=True)
class FindingRaised:
    finding: Finding


@dataclass(frozen=True)
class ScanFinished:
    result: ScanResult


Event = ScanStarted | HostFound | FindingRaised | ScanFinished
E = TypeVar("E", ScanStarted, HostFound, FindingRaised, ScanFinished)


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[type, list[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event_type: type[E], handler: Callable[[E], None]) -> None:
        self._handlers[event_type].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers[type(event)]:
            handler(event)
