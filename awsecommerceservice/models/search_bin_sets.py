# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.search_bin_set

class SearchBinSets(object):

    """Implementation of the 'SearchBinSets' model.

    TODO: type model description here.

    Attributes:
        search_bin_set (list of SearchBinSet): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_bin_set":'SearchBinSet'
    }

    def __init__(self,
                 search_bin_set=None):
        """Constructor for the SearchBinSets class"""

        # Initialize members of the class
        self.search_bin_set = search_bin_set


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
        search_bin_set = None
        if dictionary.get('SearchBinSet') != None:
            search_bin_set = list()
            for structure in dictionary.get('SearchBinSet'):
                search_bin_set.append(awsecommerceservice.models.search_bin_set.SearchBinSet.from_dictionary(structure))

        # Return an object of this model
        return cls(search_bin_set)

