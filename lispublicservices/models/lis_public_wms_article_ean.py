# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicWMSArticleEan(object):

    """Implementation of the 'LISPublicWMSArticleEan' model.

    The LISPublicWMSArticleEan data contract.

    Attributes:
        article_ean_id (int): Gets or sets ArticleEanId.
        company_id (int): Gets or sets CompanyId.
        changed_by (string): Gets or sets ChangedBy.
        changed_on (datetime): Gets or sets ChangedOn.
        created_by (string): Gets or sets ChangedBy.
        created_on (datetime): Gets or sets ChangedOn.
        article_id (int): Gets or sets ArticleId.
        article_unit_id (int): Gets or sets ArticleUnitId.
        ean (string): Gets or sets EAN.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "article_ean_id": 'articleEanId',
        "company_id": 'companyId',
        "changed_by": 'changedBy',
        "changed_on": 'changedOn',
        "created_by": 'createdBy',
        "created_on": 'createdOn',
        "article_id": 'articleId',
        "article_unit_id": 'articleUnitId',
        "ean": 'ean'
    }

    _optionals = [
        'article_ean_id',
        'company_id',
        'changed_by',
        'changed_on',
        'created_by',
        'created_on',
        'article_id',
        'article_unit_id',
        'ean',
    ]

    def __init__(self,
                 article_ean_id=APIHelper.SKIP,
                 company_id=APIHelper.SKIP,
                 changed_by=APIHelper.SKIP,
                 changed_on=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 created_on=APIHelper.SKIP,
                 article_id=APIHelper.SKIP,
                 article_unit_id=APIHelper.SKIP,
                 ean=APIHelper.SKIP):
        """Constructor for the LISPublicWMSArticleEan class"""

        # Initialize members of the class
        if article_ean_id is not APIHelper.SKIP:
            self.article_ean_id = article_ean_id 
        if company_id is not APIHelper.SKIP:
            self.company_id = company_id 
        if changed_by is not APIHelper.SKIP:
            self.changed_by = changed_by 
        if changed_on is not APIHelper.SKIP:
            self.changed_on = APIHelper.RFC3339DateTime(changed_on) if changed_on else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if created_on is not APIHelper.SKIP:
            self.created_on = APIHelper.RFC3339DateTime(created_on) if created_on else None 
        if article_id is not APIHelper.SKIP:
            self.article_id = article_id 
        if article_unit_id is not APIHelper.SKIP:
            self.article_unit_id = article_unit_id 
        if ean is not APIHelper.SKIP:
            self.ean = ean 

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

        article_ean_id = dictionary.get("articleEanId") if dictionary.get("articleEanId") else APIHelper.SKIP
        company_id = dictionary.get("companyId") if dictionary.get("companyId") else APIHelper.SKIP
        changed_by = dictionary.get("changedBy") if dictionary.get("changedBy") else APIHelper.SKIP
        changed_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("changedOn")).datetime if dictionary.get("changedOn") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdOn")).datetime if dictionary.get("createdOn") else APIHelper.SKIP
        article_id = dictionary.get("articleId") if dictionary.get("articleId") else APIHelper.SKIP
        article_unit_id = dictionary.get("articleUnitId") if dictionary.get("articleUnitId") else APIHelper.SKIP
        ean = dictionary.get("ean") if dictionary.get("ean") else APIHelper.SKIP
        # Return an object of this model
        return cls(article_ean_id,
                   company_id,
                   changed_by,
                   changed_on,
                   created_by,
                   created_on,
                   article_id,
                   article_unit_id,
                   ean)
