# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ItemLookupRequest(object):

    """Implementation of the 'ItemLookupRequest' model.

    TODO: type model description here.

    Attributes:
        condition (ConditionEnum): TODO: type description here.
        id_type (IdTypeEnum): TODO: type description here.
        merchant_id (string): TODO: type description here.
        item_id (list of string): TODO: type description here.
        response_group (list of string): TODO: type description here.
        search_index (string): TODO: type description here.
        variation_page (object): TODO: type description here.
        related_item_page (object): TODO: type description here.
        relationship_type (list of string): TODO: type description here.
        include_reviews_summary (string): TODO: type description here.
        truncate_reviews_at (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "condition":'Condition',
        "id_type":'IdType',
        "merchant_id":'MerchantId',
        "item_id":'ItemId',
        "response_group":'ResponseGroup',
        "search_index":'SearchIndex',
        "variation_page":'VariationPage',
        "related_item_page":'RelatedItemPage',
        "relationship_type":'RelationshipType',
        "include_reviews_summary":'IncludeReviewsSummary',
        "truncate_reviews_at":'TruncateReviewsAt'
    }

    def __init__(self,
                 condition=None,
                 id_type=None,
                 merchant_id=None,
                 item_id=None,
                 response_group=None,
                 search_index=None,
                 variation_page=None,
                 related_item_page=None,
                 relationship_type=None,
                 include_reviews_summary=None,
                 truncate_reviews_at=None):
        """Constructor for the ItemLookupRequest class"""

        # Initialize members of the class
        self.condition = condition
        self.id_type = id_type
        self.merchant_id = merchant_id
        self.item_id = item_id
        self.response_group = response_group
        self.search_index = search_index
        self.variation_page = variation_page
        self.related_item_page = related_item_page
        self.relationship_type = relationship_type
        self.include_reviews_summary = include_reviews_summary
        self.truncate_reviews_at = truncate_reviews_at


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
        condition = dictionary.get('Condition')
        id_type = dictionary.get('IdType')
        merchant_id = dictionary.get('MerchantId')
        item_id = dictionary.get('ItemId')
        response_group = dictionary.get('ResponseGroup')
        search_index = dictionary.get('SearchIndex')
        variation_page = dictionary.get('VariationPage')
        related_item_page = dictionary.get('RelatedItemPage')
        relationship_type = dictionary.get('RelationshipType')
        include_reviews_summary = dictionary.get('IncludeReviewsSummary')
        truncate_reviews_at = dictionary.get('TruncateReviewsAt')

        # Return an object of this model
        return cls(condition,
                   id_type,
                   merchant_id,
                   item_id,
                   response_group,
                   search_index,
                   variation_page,
                   related_item_page,
                   relationship_type,
                   include_reviews_summary,
                   truncate_reviews_at)


