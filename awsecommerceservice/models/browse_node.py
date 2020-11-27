# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.properties
import awsecommerceservice.models.children
import awsecommerceservice.models.ancestors
import awsecommerceservice.models.top_sellers
import awsecommerceservice.models.new_releases
import awsecommerceservice.models.top_item_set

class BrowseNode(object):

    """Implementation of the 'BrowseNode' model.

    TODO: type model description here.

    Attributes:
        browse_node_id (string): TODO: type description here.
        name (string): TODO: type description here.
        is_category_root (bool): TODO: type description here.
        properties (Properties): TODO: type description here.
        children (Children): TODO: type description here.
        ancestors (Ancestors): TODO: type description here.
        top_sellers (TopSellers): TODO: type description here.
        new_releases (NewReleases): TODO: type description here.
        top_item_set (list of TopItemSet): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "browse_node_id":'BrowseNodeId',
        "name":'Name',
        "is_category_root":'IsCategoryRoot',
        "properties":'Properties',
        "children":'Children',
        "ancestors":'Ancestors',
        "top_sellers":'TopSellers',
        "new_releases":'NewReleases',
        "top_item_set":'TopItemSet'
    }

    def __init__(self,
                 browse_node_id=None,
                 name=None,
                 is_category_root=None,
                 properties=None,
                 children=None,
                 ancestors=None,
                 top_sellers=None,
                 new_releases=None,
                 top_item_set=None):
        """Constructor for the BrowseNode class"""

        # Initialize members of the class
        self.browse_node_id = browse_node_id
        self.name = name
        self.is_category_root = is_category_root
        self.properties = properties
        self.children = children
        self.ancestors = ancestors
        self.top_sellers = top_sellers
        self.new_releases = new_releases
        self.top_item_set = top_item_set


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
        browse_node_id = dictionary.get('BrowseNodeId')
        name = dictionary.get('Name')
        is_category_root = dictionary.get('IsCategoryRoot')
        properties = awsecommerceservice.models.properties.Properties.from_dictionary(dictionary.get('Properties')) if dictionary.get('Properties') else None
        children = awsecommerceservice.models.children.Children.from_dictionary(dictionary.get('Children')) if dictionary.get('Children') else None
        ancestors = awsecommerceservice.models.ancestors.Ancestors.from_dictionary(dictionary.get('Ancestors')) if dictionary.get('Ancestors') else None
        top_sellers = awsecommerceservice.models.top_sellers.TopSellers.from_dictionary(dictionary.get('TopSellers')) if dictionary.get('TopSellers') else None
        new_releases = awsecommerceservice.models.new_releases.NewReleases.from_dictionary(dictionary.get('NewReleases')) if dictionary.get('NewReleases') else None
        top_item_set = None
        if dictionary.get('TopItemSet') != None:
            top_item_set = list()
            for structure in dictionary.get('TopItemSet'):
                top_item_set.append(awsecommerceservice.models.top_item_set.TopItemSet.from_dictionary(structure))

        # Return an object of this model
        return cls(browse_node_id,
                   name,
                   is_category_root,
                   properties,
                   children,
                   ancestors,
                   top_sellers,
                   new_releases,
                   top_item_set)

