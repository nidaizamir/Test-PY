# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Price(object):

    """Implementation of the 'Price' model.

    TODO: type model description here.

    Attributes:
        amount (int): TODO: type description here.
        currency_code (string): TODO: type description here.
        formatted_price (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "formatted_price":'FormattedPrice',
        "amount":'Amount',
        "currency_code":'CurrencyCode'
    }

    def __init__(self,
                 formatted_price=None,
                 amount=None,
                 currency_code=None):
        """Constructor for the Price class"""

        # Initialize members of the class
        self.amount = amount
        self.currency_code = currency_code
        self.formatted_price = formatted_price


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
        formatted_price = dictionary.get('FormattedPrice')
        amount = dictionary.get('Amount')
        currency_code = dictionary.get('CurrencyCode')

        # Return an object of this model
        return cls(formatted_price,
                   amount,
                   currency_code)


