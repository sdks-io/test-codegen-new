# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicCustomerLogisticProviderNetwork(object):

    """Implementation of the 'LISPublicCustomerLogisticProviderNetwork' model.

    The LISCustomerLogisticProviderNetwork

    Attributes:
        system_traffic_id (int): Gets or sets the system traffic identifier.
        customer_id (int): Gets or sets the customer identifier.
        service_provider_id (int): Gets or sets the service provider
            identifier.
        service_id (int): Gets or sets the service identifier.
        last_import (datetime): Gets or sets the last import.
        is_envelop_depot (bool): Gets or sets a value indicating whether this
            instance is envelop depot.
        info_text_1 (string): Gets or sets the information text1.
        info_text_2 (string): Gets or sets the value1.
        info_text_3 (string): Gets or sets the value1.
        info_text_4 (string): Gets or sets the value1.
        info_text_5 (string): Gets or sets the value1.
        info_text_6 (string): Gets or sets the value1.
        info_text_7 (string): Gets or sets the value1.
        info_text_8 (string): Gets or sets the value1.
        info_text_9 (string): Gets or sets the value1.
        info_text_10 (string): Gets or sets the value1.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "system_traffic_id": 'systemTrafficId',
        "customer_id": 'customerId',
        "service_provider_id": 'serviceProviderId',
        "service_id": 'serviceId',
        "last_import": 'lastImport',
        "is_envelop_depot": 'isEnvelopDepot',
        "info_text_1": 'infoText1',
        "info_text_2": 'infoText2',
        "info_text_3": 'infoText3',
        "info_text_4": 'infoText4',
        "info_text_5": 'infoText5',
        "info_text_6": 'infoText6',
        "info_text_7": 'infoText7',
        "info_text_8": 'infoText8',
        "info_text_9": 'infoText9',
        "info_text_10": 'infoText10'
    }

    _optionals = [
        'system_traffic_id',
        'customer_id',
        'service_provider_id',
        'service_id',
        'last_import',
        'is_envelop_depot',
        'info_text_1',
        'info_text_2',
        'info_text_3',
        'info_text_4',
        'info_text_5',
        'info_text_6',
        'info_text_7',
        'info_text_8',
        'info_text_9',
        'info_text_10',
    ]

    def __init__(self,
                 system_traffic_id=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 service_provider_id=APIHelper.SKIP,
                 service_id=APIHelper.SKIP,
                 last_import=APIHelper.SKIP,
                 is_envelop_depot=APIHelper.SKIP,
                 info_text_1=APIHelper.SKIP,
                 info_text_2=APIHelper.SKIP,
                 info_text_3=APIHelper.SKIP,
                 info_text_4=APIHelper.SKIP,
                 info_text_5=APIHelper.SKIP,
                 info_text_6=APIHelper.SKIP,
                 info_text_7=APIHelper.SKIP,
                 info_text_8=APIHelper.SKIP,
                 info_text_9=APIHelper.SKIP,
                 info_text_10=APIHelper.SKIP):
        """Constructor for the LISPublicCustomerLogisticProviderNetwork class"""

        # Initialize members of the class
        if system_traffic_id is not APIHelper.SKIP:
            self.system_traffic_id = system_traffic_id 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if service_provider_id is not APIHelper.SKIP:
            self.service_provider_id = service_provider_id 
        if service_id is not APIHelper.SKIP:
            self.service_id = service_id 
        if last_import is not APIHelper.SKIP:
            self.last_import = APIHelper.RFC3339DateTime(last_import) if last_import else None 
        if is_envelop_depot is not APIHelper.SKIP:
            self.is_envelop_depot = is_envelop_depot 
        if info_text_1 is not APIHelper.SKIP:
            self.info_text_1 = info_text_1 
        if info_text_2 is not APIHelper.SKIP:
            self.info_text_2 = info_text_2 
        if info_text_3 is not APIHelper.SKIP:
            self.info_text_3 = info_text_3 
        if info_text_4 is not APIHelper.SKIP:
            self.info_text_4 = info_text_4 
        if info_text_5 is not APIHelper.SKIP:
            self.info_text_5 = info_text_5 
        if info_text_6 is not APIHelper.SKIP:
            self.info_text_6 = info_text_6 
        if info_text_7 is not APIHelper.SKIP:
            self.info_text_7 = info_text_7 
        if info_text_8 is not APIHelper.SKIP:
            self.info_text_8 = info_text_8 
        if info_text_9 is not APIHelper.SKIP:
            self.info_text_9 = info_text_9 
        if info_text_10 is not APIHelper.SKIP:
            self.info_text_10 = info_text_10 

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

        system_traffic_id = dictionary.get("systemTrafficId") if dictionary.get("systemTrafficId") else APIHelper.SKIP
        customer_id = dictionary.get("customerId") if dictionary.get("customerId") else APIHelper.SKIP
        service_provider_id = dictionary.get("serviceProviderId") if dictionary.get("serviceProviderId") else APIHelper.SKIP
        service_id = dictionary.get("serviceId") if dictionary.get("serviceId") else APIHelper.SKIP
        last_import = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastImport")).datetime if dictionary.get("lastImport") else APIHelper.SKIP
        is_envelop_depot = dictionary.get("isEnvelopDepot") if "isEnvelopDepot" in dictionary.keys() else APIHelper.SKIP
        info_text_1 = dictionary.get("infoText1") if dictionary.get("infoText1") else APIHelper.SKIP
        info_text_2 = dictionary.get("infoText2") if dictionary.get("infoText2") else APIHelper.SKIP
        info_text_3 = dictionary.get("infoText3") if dictionary.get("infoText3") else APIHelper.SKIP
        info_text_4 = dictionary.get("infoText4") if dictionary.get("infoText4") else APIHelper.SKIP
        info_text_5 = dictionary.get("infoText5") if dictionary.get("infoText5") else APIHelper.SKIP
        info_text_6 = dictionary.get("infoText6") if dictionary.get("infoText6") else APIHelper.SKIP
        info_text_7 = dictionary.get("infoText7") if dictionary.get("infoText7") else APIHelper.SKIP
        info_text_8 = dictionary.get("infoText8") if dictionary.get("infoText8") else APIHelper.SKIP
        info_text_9 = dictionary.get("infoText9") if dictionary.get("infoText9") else APIHelper.SKIP
        info_text_10 = dictionary.get("infoText10") if dictionary.get("infoText10") else APIHelper.SKIP
        # Return an object of this model
        return cls(system_traffic_id,
                   customer_id,
                   service_provider_id,
                   service_id,
                   last_import,
                   is_envelop_depot,
                   info_text_1,
                   info_text_2,
                   info_text_3,
                   info_text_4,
                   info_text_5,
                   info_text_6,
                   info_text_7,
                   info_text_8,
                   info_text_9,
                   info_text_10)
