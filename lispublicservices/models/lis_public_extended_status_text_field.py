# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicExtendedStatusTextField(object):

    """Implementation of the 'LISPublicExtendedStatusTextField' model.

    Extended status text field for status events

    Attributes:
        status_text_ext_field_id (int): Gets or sets the status text ext field
            identifier.
        status_text_typ (StatusTextTypEnum): Gets or sets the status text
            typ.
        status_no (int): Gets or sets the status no.
        extended_field_name (string): Gets or sets the name of the extended
            field.
        is_required_field (bool): Gets or sets a value indicating whether this
            instance is required field.
        set_status_remark (bool): Gets or sets a value indicating whether [set
            status remark].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status_text_ext_field_id": 'statusTextExtFieldId',
        "status_text_typ": 'statusTextTyp',
        "status_no": 'statusNo',
        "extended_field_name": 'extendedFieldName',
        "is_required_field": 'isRequiredField',
        "set_status_remark": 'setStatusRemark'
    }

    _optionals = [
        'status_text_ext_field_id',
        'status_text_typ',
        'status_no',
        'extended_field_name',
        'is_required_field',
        'set_status_remark',
    ]

    def __init__(self,
                 status_text_ext_field_id=APIHelper.SKIP,
                 status_text_typ=APIHelper.SKIP,
                 status_no=APIHelper.SKIP,
                 extended_field_name=APIHelper.SKIP,
                 is_required_field=APIHelper.SKIP,
                 set_status_remark=APIHelper.SKIP):
        """Constructor for the LISPublicExtendedStatusTextField class"""

        # Initialize members of the class
        if status_text_ext_field_id is not APIHelper.SKIP:
            self.status_text_ext_field_id = status_text_ext_field_id 
        if status_text_typ is not APIHelper.SKIP:
            self.status_text_typ = status_text_typ 
        if status_no is not APIHelper.SKIP:
            self.status_no = status_no 
        if extended_field_name is not APIHelper.SKIP:
            self.extended_field_name = extended_field_name 
        if is_required_field is not APIHelper.SKIP:
            self.is_required_field = is_required_field 
        if set_status_remark is not APIHelper.SKIP:
            self.set_status_remark = set_status_remark 

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

        status_text_ext_field_id = dictionary.get("statusTextExtFieldId") if dictionary.get("statusTextExtFieldId") else APIHelper.SKIP
        status_text_typ = dictionary.get("statusTextTyp") if dictionary.get("statusTextTyp") else APIHelper.SKIP
        status_no = dictionary.get("statusNo") if dictionary.get("statusNo") else APIHelper.SKIP
        extended_field_name = dictionary.get("extendedFieldName") if dictionary.get("extendedFieldName") else APIHelper.SKIP
        is_required_field = dictionary.get("isRequiredField") if "isRequiredField" in dictionary.keys() else APIHelper.SKIP
        set_status_remark = dictionary.get("setStatusRemark") if "setStatusRemark" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status_text_ext_field_id,
                   status_text_typ,
                   status_no,
                   extended_field_name,
                   is_required_field,
                   set_status_remark)
