# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISResponseListInt32(object):

    """Implementation of the 'LISResponse[List[Int32]]' model.

    The api response class.

    Attributes:
        operation_result (list of int): The operation result.
        message (list of string): The message.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "operation_result": 'operationResult',
        "message": 'message'
    }

    _optionals = [
        'operation_result',
        'message',
    ]

    def __init__(self,
                 operation_result=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the LISResponseListInt32 class"""

        # Initialize members of the class
        if operation_result is not APIHelper.SKIP:
            self.operation_result = operation_result 
        if message is not APIHelper.SKIP:
            self.message = message 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        operation_result = dictionary.get("operationResult") if dictionary.get("operationResult") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(operation_result,
                   message)
