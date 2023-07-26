# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper
from lispublicservices.models.lis_public_extended_field_data_type import LISPublicExtendedFieldDataType


class LISPublicExtendedDataField(object):

    """Implementation of the 'LISPublicExtendedDataField' model.

    This class represents a column value (cell) within an
    {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtended
    DataTable}.
    Besides the schema information of the column it contains a specific data
    value.

    Attributes:
        value (object): Gets or sets the value of the cell.
        original_value (object): Gets or sets the original value.
        caption (string): Gets or sets the caption.
        column_name (string): Gets or sets the name of the column.
        data_type (LISPublicExtendedFieldDataType): This class describes the
            data type of a extended table column.
        is_key (bool): Gets or sets a value indicating whether this instance
            is part of a primary key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": 'value',
        "original_value": 'originalValue',
        "caption": 'caption',
        "column_name": 'columnName',
        "data_type": 'dataType',
        "is_key": 'isKey'
    }

    _optionals = [
        'value',
        'original_value',
        'caption',
        'column_name',
        'data_type',
        'is_key',
    ]

    def __init__(self,
                 value=APIHelper.SKIP,
                 original_value=APIHelper.SKIP,
                 caption=APIHelper.SKIP,
                 column_name=APIHelper.SKIP,
                 data_type=APIHelper.SKIP,
                 is_key=APIHelper.SKIP):
        """Constructor for the LISPublicExtendedDataField class"""

        # Initialize members of the class
        if value is not APIHelper.SKIP:
            self.value = value 
        if original_value is not APIHelper.SKIP:
            self.original_value = original_value 
        if caption is not APIHelper.SKIP:
            self.caption = caption 
        if column_name is not APIHelper.SKIP:
            self.column_name = column_name 
        if data_type is not APIHelper.SKIP:
            self.data_type = data_type 
        if is_key is not APIHelper.SKIP:
            self.is_key = is_key 

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

        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        original_value = dictionary.get("originalValue") if dictionary.get("originalValue") else APIHelper.SKIP
        caption = dictionary.get("caption") if dictionary.get("caption") else APIHelper.SKIP
        column_name = dictionary.get("columnName") if dictionary.get("columnName") else APIHelper.SKIP
        data_type = LISPublicExtendedFieldDataType.from_dictionary(dictionary.get('dataType')) if 'dataType' in dictionary.keys() else APIHelper.SKIP
        is_key = dictionary.get("isKey") if "isKey" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(value,
                   original_value,
                   caption,
                   column_name,
                   data_type,
                   is_key)
