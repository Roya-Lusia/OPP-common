# coding: utf-8

# flake8: noqa

"""
    Open Park Project - OpenAPI 3.1

    The Open Park Project (OPP) is a free open-source project that aims to  provide a scalable and flexible platform for the management of parking areas.  Some useful links: - [Open Park Project](https://github.com/OpenParkProject) - [API definition](https://github.com/OpenParkProject/OPP-common/openapi.yaml)

    The version of the OpenAPI document: 0.1
    Contact: tollsimy.dev@protonmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.test_api import TestApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.test import Test
