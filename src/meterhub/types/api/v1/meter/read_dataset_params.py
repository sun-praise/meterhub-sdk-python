# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReadDatasetParams"]


class ReadDatasetParams(TypedDict, total=False):
    dataset_id: Required[int]

    image: Required[str]
