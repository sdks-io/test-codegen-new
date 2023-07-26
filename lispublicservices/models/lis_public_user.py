# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicUser(object):

    """Implementation of the 'LISPublicUser' model.

    TODO: type model description here.

    Attributes:
        account_name (string): The account name for the user

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName'
    }

    _optionals = [
        'account_name',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP):
        """Constructor for the LISPublicUser class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 

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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name)
