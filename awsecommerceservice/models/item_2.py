# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Item2(object):

    """Implementation of the 'Item2' model.

    TODO: type model description here.

    Attributes:
        action (ActionEnum): TODO: type description here.
        cart_item_id (string): TODO: type description here.
        quantity (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action":'Action',
        "cart_item_id":'CartItemId',
        "quantity":'Quantity'
    }

    def __init__(self,
                 action=None,
                 cart_item_id=None,
                 quantity=None):
        """Constructor for the Item2 class"""

        # Initialize members of the class
        self.action = action
        self.cart_item_id = cart_item_id
        self.quantity = quantity


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
        action = dictionary.get('Action')
        cart_item_id = dictionary.get('CartItemId')
        quantity = dictionary.get('Quantity')

        # Return an object of this model
        return cls(action,
                   cart_item_id,
                   quantity)


