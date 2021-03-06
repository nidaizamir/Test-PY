# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.merchant
import awsecommerceservice.models.offer_attributes
import awsecommerceservice.models.offer_listing
import awsecommerceservice.models.loyalty_points
import awsecommerceservice.models.promotions

class Offer(object):

    """Implementation of the 'Offer' model.

    TODO: type model description here.

    Attributes:
        merchant (Merchant): TODO: type description here.
        offer_attributes (OfferAttributes): TODO: type description here.
        offer_listing (list of OfferListing): TODO: type description here.
        loyalty_points (LoyaltyPoints): TODO: type description here.
        promotions (Promotions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "merchant":'Merchant',
        "offer_attributes":'OfferAttributes',
        "offer_listing":'OfferListing',
        "loyalty_points":'LoyaltyPoints',
        "promotions":'Promotions'
    }

    def __init__(self,
                 merchant=None,
                 offer_attributes=None,
                 offer_listing=None,
                 loyalty_points=None,
                 promotions=None):
        """Constructor for the Offer class"""

        # Initialize members of the class
        self.merchant = merchant
        self.offer_attributes = offer_attributes
        self.offer_listing = offer_listing
        self.loyalty_points = loyalty_points
        self.promotions = promotions


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
        merchant = awsecommerceservice.models.merchant.Merchant.from_dictionary(dictionary.get('Merchant')) if dictionary.get('Merchant') else None
        offer_attributes = awsecommerceservice.models.offer_attributes.OfferAttributes.from_dictionary(dictionary.get('OfferAttributes')) if dictionary.get('OfferAttributes') else None
        offer_listing = None
        if dictionary.get('OfferListing') != None:
            offer_listing = list()
            for structure in dictionary.get('OfferListing'):
                offer_listing.append(awsecommerceservice.models.offer_listing.OfferListing.from_dictionary(structure))
        loyalty_points = awsecommerceservice.models.loyalty_points.LoyaltyPoints.from_dictionary(dictionary.get('LoyaltyPoints')) if dictionary.get('LoyaltyPoints') else None
        promotions = awsecommerceservice.models.promotions.Promotions.from_dictionary(dictionary.get('Promotions')) if dictionary.get('Promotions') else None

        # Return an object of this model
        return cls(merchant,
                   offer_attributes,
                   offer_listing,
                   loyalty_points,
                   promotions)


