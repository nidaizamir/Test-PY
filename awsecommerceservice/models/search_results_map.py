# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.search_index

class SearchResultsMap(object):

    """Implementation of the 'SearchResultsMap' model.

    TODO: type model description here.

    Attributes:
        search_index (list of SearchIndex): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_index":'SearchIndex'
    }

    def __init__(self,
                 search_index=None):
        """Constructor for the SearchResultsMap class"""

        # Initialize members of the class
        self.search_index = search_index


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
        search_index = None
        if dictionary.get('SearchIndex') != None:
            search_index = list()
            for structure in dictionary.get('SearchIndex'):
                search_index.append(awsecommerceservice.models.search_index.SearchIndex.from_dictionary(structure))

        # Return an object of this model
        return cls(search_index)


