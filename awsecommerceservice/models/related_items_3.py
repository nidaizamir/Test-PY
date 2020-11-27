# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.related_item_4

class RelatedItems3(object):

    """Implementation of the 'RelatedItems3' model.

    TODO: type model description here.

    Attributes:
        relationship (RelationshipEnum): TODO: type description here.
        relationship_type (string): TODO: type description here.
        related_item_count (int): TODO: type description here.
        related_item_page_count (int): TODO: type description here.
        related_item_page (int): TODO: type description here.
        related_item (list of RelatedItem4): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "relationship":'Relationship',
        "relationship_type":'RelationshipType',
        "related_item_count":'RelatedItemCount',
        "related_item_page_count":'RelatedItemPageCount',
        "related_item_page":'RelatedItemPage',
        "related_item":'RelatedItem'
    }

    def __init__(self,
                 relationship=None,
                 relationship_type=None,
                 related_item_count=None,
                 related_item_page_count=None,
                 related_item_page=None,
                 related_item=None):
        """Constructor for the RelatedItems3 class"""

        # Initialize members of the class
        self.relationship = relationship
        self.relationship_type = relationship_type
        self.related_item_count = related_item_count
        self.related_item_page_count = related_item_page_count
        self.related_item_page = related_item_page
        self.related_item = related_item


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
        relationship = dictionary.get('Relationship')
        relationship_type = dictionary.get('RelationshipType')
        related_item_count = dictionary.get('RelatedItemCount')
        related_item_page_count = dictionary.get('RelatedItemPageCount')
        related_item_page = dictionary.get('RelatedItemPage')
        related_item = None
        if dictionary.get('RelatedItem') != None:
            related_item = list()
            for structure in dictionary.get('RelatedItem'):
                related_item.append(awsecommerceservice.models.related_item_4.RelatedItem4.from_dictionary(structure))

        # Return an object of this model
        return cls(relationship,
                   relationship_type,
                   related_item_count,
                   related_item_page_count,
                   related_item_page,
                   related_item)


