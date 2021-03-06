# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.alternate_version

class AlternateVersions(object):

    """Implementation of the 'AlternateVersions' model.

    TODO: type model description here.

    Attributes:
        alternate_version (list of AlternateVersion): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alternate_version":'AlternateVersion'
    }

    def __init__(self,
                 alternate_version=None):
        """Constructor for the AlternateVersions class"""

        # Initialize members of the class
        self.alternate_version = alternate_version


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
        alternate_version = None
        if dictionary.get('AlternateVersion') != None:
            alternate_version = list()
            for structure in dictionary.get('AlternateVersion'):
                alternate_version.append(awsecommerceservice.models.alternate_version.AlternateVersion.from_dictionary(structure))

        # Return an object of this model
        return cls(alternate_version)


