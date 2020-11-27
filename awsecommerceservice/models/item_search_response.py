# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.operation_request
import awsecommerceservice.models.items

class ItemSearchResponse(object):

    """Implementation of the 'ItemSearchResponse' model.

    TODO: type model description here.

    Attributes:
        operation_request (OperationRequest): TODO: type description here.
        items (list of Items): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "operation_request":'OperationRequest',
        "items":'Items'
    }

    def __init__(self,
                 operation_request=None,
                 items=None):
        """Constructor for the ItemSearchResponse class"""

        # Initialize members of the class
        self.operation_request = operation_request
        self.items = items


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
        operation_request = awsecommerceservice.models.operation_request.OperationRequest.from_dictionary(dictionary.get('OperationRequest')) if dictionary.get('OperationRequest') else None
        items = None
        if dictionary.get('Items') != None:
            items = list()
            for structure in dictionary.get('Items'):
                items.append(awsecommerceservice.models.items.Items.from_dictionary(structure))

        # Return an object of this model
        return cls(operation_request,
                   items)


