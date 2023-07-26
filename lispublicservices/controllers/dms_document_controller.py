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
from lispublicservices.models.lis_response_lis_public_dms_document import LISResponseLISPublicDMSDocument
from lispublicservices.models.lis_response_list_lis_public_dms_document_meta import LISResponseListLISPublicDMSDocumentMeta


class DMSDocumentController(BaseController):

    """A Controller to access Endpoints in the lispublicservices API."""
    def __init__(self, config):
        super(DMSDocumentController, self).__init__(config)

    def get_document_data(self,
                          document_id):
        """Does a GET request to /DMSDocument/DocumentData.

        Get DMS document selection

        Args:
            document_id (int): The request.

        Returns:
            LISResponseLISPublicDMSDocument: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/DMSDocument/DocumentData')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('DocumentId')
                         .value(document_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseLISPublicDMSDocument.from_dictionary)
        ).execute()

    def get_documents(self,
                      key_values,
                      document_id=None,
                      dms_archiv=None,
                      dms_folder=None,
                      dms_doc_types=None,
                      document_desc=None,
                      state=None,
                      file_type=None,
                      created_on_from=None,
                      created_on_to=None,
                      key_item_linkage=None):
        """Does a GET request to /DMSDocument/Documents.

        Get DMS document selection. Example Request
        http://{{ServerAddress}}/DMSDocument/Documents?KeyValues=[{"KeyItemName
        ":"AufIntNr","KeyItemValue":"653"}]

        Args:
            key_values (string): Request for DMS Documents Example value:
                [{"KeyItemName":"AufIntNr","KeyItemValue":"653"}]
            document_id (int, optional): Request for DMS Documents
            dms_archiv (string, optional): Request for DMS Documents
            dms_folder (string, optional): Request for DMS Documents
            dms_doc_types (list of string, optional): Request for DMS
                Documents
            document_desc (string, optional): Request for DMS Documents
            state (State3Enum, optional): Request for DMS Documents
            file_type (FileType1Enum, optional): Request for DMS Documents
            created_on_from (datetime, optional): Request for DMS Documents
            created_on_to (datetime, optional): Request for DMS Documents
            key_item_linkage (KeyItemLinkageEnum, optional): Request for DMS
                Documents

        Returns:
            LISResponseListLISPublicDMSDocumentMeta: Response from the API.
                OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/DMSDocument/Documents')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('KeyValues')
                         .value(key_values))
            .query_param(Parameter()
                         .key('DocumentId')
                         .value(document_id))
            .query_param(Parameter()
                         .key('DMSArchiv')
                         .value(dms_archiv))
            .query_param(Parameter()
                         .key('DMSFolder')
                         .value(dms_folder))
            .query_param(Parameter()
                         .key('DMSDocTypes')
                         .value(dms_doc_types))
            .query_param(Parameter()
                         .key('DocumentDesc')
                         .value(document_desc))
            .query_param(Parameter()
                         .key('State')
                         .value(state))
            .query_param(Parameter()
                         .key('FileType')
                         .value(file_type))
            .query_param(Parameter()
                         .key('CreatedOnFrom')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_on_from)))
            .query_param(Parameter()
                         .key('CreatedOnTo')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_on_to)))
            .query_param(Parameter()
                         .key('KeyItemLinkage')
                         .value(key_item_linkage))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LISResponseListLISPublicDMSDocumentMeta.from_dictionary)
        ).execute()
