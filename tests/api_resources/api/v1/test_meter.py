# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from meterhub import Meterhub, AsyncMeterhub
from tests.utils import assert_matches_type
from meterhub.types.api.v1 import MeterDetectResponse, MeterAnalyzeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_analyze(self, client: Meterhub) -> None:
        meter = client.api.v1.meter.analyze(
            image="image",
        )
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_analyze_with_all_params(self, client: Meterhub) -> None:
        meter = client.api.v1.meter.analyze(
            image="image",
            unit="unit",
        )
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_analyze(self, client: Meterhub) -> None:
        response = client.api.v1.meter.with_raw_response.analyze(
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_analyze(self, client: Meterhub) -> None:
        with client.api.v1.meter.with_streaming_response.analyze(
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_detect(self, client: Meterhub) -> None:
        meter = client.api.v1.meter.detect(
            image="image",
        )
        assert_matches_type(MeterDetectResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_detect(self, client: Meterhub) -> None:
        response = client.api.v1.meter.with_raw_response.detect(
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert_matches_type(MeterDetectResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_detect(self, client: Meterhub) -> None:
        with client.api.v1.meter.with_streaming_response.detect(
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert_matches_type(MeterDetectResponse, meter, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMeter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_analyze(self, async_client: AsyncMeterhub) -> None:
        meter = await async_client.api.v1.meter.analyze(
            image="image",
        )
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_analyze_with_all_params(self, async_client: AsyncMeterhub) -> None:
        meter = await async_client.api.v1.meter.analyze(
            image="image",
            unit="unit",
        )
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncMeterhub) -> None:
        response = await async_client.api.v1.meter.with_raw_response.analyze(
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncMeterhub) -> None:
        async with async_client.api.v1.meter.with_streaming_response.analyze(
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert_matches_type(MeterAnalyzeResponse, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_detect(self, async_client: AsyncMeterhub) -> None:
        meter = await async_client.api.v1.meter.detect(
            image="image",
        )
        assert_matches_type(MeterDetectResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_detect(self, async_client: AsyncMeterhub) -> None:
        response = await async_client.api.v1.meter.with_raw_response.detect(
            image="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert_matches_type(MeterDetectResponse, meter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_detect(self, async_client: AsyncMeterhub) -> None:
        async with async_client.api.v1.meter.with_streaming_response.detect(
            image="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert_matches_type(MeterDetectResponse, meter, path=["response"])

        assert cast(Any, response.is_closed) is True
