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

from ironclad_python.models.retrieve_asynchronous_workflow_status404_response import RetrieveAsynchronousWorkflowStatus404Response

class TestRetrieveAsynchronousWorkflowStatus404Response(unittest.TestCase):
    """RetrieveAsynchronousWorkflowStatus404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAsynchronousWorkflowStatus404Response:
        """Test RetrieveAsynchronousWorkflowStatus404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAsynchronousWorkflowStatus404Response`
        """
        model = RetrieveAsynchronousWorkflowStatus404Response()
        if include_optional:
            return RetrieveAsynchronousWorkflowStatus404Response(
                code = 'NOT_FOUND',
                message = 'not found',
                param = 'parameter identifier'
            )
        else:
            return RetrieveAsynchronousWorkflowStatus404Response(
        )
        """

    def testRetrieveAsynchronousWorkflowStatus404Response(self):
        """Test RetrieveAsynchronousWorkflowStatus404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
