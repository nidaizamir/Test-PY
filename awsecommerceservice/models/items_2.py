# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.item_2

class Items2(object):

    """Implementation of the 'Items2' model.

    TODO: type model description here.

    Attributes:
        item (list of Item2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item":'Item'
    }

    def __init__(self,
                 item=None):
        """Constructor for the Items2 class"""

        # Initialize members of the class
        self.item = item


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
        item = None
        if dictionary.get('Item') != None:
            item = list()
            for structure in dictionary.get('Item'):
                item.append(awsecommerceservice.models.item_2.Item2.from_dictionary(structure))

        # Return an object of this model
        return cls(item)

