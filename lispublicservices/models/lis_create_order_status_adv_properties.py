# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISCreateOrderStatusAdvProperties(object):

    """Implementation of the 'LISCreateOrderStatusAdvProperties' model.

    The LISOrderStatusEntityAdvProperties data contract.

    Attributes:
        order_item (int): Gets or sets OrderItem.
        difference_quantity (int): Gets or sets DifferenceQuantity.
        difference_unit (string): Gets or sets DifferenceUnit.
        note (string): Gets or sets Note.
        event_date (datetime): Gets or sets EventDate.
        event_time (datetime): Gets or sets EventTime.
        edi_status (int): Gets or sets EDIStatus.
        data_source (int): Gets or sets DataSource.
        generated_internal_no (int): Gets or sets GeneratedInternalNo.
        carrier_id (int): Gets or sets CarrierId.
        special_invoicing_id (int): Gets or sets SpecialInvoicingId.
        receipt (string): Gets or sets Receipt.
        tour_id (int): Gets or sets TourId.
        tour_no (int): Gets or sets TourNo.
        status_category_id (string): Gets or sets the status category id.
        contact_information (string): Gets or sets the contact information.
        text_master_id (int): Gets or sets the text master identifier.
        long_text (string): Gets or sets the long text.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_item": 'orderItem',
        "difference_quantity": 'differenceQuantity',
        "difference_unit": 'differenceUnit',
        "note": 'note',
        "event_date": 'eventDate',
        "event_time": 'eventTime',
        "edi_status": 'ediStatus',
        "data_source": 'dataSource',
        "generated_internal_no": 'generatedInternalNo',
        "carrier_id": 'carrierId',
        "special_invoicing_id": 'specialInvoicingId',
        "receipt": 'receipt',
        "tour_id": 'tourId',
        "tour_no": 'tourNo',
        "status_category_id": 'statusCategoryId',
        "contact_information": 'contactInformation',
        "text_master_id": 'textMasterId',
        "long_text": 'longText'
    }

    _optionals = [
        'order_item',
        'difference_quantity',
        'difference_unit',
        'note',
        'event_date',
        'event_time',
        'edi_status',
        'data_source',
        'generated_internal_no',
        'carrier_id',
        'special_invoicing_id',
        'receipt',
        'tour_id',
        'tour_no',
        'status_category_id',
        'contact_information',
        'text_master_id',
        'long_text',
    ]

    def __init__(self,
                 order_item=APIHelper.SKIP,
                 difference_quantity=APIHelper.SKIP,
                 difference_unit=APIHelper.SKIP,
                 note=APIHelper.SKIP,
                 event_date=APIHelper.SKIP,
                 event_time=APIHelper.SKIP,
                 edi_status=APIHelper.SKIP,
                 data_source=APIHelper.SKIP,
                 generated_internal_no=APIHelper.SKIP,
                 carrier_id=APIHelper.SKIP,
                 special_invoicing_id=APIHelper.SKIP,
                 receipt=APIHelper.SKIP,
                 tour_id=APIHelper.SKIP,
                 tour_no=APIHelper.SKIP,
                 status_category_id=APIHelper.SKIP,
                 contact_information=APIHelper.SKIP,
                 text_master_id=APIHelper.SKIP,
                 long_text=APIHelper.SKIP):
        """Constructor for the LISCreateOrderStatusAdvProperties class"""

        # Initialize members of the class
        if order_item is not APIHelper.SKIP:
            self.order_item = order_item 
        if difference_quantity is not APIHelper.SKIP:
            self.difference_quantity = difference_quantity 
        if difference_unit is not APIHelper.SKIP:
            self.difference_unit = difference_unit 
        if note is not APIHelper.SKIP:
            self.note = note 
        if event_date is not APIHelper.SKIP:
            self.event_date = APIHelper.RFC3339DateTime(event_date) if event_date else None 
        if event_time is not APIHelper.SKIP:
            self.event_time = APIHelper.RFC3339DateTime(event_time) if event_time else None 
        if edi_status is not APIHelper.SKIP:
            self.edi_status = edi_status 
        if data_source is not APIHelper.SKIP:
            self.data_source = data_source 
        if generated_internal_no is not APIHelper.SKIP:
            self.generated_internal_no = generated_internal_no 
        if carrier_id is not APIHelper.SKIP:
            self.carrier_id = carrier_id 
        if special_invoicing_id is not APIHelper.SKIP:
            self.special_invoicing_id = special_invoicing_id 
        if receipt is not APIHelper.SKIP:
            self.receipt = receipt 
        if tour_id is not APIHelper.SKIP:
            self.tour_id = tour_id 
        if tour_no is not APIHelper.SKIP:
            self.tour_no = tour_no 
        if status_category_id is not APIHelper.SKIP:
            self.status_category_id = status_category_id 
        if contact_information is not APIHelper.SKIP:
            self.contact_information = contact_information 
        if text_master_id is not APIHelper.SKIP:
            self.text_master_id = text_master_id 
        if long_text is not APIHelper.SKIP:
            self.long_text = long_text 

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

        order_item = dictionary.get("orderItem") if dictionary.get("orderItem") else APIHelper.SKIP
        difference_quantity = dictionary.get("differenceQuantity") if dictionary.get("differenceQuantity") else APIHelper.SKIP
        difference_unit = dictionary.get("differenceUnit") if dictionary.get("differenceUnit") else APIHelper.SKIP
        note = dictionary.get("note") if dictionary.get("note") else APIHelper.SKIP
        event_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("eventDate")).datetime if dictionary.get("eventDate") else APIHelper.SKIP
        event_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("eventTime")).datetime if dictionary.get("eventTime") else APIHelper.SKIP
        edi_status = dictionary.get("ediStatus") if dictionary.get("ediStatus") else APIHelper.SKIP
        data_source = dictionary.get("dataSource") if dictionary.get("dataSource") else APIHelper.SKIP
        generated_internal_no = dictionary.get("generatedInternalNo") if dictionary.get("generatedInternalNo") else APIHelper.SKIP
        carrier_id = dictionary.get("carrierId") if dictionary.get("carrierId") else APIHelper.SKIP
        special_invoicing_id = dictionary.get("specialInvoicingId") if dictionary.get("specialInvoicingId") else APIHelper.SKIP
        receipt = dictionary.get("receipt") if dictionary.get("receipt") else APIHelper.SKIP
        tour_id = dictionary.get("tourId") if dictionary.get("tourId") else APIHelper.SKIP
        tour_no = dictionary.get("tourNo") if dictionary.get("tourNo") else APIHelper.SKIP
        status_category_id = dictionary.get("statusCategoryId") if dictionary.get("statusCategoryId") else APIHelper.SKIP
        contact_information = dictionary.get("contactInformation") if dictionary.get("contactInformation") else APIHelper.SKIP
        text_master_id = dictionary.get("textMasterId") if dictionary.get("textMasterId") else APIHelper.SKIP
        long_text = dictionary.get("longText") if dictionary.get("longText") else APIHelper.SKIP
        # Return an object of this model
        return cls(order_item,
                   difference_quantity,
                   difference_unit,
                   note,
                   event_date,
                   event_time,
                   edi_status,
                   data_source,
                   generated_internal_no,
                   carrier_id,
                   special_invoicing_id,
                   receipt,
                   tour_id,
                   tour_no,
                   status_category_id,
                   contact_information,
                   text_master_id,
                   long_text)
