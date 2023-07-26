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
from lispublicservices.models.lis_response_string import LISResponseString


class AuthenticationController(BaseController):

    """A Controller to access Endpoints in the lispublicservices API."""
    def __init__(self, config):
        super(AuthenticationController, self).__init__(config)

    def authenticate(self,
                     request,
                     authorization):
        """Does a POST request to /Auth.

         #### Getting the bearer token via curl command
        ---  
        ```
        curl --location --request POST 'http://api.lis.eu/Auth' \
        --header 'Authorization: Basic bXZsb2g6JFdpbjJrOHIy' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "companyId": 1,
          "divisionId": 1,
          "departmentId": 0
        }'
        ```  
        The WinSped user credentials have to be encoded as a** Base64 String**
        instead of(user:password) its the Base64 string value ** Basic
        bXZsb2g6JFdpbjJrOHIy ** for test credentials.The request also needs
        your **company**, ** division** and** department id**.
         
         
        #### Getting the bearer token via api endpoint:  
        ---  
         Use the Basic Authentication Endpoint to receive your bearer token.

        Args:
            request (LISAuthenticationRequest): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            LISResponseString: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Auth')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(request))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseString.from_dictionary)
        ).execute()
