# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper
from lispublicservices.models.lis_public_order_aggregates import LISPublicOrderAggregates
from lispublicservices.models.lis_public_order_appointment import LISPublicOrderAppointment
from lispublicservices.models.lis_public_shipment_station import LISPublicShipmentStation


class LISPublicTransportSectionBordero(object):

    """Implementation of the 'LISPublicTransportSectionBordero' model.

    TODO: type model description here.

    Attributes:
        bordero_id (int): Gets or sets the bordero id.
        transport_section_type (string): Gets or sets the TranportSectionType
        company_id (int): Gets or sets CompanyId.
        division_id (int): Gets or sets DivisionId.
        department_id (int): Gets or sets DepartmentId.
        tour_id (int): Gets or sets TourId.
        id (int): Gets or sets Id.
        no (int): Gets or sets No.
        sub_no (int): Gets or sets SubNo.
        sequence (int): Gets or sets Sequence.
        is_last (bool): Gets or sets IsLast.
        appointments (list of LISPublicOrderAppointment): Gets or sets
            Appointments.
        aggregates (LISPublicOrderAggregates): The LIS Order aggregates.
        stations (list of LISPublicShipmentStation): Gets or sets Stations.
        prev_shipment_dispatch_calculated_unloading_time (datetime): Gets or
            sets the order informations.
        prev_shipment_id (int): Gets or sets the type of the order.
        prev_shipment_tour_id (int): Gets or sets the previous shipment tour
            no.
        prev_shipment_tour_no (int): Gets or sets the previous shipment tour
            identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bordero_id": 'borderoId',
        "transport_section_type": 'transportSectionType',
        "company_id": 'companyId',
        "division_id": 'divisionId',
        "department_id": 'departmentId',
        "tour_id": 'tourId',
        "id": 'id',
        "no": 'no',
        "sub_no": 'subNo',
        "sequence": 'sequence',
        "is_last": 'isLast',
        "appointments": 'appointments',
        "aggregates": 'aggregates',
        "stations": 'stations',
        "prev_shipment_dispatch_calculated_unloading_time": 'prevShipmentDispatchCalculatedUnloadingTime',
        "prev_shipment_id": 'prevShipmentId',
        "prev_shipment_tour_id": 'prevShipmentTourId',
        "prev_shipment_tour_no": 'prevShipmentTourNo'
    }

    _optionals = [
        'bordero_id',
        'transport_section_type',
        'company_id',
        'division_id',
        'department_id',
        'tour_id',
        'id',
        'no',
        'sub_no',
        'sequence',
        'is_last',
        'appointments',
        'aggregates',
        'stations',
        'prev_shipment_dispatch_calculated_unloading_time',
        'prev_shipment_id',
        'prev_shipment_tour_id',
        'prev_shipment_tour_no',
    ]

    def __init__(self,
                 bordero_id=APIHelper.SKIP,
                 transport_section_type=APIHelper.SKIP,
                 company_id=APIHelper.SKIP,
                 division_id=APIHelper.SKIP,
                 department_id=APIHelper.SKIP,
                 tour_id=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 no=APIHelper.SKIP,
                 sub_no=APIHelper.SKIP,
                 sequence=APIHelper.SKIP,
                 is_last=APIHelper.SKIP,
                 appointments=APIHelper.SKIP,
                 aggregates=APIHelper.SKIP,
                 stations=APIHelper.SKIP,
                 prev_shipment_dispatch_calculated_unloading_time=APIHelper.SKIP,
                 prev_shipment_id=APIHelper.SKIP,
                 prev_shipment_tour_id=APIHelper.SKIP,
                 prev_shipment_tour_no=APIHelper.SKIP):
        """Constructor for the LISPublicTransportSectionBordero class"""

        # Initialize members of the class
        if bordero_id is not APIHelper.SKIP:
            self.bordero_id = bordero_id 
        if transport_section_type is not APIHelper.SKIP:
            self.transport_section_type = transport_section_type 
        if company_id is not APIHelper.SKIP:
            self.company_id = company_id 
        if division_id is not APIHelper.SKIP:
            self.division_id = division_id 
        if department_id is not APIHelper.SKIP:
            self.department_id = department_id 
        if tour_id is not APIHelper.SKIP:
            self.tour_id = tour_id 
        if id is not APIHelper.SKIP:
            self.id = id 
        if no is not APIHelper.SKIP:
            self.no = no 
        if sub_no is not APIHelper.SKIP:
            self.sub_no = sub_no 
        if sequence is not APIHelper.SKIP:
            self.sequence = sequence 
        if is_last is not APIHelper.SKIP:
            self.is_last = is_last 
        if appointments is not APIHelper.SKIP:
            self.appointments = appointments 
        if aggregates is not APIHelper.SKIP:
            self.aggregates = aggregates 
        if stations is not APIHelper.SKIP:
            self.stations = stations 
        if prev_shipment_dispatch_calculated_unloading_time is not APIHelper.SKIP:
            self.prev_shipment_dispatch_calculated_unloading_time = APIHelper.RFC3339DateTime(prev_shipment_dispatch_calculated_unloading_time) if prev_shipment_dispatch_calculated_unloading_time else None 
        if prev_shipment_id is not APIHelper.SKIP:
            self.prev_shipment_id = prev_shipment_id 
        if prev_shipment_tour_id is not APIHelper.SKIP:
            self.prev_shipment_tour_id = prev_shipment_tour_id 
        if prev_shipment_tour_no is not APIHelper.SKIP:
            self.prev_shipment_tour_no = prev_shipment_tour_no 

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

        bordero_id = dictionary.get("borderoId") if dictionary.get("borderoId") else APIHelper.SKIP
        transport_section_type = dictionary.get("transportSectionType") if dictionary.get("transportSectionType") else APIHelper.SKIP
        company_id = dictionary.get("companyId") if dictionary.get("companyId") else APIHelper.SKIP
        division_id = dictionary.get("divisionId") if dictionary.get("divisionId") else APIHelper.SKIP
        department_id = dictionary.get("departmentId") if dictionary.get("departmentId") else APIHelper.SKIP
        tour_id = dictionary.get("tourId") if dictionary.get("tourId") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        no = dictionary.get("no") if dictionary.get("no") else APIHelper.SKIP
        sub_no = dictionary.get("subNo") if dictionary.get("subNo") else APIHelper.SKIP
        sequence = dictionary.get("sequence") if dictionary.get("sequence") else APIHelper.SKIP
        is_last = dictionary.get("isLast") if "isLast" in dictionary.keys() else APIHelper.SKIP
        appointments = None
        if dictionary.get('appointments') is not None:
            appointments = [LISPublicOrderAppointment.from_dictionary(x) for x in dictionary.get('appointments')]
        else:
            appointments = APIHelper.SKIP
        aggregates = LISPublicOrderAggregates.from_dictionary(dictionary.get('aggregates')) if 'aggregates' in dictionary.keys() else APIHelper.SKIP
        stations = None
        if dictionary.get('stations') is not None:
            stations = [LISPublicShipmentStation.from_dictionary(x) for x in dictionary.get('stations')]
        else:
            stations = APIHelper.SKIP
        prev_shipment_dispatch_calculated_unloading_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("prevShipmentDispatchCalculatedUnloadingTime")).datetime if dictionary.get("prevShipmentDispatchCalculatedUnloadingTime") else APIHelper.SKIP
        prev_shipment_id = dictionary.get("prevShipmentId") if dictionary.get("prevShipmentId") else APIHelper.SKIP
        prev_shipment_tour_id = dictionary.get("prevShipmentTourId") if dictionary.get("prevShipmentTourId") else APIHelper.SKIP
        prev_shipment_tour_no = dictionary.get("prevShipmentTourNo") if dictionary.get("prevShipmentTourNo") else APIHelper.SKIP
        # Return an object of this model
        return cls(bordero_id,
                   transport_section_type,
                   company_id,
                   division_id,
                   department_id,
                   tour_id,
                   id,
                   no,
                   sub_no,
                   sequence,
                   is_last,
                   appointments,
                   aggregates,
                   stations,
                   prev_shipment_dispatch_calculated_unloading_time,
                   prev_shipment_id,
                   prev_shipment_tour_id,
                   prev_shipment_tour_no)
