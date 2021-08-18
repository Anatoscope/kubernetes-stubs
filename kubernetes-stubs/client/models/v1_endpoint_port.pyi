import datetime
import typing

import kubernetes.client

class V1EndpointPort:
    app_protocol: typing.Optional[str]
    name: typing.Optional[str]
    port: int
    protocol: typing.Optional[str]
    def __init__(
        self,
        *,
        app_protocol: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        port: int,
        protocol: typing.Optional[str] = ...
    ) -> None: ...
