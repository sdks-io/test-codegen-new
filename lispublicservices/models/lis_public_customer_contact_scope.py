# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicCustomerContactScope(object):

    """Implementation of the 'LISPublicCustomerContactScope' model.

    The LISCustomerContactScope data contract.

    Attributes:
        consultant (string): Gets or sets Consultant.
        phone (string): Gets or sets Phone.
        mobile (string): Gets or sets Mobile.
        fax (string): Gets or sets Fax.
        homepage (string): Gets or sets Homepage.
        email (string): Gets or sets Email.
        language_id (int): Gets or sets LanguageId.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consultant": 'consultant',
        "phone": 'phone',
        "mobile": 'mobile',
        "fax": 'fax',
        "homepage": 'homepage',
        "email": 'email',
        "language_id": 'languageId'
    }

    _optionals = [
        'consultant',
        'phone',
        'mobile',
        'fax',
        'homepage',
        'email',
        'language_id',
    ]

    def __init__(self,
                 consultant=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 mobile=APIHelper.SKIP,
                 fax=APIHelper.SKIP,
                 homepage=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 language_id=APIHelper.SKIP):
        """Constructor for the LISPublicCustomerContactScope class"""

        # Initialize members of the class
        if consultant is not APIHelper.SKIP:
            self.consultant = consultant 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if mobile is not APIHelper.SKIP:
            self.mobile = mobile 
        if fax is not APIHelper.SKIP:
            self.fax = fax 
        if homepage is not APIHelper.SKIP:
            self.homepage = homepage 
        if email is not APIHelper.SKIP:
            self.email = email 
        if language_id is not APIHelper.SKIP:
            self.language_id = language_id 

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

        consultant = dictionary.get("consultant") if dictionary.get("consultant") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        mobile = dictionary.get("mobile") if dictionary.get("mobile") else APIHelper.SKIP
        fax = dictionary.get("fax") if dictionary.get("fax") else APIHelper.SKIP
        homepage = dictionary.get("homepage") if dictionary.get("homepage") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        language_id = dictionary.get("languageId") if dictionary.get("languageId") else APIHelper.SKIP
        # Return an object of this model
        return cls(consultant,
                   phone,
                   mobile,
                   fax,
                   homepage,
                   email,
                   language_id)
