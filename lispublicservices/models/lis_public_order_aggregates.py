# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicOrderAggregates(object):

    """Implementation of the 'LISPublicOrderAggregates' model.

    The LIS Order aggregates.

    Attributes:
        weight (float): Gets or sets the weight.
        chargeable_weight (float): Gets or sets the chargeable weight.
        cubic_decimeter (float): Gets or sets the cubic decimeter.
        loading_meter (float): Gets or sets the loading meter.
        square_meter (float): Gets or sets the square meter.
        storage_places (float): Gets or sets the storage places.
        given_weight (float): Gets or sets the given weight.
        palletts (float): Gets or sets the palletts.
        packages (float): Gets or sets the packages.
        pieces (float): Gets or sets the pieces.
        shipping_units (float): Gets or sets the shipping units.
        dangerous_goods (bool): Gets or sets a value indicating whether
            [dangerous goods].
        reefer_cargo (bool): Gets or sets a value indicating whether [reefer
            cargo].
        declared_value (float): Gets or sets the declared value.
        calculated_amount (float): Gets or sets the calculated amount.
        orders (int): Gets or sets the orders.
        given_packages (float): Gets or sets the given packages.
        ecological_menace (EcologicalMenace1Enum): Gets or sets the ecological
            menace.
        tunnel_category (TunnelCategoryEnum): Gets or sets the tunnel
            category.
        is_explosiv (bool): Gets or sets a value indicating whether this
            instance is explosiv.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "weight": 'weight',
        "chargeable_weight": 'chargeableWeight',
        "cubic_decimeter": 'cubicDecimeter',
        "loading_meter": 'loadingMeter',
        "square_meter": 'squareMeter',
        "storage_places": 'storagePlaces',
        "given_weight": 'givenWeight',
        "palletts": 'palletts',
        "packages": 'packages',
        "pieces": 'pieces',
        "shipping_units": 'shippingUnits',
        "dangerous_goods": 'dangerousGoods',
        "reefer_cargo": 'reeferCargo',
        "declared_value": 'declaredValue',
        "calculated_amount": 'calculatedAmount',
        "orders": 'orders',
        "given_packages": 'givenPackages',
        "ecological_menace": 'ecologicalMenace',
        "tunnel_category": 'tunnelCategory',
        "is_explosiv": 'isExplosiv'
    }

    _optionals = [
        'weight',
        'chargeable_weight',
        'cubic_decimeter',
        'loading_meter',
        'square_meter',
        'storage_places',
        'given_weight',
        'palletts',
        'packages',
        'pieces',
        'shipping_units',
        'dangerous_goods',
        'reefer_cargo',
        'declared_value',
        'calculated_amount',
        'orders',
        'given_packages',
        'ecological_menace',
        'tunnel_category',
        'is_explosiv',
    ]

    def __init__(self,
                 weight=APIHelper.SKIP,
                 chargeable_weight=APIHelper.SKIP,
                 cubic_decimeter=APIHelper.SKIP,
                 loading_meter=APIHelper.SKIP,
                 square_meter=APIHelper.SKIP,
                 storage_places=APIHelper.SKIP,
                 given_weight=APIHelper.SKIP,
                 palletts=APIHelper.SKIP,
                 packages=APIHelper.SKIP,
                 pieces=APIHelper.SKIP,
                 shipping_units=APIHelper.SKIP,
                 dangerous_goods=APIHelper.SKIP,
                 reefer_cargo=APIHelper.SKIP,
                 declared_value=APIHelper.SKIP,
                 calculated_amount=APIHelper.SKIP,
                 orders=APIHelper.SKIP,
                 given_packages=APIHelper.SKIP,
                 ecological_menace=APIHelper.SKIP,
                 tunnel_category=APIHelper.SKIP,
                 is_explosiv=APIHelper.SKIP):
        """Constructor for the LISPublicOrderAggregates class"""

        # Initialize members of the class
        if weight is not APIHelper.SKIP:
            self.weight = weight 
        if chargeable_weight is not APIHelper.SKIP:
            self.chargeable_weight = chargeable_weight 
        if cubic_decimeter is not APIHelper.SKIP:
            self.cubic_decimeter = cubic_decimeter 
        if loading_meter is not APIHelper.SKIP:
            self.loading_meter = loading_meter 
        if square_meter is not APIHelper.SKIP:
            self.square_meter = square_meter 
        if storage_places is not APIHelper.SKIP:
            self.storage_places = storage_places 
        if given_weight is not APIHelper.SKIP:
            self.given_weight = given_weight 
        if palletts is not APIHelper.SKIP:
            self.palletts = palletts 
        if packages is not APIHelper.SKIP:
            self.packages = packages 
        if pieces is not APIHelper.SKIP:
            self.pieces = pieces 
        if shipping_units is not APIHelper.SKIP:
            self.shipping_units = shipping_units 
        if dangerous_goods is not APIHelper.SKIP:
            self.dangerous_goods = dangerous_goods 
        if reefer_cargo is not APIHelper.SKIP:
            self.reefer_cargo = reefer_cargo 
        if declared_value is not APIHelper.SKIP:
            self.declared_value = declared_value 
        if calculated_amount is not APIHelper.SKIP:
            self.calculated_amount = calculated_amount 
        if orders is not APIHelper.SKIP:
            self.orders = orders 
        if given_packages is not APIHelper.SKIP:
            self.given_packages = given_packages 
        if ecological_menace is not APIHelper.SKIP:
            self.ecological_menace = ecological_menace 
        if tunnel_category is not APIHelper.SKIP:
            self.tunnel_category = tunnel_category 
        if is_explosiv is not APIHelper.SKIP:
            self.is_explosiv = is_explosiv 

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

        weight = dictionary.get("weight") if dictionary.get("weight") else APIHelper.SKIP
        chargeable_weight = dictionary.get("chargeableWeight") if dictionary.get("chargeableWeight") else APIHelper.SKIP
        cubic_decimeter = dictionary.get("cubicDecimeter") if dictionary.get("cubicDecimeter") else APIHelper.SKIP
        loading_meter = dictionary.get("loadingMeter") if dictionary.get("loadingMeter") else APIHelper.SKIP
        square_meter = dictionary.get("squareMeter") if dictionary.get("squareMeter") else APIHelper.SKIP
        storage_places = dictionary.get("storagePlaces") if dictionary.get("storagePlaces") else APIHelper.SKIP
        given_weight = dictionary.get("givenWeight") if dictionary.get("givenWeight") else APIHelper.SKIP
        palletts = dictionary.get("palletts") if dictionary.get("palletts") else APIHelper.SKIP
        packages = dictionary.get("packages") if dictionary.get("packages") else APIHelper.SKIP
        pieces = dictionary.get("pieces") if dictionary.get("pieces") else APIHelper.SKIP
        shipping_units = dictionary.get("shippingUnits") if dictionary.get("shippingUnits") else APIHelper.SKIP
        dangerous_goods = dictionary.get("dangerousGoods") if "dangerousGoods" in dictionary.keys() else APIHelper.SKIP
        reefer_cargo = dictionary.get("reeferCargo") if "reeferCargo" in dictionary.keys() else APIHelper.SKIP
        declared_value = dictionary.get("declaredValue") if dictionary.get("declaredValue") else APIHelper.SKIP
        calculated_amount = dictionary.get("calculatedAmount") if dictionary.get("calculatedAmount") else APIHelper.SKIP
        orders = dictionary.get("orders") if dictionary.get("orders") else APIHelper.SKIP
        given_packages = dictionary.get("givenPackages") if dictionary.get("givenPackages") else APIHelper.SKIP
        ecological_menace = dictionary.get("ecologicalMenace") if dictionary.get("ecologicalMenace") else APIHelper.SKIP
        tunnel_category = dictionary.get("tunnelCategory") if dictionary.get("tunnelCategory") else APIHelper.SKIP
        is_explosiv = dictionary.get("isExplosiv") if "isExplosiv" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(weight,
                   chargeable_weight,
                   cubic_decimeter,
                   loading_meter,
                   square_meter,
                   storage_places,
                   given_weight,
                   palletts,
                   packages,
                   pieces,
                   shipping_units,
                   dangerous_goods,
                   reefer_cargo,
                   declared_value,
                   calculated_amount,
                   orders,
                   given_packages,
                   ecological_menace,
                   tunnel_category,
                   is_explosiv)
