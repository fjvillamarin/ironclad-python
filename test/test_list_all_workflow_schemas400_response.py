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

from ironclad_python.models.list_all_workflow_schemas400_response import ListAllWorkflowSchemas400Response

class TestListAllWorkflowSchemas400Response(unittest.TestCase):
    """ListAllWorkflowSchemas400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllWorkflowSchemas400Response:
        """Test ListAllWorkflowSchemas400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllWorkflowSchemas400Response`
        """
        model = ListAllWorkflowSchemas400Response()
        if include_optional:
            return ListAllWorkflowSchemas400Response(
                code = 'MISSING_PARAM',
                message = 'reason why something has gone wrong',
                param = 'parameter identifier'
            )
        else:
            return ListAllWorkflowSchemas400Response(
        )
        """

    def testListAllWorkflowSchemas400Response(self):
        """Test ListAllWorkflowSchemas400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
