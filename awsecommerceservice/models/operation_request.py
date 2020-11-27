# -*- coding: utf-8 -*-

"""
    awsecommerceservice

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import awsecommerceservice.models.http_headers
import awsecommerceservice.models.arguments
import awsecommerceservice.models.errors

class OperationRequest(object):

    """Implementation of the 'OperationRequest' model.

    TODO: type model description here.

    Attributes:
        http_headers (HTTPHeaders): TODO: type description here.
        request_id (string): TODO: type description here.
        arguments (Arguments): TODO: type description here.
        errors (Errors): TODO: type description here.
        request_processing_time (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "http_headers":'HTTPHeaders',
        "request_id":'RequestId',
        "arguments":'Arguments',
        "errors":'Errors',
        "request_processing_time":'RequestProcessingTime'
    }

    def __init__(self,
                 http_headers=None,
                 request_id=None,
                 arguments=None,
                 errors=None,
                 request_processing_time=None):
        """Constructor for the OperationRequest class"""

        # Initialize members of the class
        self.http_headers = http_headers
        self.request_id = request_id
        self.arguments = arguments
        self.errors = errors
        self.request_processing_time = request_processing_time


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
        http_headers = awsecommerceservice.models.http_headers.HTTPHeaders.from_dictionary(dictionary.get('HTTPHeaders')) if dictionary.get('HTTPHeaders') else None
        request_id = dictionary.get('RequestId')
        arguments = awsecommerceservice.models.arguments.Arguments.from_dictionary(dictionary.get('Arguments')) if dictionary.get('Arguments') else None
        errors = awsecommerceservice.models.errors.Errors.from_dictionary(dictionary.get('Errors')) if dictionary.get('Errors') else None
        request_processing_time = dictionary.get('RequestProcessingTime')

        # Return an object of this model
        return cls(http_headers,
                   request_id,
                   arguments,
                   errors,
                   request_processing_time)


