# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .read import (
    ReadResource,
    AsyncReadResource,
    ReadResourceWithRawResponse,
    AsyncReadResourceWithRawResponse,
    ReadResourceWithStreamingResponse,
    AsyncReadResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import meter_detect_params, meter_analyze_params
from .....types.api.v1.meter_detect_response import MeterDetectResponse
from .....types.api.v1.meter_analyze_response import MeterAnalyzeResponse

__all__ = ["MeterResource", "AsyncMeterResource"]


class MeterResource(SyncAPIResource):
    @cached_property
    def read(self) -> ReadResource:
        return ReadResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Svtter/meterhub-sdk#accessing-raw-response-data-eg-headers
        """
        return MeterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Svtter/meterhub-sdk#with_streaming_response
        """
        return MeterResourceWithStreamingResponse(self)

    def analyze(
        self,
        *,
        image: str,
        unit: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterAnalyzeResponse:
        """
        分析仪表图片，返回仪表的读数和类型

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/meter/analyze/",
            body=maybe_transform(
                {
                    "image": image,
                    "unit": unit,
                },
                meter_analyze_params.MeterAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterAnalyzeResponse,
        )

    def detect(
        self,
        *,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterDetectResponse:
        """
        Detect Meter

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/meter/detect/",
            body=maybe_transform({"image": image}, meter_detect_params.MeterDetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterDetectResponse,
        )


class AsyncMeterResource(AsyncAPIResource):
    @cached_property
    def read(self) -> AsyncReadResource:
        return AsyncReadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Svtter/meterhub-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMeterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Svtter/meterhub-sdk#with_streaming_response
        """
        return AsyncMeterResourceWithStreamingResponse(self)

    async def analyze(
        self,
        *,
        image: str,
        unit: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterAnalyzeResponse:
        """
        分析仪表图片，返回仪表的读数和类型

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/meter/analyze/",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "unit": unit,
                },
                meter_analyze_params.MeterAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterAnalyzeResponse,
        )

    async def detect(
        self,
        *,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterDetectResponse:
        """
        Detect Meter

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/meter/detect/",
            body=await async_maybe_transform({"image": image}, meter_detect_params.MeterDetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterDetectResponse,
        )


class MeterResourceWithRawResponse:
    def __init__(self, meter: MeterResource) -> None:
        self._meter = meter

        self.analyze = to_raw_response_wrapper(
            meter.analyze,
        )
        self.detect = to_raw_response_wrapper(
            meter.detect,
        )

    @cached_property
    def read(self) -> ReadResourceWithRawResponse:
        return ReadResourceWithRawResponse(self._meter.read)


class AsyncMeterResourceWithRawResponse:
    def __init__(self, meter: AsyncMeterResource) -> None:
        self._meter = meter

        self.analyze = async_to_raw_response_wrapper(
            meter.analyze,
        )
        self.detect = async_to_raw_response_wrapper(
            meter.detect,
        )

    @cached_property
    def read(self) -> AsyncReadResourceWithRawResponse:
        return AsyncReadResourceWithRawResponse(self._meter.read)


class MeterResourceWithStreamingResponse:
    def __init__(self, meter: MeterResource) -> None:
        self._meter = meter

        self.analyze = to_streamed_response_wrapper(
            meter.analyze,
        )
        self.detect = to_streamed_response_wrapper(
            meter.detect,
        )

    @cached_property
    def read(self) -> ReadResourceWithStreamingResponse:
        return ReadResourceWithStreamingResponse(self._meter.read)


class AsyncMeterResourceWithStreamingResponse:
    def __init__(self, meter: AsyncMeterResource) -> None:
        self._meter = meter

        self.analyze = async_to_streamed_response_wrapper(
            meter.analyze,
        )
        self.detect = async_to_streamed_response_wrapper(
            meter.detect,
        )

    @cached_property
    def read(self) -> AsyncReadResourceWithStreamingResponse:
        return AsyncReadResourceWithStreamingResponse(self._meter.read)
