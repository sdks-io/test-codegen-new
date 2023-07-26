# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from lispublicservices.api_helper import APIHelper
from lispublicservices.configuration import Server
from lispublicservices.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from lispublicservices.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from lispublicservices.models.lis_response_lis_public_unit import LISResponseLISPublicUnit


class UnitController(BaseController):

    """A Controller to access Endpoints in the lispublicservices API."""
    def __init__(self, config):
        super(UnitController, self).__init__(config)

    def get_unit(self,
                 unit_id):
        """Does a GET request to /Unit.

        Gets the unit

        Args:
            unit_id (string): TODO: type description here.

        Returns:
            LISResponseLISPublicUnit: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Unit')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('UnitId')
                         .value(unit_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseLISPublicUnit.from_dictionary)
        ).execute()

    def get_new_unit(self):
        """Does a GET request to /Unit/GetNewUnit.

        Create and get a new Unit.

        Returns:
            LISResponseLISPublicUnit: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Unit/GetNewUnit')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseLISPublicUnit.from_dictionary)
        ).execute()

    def save_unit(self,
                  unit):
        """Does a POST request to /Unit/SaveUnit.

        Saves the Unit

        Args:
            unit (LISPublicUnit): TODO: type description here.

        Returns:
            LISResponseLISPublicUnit: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Unit/SaveUnit')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(unit))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseLISPublicUnit.from_dictionary)
        ).execute()
