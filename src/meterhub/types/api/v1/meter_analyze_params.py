# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MeterAnalyzeParams"]


class MeterAnalyzeParams(TypedDict, total=False):
    image: Required[str]

    unit: Optional[str]
