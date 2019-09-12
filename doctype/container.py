"""Defines the doctype container type"""
from typing import Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Doc(Generic[T, S]):
    """Doc Type container provides a way to attach doc strings to parameters"""

    def __init__(self, kind: T, doc: str = "") -> None:
        self.kind = kind
        self.doc = doc

    def get(self) -> T:
        return self.kind
