# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicTourRouteInfo(object):

    """Implementation of the 'LISPublicTourRouteInfo' model.

    The public common route info

    Attributes:
        distance (float): Gets or sets the distance.
        distance_empty (float): Gets or sets the distance empty.
        distance_toll (float): Gets or sets the distance toll.
        distance_toll_empty (float): Gets or sets the distance toll empty.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "distance": 'distance',
        "distance_empty": 'distanceEmpty',
        "distance_toll": 'distanceToll',
        "distance_toll_empty": 'distanceTollEmpty'
    }

    _optionals = [
        'distance',
        'distance_empty',
        'distance_toll',
        'distance_toll_empty',
    ]

    def __init__(self,
                 distance=APIHelper.SKIP,
                 distance_empty=APIHelper.SKIP,
                 distance_toll=APIHelper.SKIP,
                 distance_toll_empty=APIHelper.SKIP):
        """Constructor for the LISPublicTourRouteInfo class"""

        # Initialize members of the class
        if distance is not APIHelper.SKIP:
            self.distance = distance 
        if distance_empty is not APIHelper.SKIP:
            self.distance_empty = distance_empty 
        if distance_toll is not APIHelper.SKIP:
            self.distance_toll = distance_toll 
        if distance_toll_empty is not APIHelper.SKIP:
            self.distance_toll_empty = distance_toll_empty 

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

        distance = dictionary.get("distance") if dictionary.get("distance") else APIHelper.SKIP
        distance_empty = dictionary.get("distanceEmpty") if dictionary.get("distanceEmpty") else APIHelper.SKIP
        distance_toll = dictionary.get("distanceToll") if dictionary.get("distanceToll") else APIHelper.SKIP
        distance_toll_empty = dictionary.get("distanceTollEmpty") if dictionary.get("distanceTollEmpty") else APIHelper.SKIP
        # Return an object of this model
        return cls(distance,
                   distance_empty,
                   distance_toll,
                   distance_toll_empty)
