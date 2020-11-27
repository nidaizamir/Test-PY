# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class VariationDimensions(object):

    """Implementation of the 'VariationDimensions' model.

    TODO: type model description here.

    Attributes:
        variation_dimension (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "variation_dimension":'VariationDimension'
    }

    def __init__(self,
                 variation_dimension=None):
        """Constructor for the VariationDimensions class"""

        # Initialize members of the class
        self.variation_dimension = variation_dimension


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
        variation_dimension = dictionary.get('VariationDimension')

        # Return an object of this model
        return cls(variation_dimension)


