# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.price

class OfferSummary(object):

    """Implementation of the 'OfferSummary' model.

    TODO: type model description here.

    Attributes:
        lowest_new_price (Price): TODO: type description here.
        lowest_used_price (Price): TODO: type description here.
        lowest_collectible_price (Price): TODO: type description here.
        lowest_refurbished_price (Price): TODO: type description here.
        total_new (string): TODO: type description here.
        total_used (string): TODO: type description here.
        total_collectible (string): TODO: type description here.
        total_refurbished (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lowest_new_price":'LowestNewPrice',
        "lowest_used_price":'LowestUsedPrice',
        "lowest_collectible_price":'LowestCollectiblePrice',
        "lowest_refurbished_price":'LowestRefurbishedPrice',
        "total_new":'TotalNew',
        "total_used":'TotalUsed',
        "total_collectible":'TotalCollectible',
        "total_refurbished":'TotalRefurbished'
    }

    def __init__(self,
                 lowest_new_price=None,
                 lowest_used_price=None,
                 lowest_collectible_price=None,
                 lowest_refurbished_price=None,
                 total_new=None,
                 total_used=None,
                 total_collectible=None,
                 total_refurbished=None):
        """Constructor for the OfferSummary class"""

        # Initialize members of the class
        self.lowest_new_price = lowest_new_price
        self.lowest_used_price = lowest_used_price
        self.lowest_collectible_price = lowest_collectible_price
        self.lowest_refurbished_price = lowest_refurbished_price
        self.total_new = total_new
        self.total_used = total_used
        self.total_collectible = total_collectible
        self.total_refurbished = total_refurbished


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        lowest_new_price = awsecommerceservice.models.price.Price.from_dictionary(dictionary.get('LowestNewPrice')) if dictionary.get('LowestNewPrice') else None
        lowest_used_price = awsecommerceservice.models.price.Price.from_dictionary(dictionary.get('LowestUsedPrice')) if dictionary.get('LowestUsedPrice') else None
        lowest_collectible_price = awsecommerceservice.models.price.Price.from_dictionary(dictionary.get('LowestCollectiblePrice')) if dictionary.get('LowestCollectiblePrice') else None
        lowest_refurbished_price = awsecommerceservice.models.price.Price.from_dictionary(dictionary.get('LowestRefurbishedPrice')) if dictionary.get('LowestRefurbishedPrice') else None
        total_new = dictionary.get('TotalNew')
        total_used = dictionary.get('TotalUsed')
        total_collectible = dictionary.get('TotalCollectible')
        total_refurbished = dictionary.get('TotalRefurbished')

        # Return an object of this model
        return cls(lowest_new_price,
                   lowest_used_price,
                   lowest_collectible_price,
                   lowest_refurbished_price,
                   total_new,
                   total_used,
                   total_collectible,
                   total_refurbished)

