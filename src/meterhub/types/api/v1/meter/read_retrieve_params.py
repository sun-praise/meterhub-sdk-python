# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReadRetrieveParams", "Point"]


class ReadRetrieveParams(TypedDict, total=False):
    image: Required[str]

    points: Required[Iterable[Point]]

    unit: Optional[str]


class Point(TypedDict, total=False):
    x: Required[float]

    y: Required[float]
