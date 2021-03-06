# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.corrected_query

class SearchIndex(object):

    """Implementation of the 'SearchIndex' model.

    TODO: type model description here.

    Attributes:
        index_name (string): TODO: type description here.
        results (int): TODO: type description here.
        pages (int): TODO: type description here.
        corrected_query (CorrectedQuery): TODO: type description here.
        relevance_rank (int): TODO: type description here.
        asin (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "index_name":'IndexName',
        "relevance_rank":'RelevanceRank',
        "asin":'ASIN',
        "results":'Results',
        "pages":'Pages',
        "corrected_query":'CorrectedQuery'
    }

    def __init__(self,
                 index_name=None,
                 relevance_rank=None,
                 asin=None,
                 results=None,
                 pages=None,
                 corrected_query=None):
        """Constructor for the SearchIndex class"""

        # Initialize members of the class
        self.index_name = index_name
        self.results = results
        self.pages = pages
        self.corrected_query = corrected_query
        self.relevance_rank = relevance_rank
        self.asin = asin


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
        index_name = dictionary.get('IndexName')
        relevance_rank = dictionary.get('RelevanceRank')
        asin = dictionary.get('ASIN')
        results = dictionary.get('Results')
        pages = dictionary.get('Pages')
        corrected_query = awsecommerceservice.models.corrected_query.CorrectedQuery.from_dictionary(dictionary.get('CorrectedQuery')) if dictionary.get('CorrectedQuery') else None

        # Return an object of this model
        return cls(index_name,
                   relevance_rank,
                   asin,
                   results,
                   pages,
                   corrected_query)


