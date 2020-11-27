# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.bin_parameter

class Bin(object):

    """Implementation of the 'Bin' model.

    TODO: type model description here.

    Attributes:
        bin_name (string): TODO: type description here.
        bin_item_count (int): TODO: type description here.
        bin_parameter (list of BinParameter): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bin_name":'BinName',
        "bin_item_count":'BinItemCount',
        "bin_parameter":'BinParameter'
    }

    def __init__(self,
                 bin_name=None,
                 bin_item_count=None,
                 bin_parameter=None):
        """Constructor for the Bin class"""

        # Initialize members of the class
        self.bin_name = bin_name
        self.bin_item_count = bin_item_count
        self.bin_parameter = bin_parameter


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
        bin_name = dictionary.get('BinName')
        bin_item_count = dictionary.get('BinItemCount')
        bin_parameter = None
        if dictionary.get('BinParameter') != None:
            bin_parameter = list()
            for structure in dictionary.get('BinParameter'):
                bin_parameter.append(awsecommerceservice.models.bin_parameter.BinParameter.from_dictionary(structure))

        # Return an object of this model
        return cls(bin_name,
                   bin_item_count,
                   bin_parameter)


