# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicCostSurchargeItem(object):

    """Implementation of the 'LISPublicCostSurchargeItem' model.

    The surcharge for costs

    Attributes:
        surcharge_no (int): Gets or sets the surcharge no.
        charge_id (int): Gets or sets the charge id.
        number_of_decimal_places (int): Gets or sets the number of decimal
            places.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "surcharge_no": 'surchargeNo',
        "charge_id": 'chargeId',
        "number_of_decimal_places": 'numberOfDecimalPlaces'
    }

    _optionals = [
        'surcharge_no',
        'charge_id',
        'number_of_decimal_places',
    ]

    def __init__(self,
                 surcharge_no=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 number_of_decimal_places=APIHelper.SKIP):
        """Constructor for the LISPublicCostSurchargeItem class"""

        # Initialize members of the class
        if surcharge_no is not APIHelper.SKIP:
            self.surcharge_no = surcharge_no 
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 
        if number_of_decimal_places is not APIHelper.SKIP:
            self.number_of_decimal_places = number_of_decimal_places 

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

        surcharge_no = dictionary.get("surchargeNo") if dictionary.get("surchargeNo") else APIHelper.SKIP
        charge_id = dictionary.get("chargeId") if dictionary.get("chargeId") else APIHelper.SKIP
        number_of_decimal_places = dictionary.get("numberOfDecimalPlaces") if dictionary.get("numberOfDecimalPlaces") else APIHelper.SKIP
        # Return an object of this model
        return cls(surcharge_no,
                   charge_id,
                   number_of_decimal_places)
