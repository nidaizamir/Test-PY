# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.item_search

class ItemSearchRequestMsg(object):

    """Implementation of the 'ItemSearchRequestMsg' model.

    TODO: type model description here.

    Attributes:
        body (ItemSearch): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body":'body'
    }

    def __init__(self,
                 body=None):
        """Constructor for the ItemSearchRequestMsg class"""

        # Initialize members of the class
        self.body = body


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
        body = awsecommerceservice.models.item_search.ItemSearch.from_dictionary(dictionary.get('body')) if dictionary.get('body') else None

        # Return an object of this model
        return cls(body)


