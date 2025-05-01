# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

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
from .....types.api.v1.meter import read_dataset_params, read_retrieve_params
from .....types.api.v1.meter.meter_reading import MeterReading

__all__ = ["ReadResource", "AsyncReadResource"]


class ReadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/meterhub-python#accessing-raw-response-data-eg-headers
        """
        return ReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/meterhub-python#with_streaming_response
        """
        return ReadResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        image: str,
        points: Iterable[read_retrieve_params.Point],
        unit: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterReading:
        """
        Read Meter

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
            "/api/v1/meter/read/",
            body=maybe_transform(
                {
                    "image": image,
                    "points": points,
                    "unit": unit,
                },
                read_retrieve_params.ReadRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterReading,
        )

    def dataset(
        self,
        *,
        dataset_id: int,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterReading:
        """
        使用某个数据集配置，来获得仪表图片的读数。可以获得更高的性能

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
            "/api/v1/meter/read/dataset",
            body=maybe_transform({"image": image}, read_dataset_params.ReadDatasetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_id": dataset_id}, read_dataset_params.ReadDatasetParams),
            ),
            cast_to=MeterReading,
        )


class AsyncReadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/meterhub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/meterhub-python#with_streaming_response
        """
        return AsyncReadResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        image: str,
        points: Iterable[read_retrieve_params.Point],
        unit: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterReading:
        """
        Read Meter

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
            "/api/v1/meter/read/",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "points": points,
                    "unit": unit,
                },
                read_retrieve_params.ReadRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeterReading,
        )

    async def dataset(
        self,
        *,
        dataset_id: int,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeterReading:
        """
        使用某个数据集配置，来获得仪表图片的读数。可以获得更高的性能

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
            "/api/v1/meter/read/dataset",
            body=await async_maybe_transform({"image": image}, read_dataset_params.ReadDatasetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset_id": dataset_id}, read_dataset_params.ReadDatasetParams),
            ),
            cast_to=MeterReading,
        )


class ReadResourceWithRawResponse:
    def __init__(self, read: ReadResource) -> None:
        self._read = read

        self.retrieve = to_raw_response_wrapper(
            read.retrieve,
        )
        self.dataset = to_raw_response_wrapper(
            read.dataset,
        )


class AsyncReadResourceWithRawResponse:
    def __init__(self, read: AsyncReadResource) -> None:
        self._read = read

        self.retrieve = async_to_raw_response_wrapper(
            read.retrieve,
        )
        self.dataset = async_to_raw_response_wrapper(
            read.dataset,
        )


class ReadResourceWithStreamingResponse:
    def __init__(self, read: ReadResource) -> None:
        self._read = read

        self.retrieve = to_streamed_response_wrapper(
            read.retrieve,
        )
        self.dataset = to_streamed_response_wrapper(
            read.dataset,
        )


class AsyncReadResourceWithStreamingResponse:
    def __init__(self, read: AsyncReadResource) -> None:
        self._read = read

        self.retrieve = async_to_streamed_response_wrapper(
            read.retrieve,
        )
        self.dataset = async_to_streamed_response_wrapper(
            read.dataset,
        )
