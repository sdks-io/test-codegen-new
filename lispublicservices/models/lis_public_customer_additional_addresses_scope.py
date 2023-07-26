# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper
from lispublicservices.models.lis_public_customer_address_role import LISPublicCustomerAddressRole


class LISPublicCustomerAdditionalAddressesScope(object):

    """Implementation of the 'LISPublicCustomerAdditionalAddressesScope' model.

    The LISCustomerAdditionalAddressesScope data contract.

    Attributes:
        address_roles (list of LISPublicCustomerAddressRole): Gets or sets
            AddressRoles.
        copy_lock (bool): Gets or sets the copy lock.
        transshipment_point (int): Gets or sets the transshipment point.
        warehouse_scanning (bool): Gets or sets the warehouse scanning.
        external_address_id (string): Gets or sets the external address id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_roles": 'addressRoles',
        "copy_lock": 'copyLock',
        "transshipment_point": 'transshipmentPoint',
        "warehouse_scanning": 'warehouseScanning',
        "external_address_id": 'externalAddressId'
    }

    _optionals = [
        'address_roles',
        'copy_lock',
        'transshipment_point',
        'warehouse_scanning',
        'external_address_id',
    ]

    def __init__(self,
                 address_roles=APIHelper.SKIP,
                 copy_lock=APIHelper.SKIP,
                 transshipment_point=APIHelper.SKIP,
                 warehouse_scanning=APIHelper.SKIP,
                 external_address_id=APIHelper.SKIP):
        """Constructor for the LISPublicCustomerAdditionalAddressesScope class"""

        # Initialize members of the class
        if address_roles is not APIHelper.SKIP:
            self.address_roles = address_roles 
        if copy_lock is not APIHelper.SKIP:
            self.copy_lock = copy_lock 
        if transshipment_point is not APIHelper.SKIP:
            self.transshipment_point = transshipment_point 
        if warehouse_scanning is not APIHelper.SKIP:
            self.warehouse_scanning = warehouse_scanning 
        if external_address_id is not APIHelper.SKIP:
            self.external_address_id = external_address_id 

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

        address_roles = None
        if dictionary.get('addressRoles') is not None:
            address_roles = [LISPublicCustomerAddressRole.from_dictionary(x) for x in dictionary.get('addressRoles')]
        else:
            address_roles = APIHelper.SKIP
        copy_lock = dictionary.get("copyLock") if "copyLock" in dictionary.keys() else APIHelper.SKIP
        transshipment_point = dictionary.get("transshipmentPoint") if dictionary.get("transshipmentPoint") else APIHelper.SKIP
        warehouse_scanning = dictionary.get("warehouseScanning") if "warehouseScanning" in dictionary.keys() else APIHelper.SKIP
        external_address_id = dictionary.get("externalAddressId") if dictionary.get("externalAddressId") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_roles,
                   copy_lock,
                   transshipment_point,
                   warehouse_scanning,
                   external_address_id)
