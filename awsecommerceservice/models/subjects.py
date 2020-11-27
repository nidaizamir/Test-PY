# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Subjects(object):

    """Implementation of the 'Subjects' model.

    TODO: type model description here.

    Attributes:
        subject (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subject":'Subject'
    }

    def __init__(self,
                 subject=None):
        """Constructor for the Subjects class"""

        # Initialize members of the class
        self.subject = subject


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
        subject = dictionary.get('Subject')

        # Return an object of this model
        return cls(subject)


