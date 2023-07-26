# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicOrderAddressRole(object):

    """Implementation of the 'LISPublicOrderAddressRole' model.

    The LISOrderAddressRole data contract.

    Attributes:
        order_id (int): Gets or sets OrderId.
        sequential_no (int): Gets or sets SequentialNo.
        changed_on (datetime): Gets or sets ChangedOn.
        changed_by (string): Gets or sets ChangedBy.
        customer_id (int): Gets or sets CustomerId.
        address_type_id (int): Gets or sets AddressTypeId.
        note (string): Gets or sets Note.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_id": 'orderId',
        "sequential_no": 'sequentialNo',
        "changed_on": 'changedOn',
        "changed_by": 'changedBy',
        "customer_id": 'customerId',
        "address_type_id": 'addressTypeId',
        "note": 'note'
    }

    _optionals = [
        'order_id',
        'sequential_no',
        'changed_on',
        'changed_by',
        'customer_id',
        'address_type_id',
        'note',
    ]

    def __init__(self,
                 order_id=APIHelper.SKIP,
                 sequential_no=APIHelper.SKIP,
                 changed_on=APIHelper.SKIP,
                 changed_by=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 address_type_id=APIHelper.SKIP,
                 note=APIHelper.SKIP):
        """Constructor for the LISPublicOrderAddressRole class"""

        # Initialize members of the class
        if order_id is not APIHelper.SKIP:
            self.order_id = order_id 
        if sequential_no is not APIHelper.SKIP:
            self.sequential_no = sequential_no 
        if changed_on is not APIHelper.SKIP:
            self.changed_on = APIHelper.RFC3339DateTime(changed_on) if changed_on else None 
        if changed_by is not APIHelper.SKIP:
            self.changed_by = changed_by 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if address_type_id is not APIHelper.SKIP:
            self.address_type_id = address_type_id 
        if note is not APIHelper.SKIP:
            self.note = note 

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

        order_id = dictionary.get("orderId") if dictionary.get("orderId") else APIHelper.SKIP
        sequential_no = dictionary.get("sequentialNo") if dictionary.get("sequentialNo") else APIHelper.SKIP
        changed_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("changedOn")).datetime if dictionary.get("changedOn") else APIHelper.SKIP
        changed_by = dictionary.get("changedBy") if dictionary.get("changedBy") else APIHelper.SKIP
        customer_id = dictionary.get("customerId") if dictionary.get("customerId") else APIHelper.SKIP
        address_type_id = dictionary.get("addressTypeId") if dictionary.get("addressTypeId") else APIHelper.SKIP
        note = dictionary.get("note") if dictionary.get("note") else APIHelper.SKIP
        # Return an object of this model
        return cls(order_id,
                   sequential_no,
                   changed_on,
                   changed_by,
                   customer_id,
                   address_type_id,
                   note)
