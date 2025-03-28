# coding: utf-8

"""
    Ironclad Public API

    Documentation for Ironclad's REST API.

    The version of the OpenAPI document: 1
    Contact: support@ironcladapp.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ironclad_python.models.retrieve_import_predictions400_response import RetrieveImportPredictions400Response

class TestRetrieveImportPredictions400Response(unittest.TestCase):
    """RetrieveImportPredictions400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveImportPredictions400Response:
        """Test RetrieveImportPredictions400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveImportPredictions400Response`
        """
        model = RetrieveImportPredictions400Response()
        if include_optional:
            return RetrieveImportPredictions400Response(
                code = '',
                message = ''
            )
        else:
            return RetrieveImportPredictions400Response(
        )
        """

    def testRetrieveImportPredictions400Response(self):
        """Test RetrieveImportPredictions400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
