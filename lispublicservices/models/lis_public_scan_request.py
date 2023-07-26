# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicScanRequest(object):

    """Implementation of the 'LISPublicScanRequest' model.

    TODO: type model description here.

    Attributes:
        place_no (string): TODO: type description here.
        sscc (string): TODO: type description here.
        mde_id (int): TODO: type description here.
        mdeip_address (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "place_no": 'placeNo',
        "sscc": 'sscc',
        "mde_id": 'mdeID',
        "mdeip_address": 'mdeipAddress'
    }

    _optionals = [
        'place_no',
        'sscc',
        'mde_id',
        'mdeip_address',
    ]

    def __init__(self,
                 place_no=APIHelper.SKIP,
                 sscc=APIHelper.SKIP,
                 mde_id=APIHelper.SKIP,
                 mdeip_address=APIHelper.SKIP):
        """Constructor for the LISPublicScanRequest class"""

        # Initialize members of the class
        if place_no is not APIHelper.SKIP:
            self.place_no = place_no 
        if sscc is not APIHelper.SKIP:
            self.sscc = sscc 
        if mde_id is not APIHelper.SKIP:
            self.mde_id = mde_id 
        if mdeip_address is not APIHelper.SKIP:
            self.mdeip_address = mdeip_address 

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

        place_no = dictionary.get("placeNo") if dictionary.get("placeNo") else APIHelper.SKIP
        sscc = dictionary.get("sscc") if dictionary.get("sscc") else APIHelper.SKIP
        mde_id = dictionary.get("mdeID") if dictionary.get("mdeID") else APIHelper.SKIP
        mdeip_address = dictionary.get("mdeipAddress") if dictionary.get("mdeipAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(place_no,
                   sscc,
                   mde_id,
                   mdeip_address)
