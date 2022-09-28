# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.credentials import AzureKeyCredential
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AnomalyDetectorClientConfiguration
from ._operations import AnomalyDetectorClientOperationsMixin
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AnomalyDetectorClient(AnomalyDetectorClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """The Anomaly Detector API detects anomalies automatically in time series data. It supports two
    kinds of mode, one is for stateless using, another is for stateful using. In stateless mode,
    there are three functionalities. Entire Detect is for detecting the whole series with model
    trained by the time series, Last Detect is detecting last point with model trained by points
    before. ChangePoint Detect is for detecting trend changes in time series. In stateful mode,
    user can store time series, the stored time series will be used for detection anomalies. Under
    this mode, user can still use the above three functionalities by only giving a time range
    without preparing time series in client side. Besides the above three functionalities, stateful
    model also provide group based detection and labeling service. By leveraging labeling service
    user can provide labels for each detection result, these labels will be used for retuning or
    regenerating detection models. Inconsistency detection is a kind of group based detection, this
    detection will find inconsistency ones in a set of time series. By using anomaly detector
    service, business customers can discover incidents and establish a logic flow for root cause
    analysis.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://westus2.api.cognitive.microsoft.com). Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param api_version: Anomaly Detector API version (for example, v1.1). "v1.1" Default value is
     "v1.1".
    :type api_version: str
    :keyword endpoint: Service URL. Required. Default value is "".
    :paramtype endpoint: str
    """

    def __init__(
        self,
        endpoint: str,
        credential: AzureKeyCredential,
        api_version: str = "v1.1",
        *,
        endpoint: str = "",
        **kwargs: Any
    ) -> None:
        self._config = AnomalyDetectorClientConfiguration(
            endpoint=endpoint, credential=credential, api_version=api_version, **kwargs
        )
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "ApiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AnomalyDetectorClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
