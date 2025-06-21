# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from meterhub import Meterhub, AsyncMeterhub
from tests.utils import assert_matches_type
from meterhub.types.api.v1.meter import MeterReading

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRead:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Meterhub) -> None:
        read = client.api.v1.meter.read.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Meterhub) -> None:
        read = client.api.v1.meter.read.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
            unit="unit",
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Meterhub) -> None:
        response = client.api.v1.meter.read.with_raw_response.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = response.parse()
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Meterhub) -> None:
        with client.api.v1.meter.read.with_streaming_response.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = response.parse()
            assert_matches_type(MeterReading, read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_dataset(self, client: Meterhub) -> None:
        read = client.api.v1.meter.read.dataset(
            dataset_id=0,
            image="image",
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dataset(self, client: Meterhub) -> None:
        response = client.api.v1.meter.read.with_raw_response.dataset(
            dataset_id=0,
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = response.parse()
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dataset(self, client: Meterhub) -> None:
        with client.api.v1.meter.read.with_streaming_response.dataset(
            dataset_id=0,
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = response.parse()
            assert_matches_type(MeterReading, read, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRead:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeterhub) -> None:
        read = await async_client.api.v1.meter.read.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMeterhub) -> None:
        read = await async_client.api.v1.meter.read.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
            unit="unit",
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeterhub) -> None:
        response = await async_client.api.v1.meter.read.with_raw_response.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = await response.parse()
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeterhub) -> None:
        async with async_client.api.v1.meter.read.with_streaming_response.retrieve(
            image="image",
            points=[
                {
                    "x": 0,
                    "y": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = await response.parse()
            assert_matches_type(MeterReading, read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_dataset(self, async_client: AsyncMeterhub) -> None:
        read = await async_client.api.v1.meter.read.dataset(
            dataset_id=0,
            image="image",
        )
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dataset(self, async_client: AsyncMeterhub) -> None:
        response = await async_client.api.v1.meter.read.with_raw_response.dataset(
            dataset_id=0,
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = await response.parse()
        assert_matches_type(MeterReading, read, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dataset(self, async_client: AsyncMeterhub) -> None:
        async with async_client.api.v1.meter.read.with_streaming_response.dataset(
            dataset_id=0,
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = await response.parse()
            assert_matches_type(MeterReading, read, path=["response"])

        assert cast(Any, response.is_closed) is True
