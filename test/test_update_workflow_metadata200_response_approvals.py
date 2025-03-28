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

from ironclad_python.models.update_workflow_metadata200_response_approvals import UpdateWorkflowMetadata200ResponseApprovals

class TestUpdateWorkflowMetadata200ResponseApprovals(unittest.TestCase):
    """UpdateWorkflowMetadata200ResponseApprovals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWorkflowMetadata200ResponseApprovals:
        """Test UpdateWorkflowMetadata200ResponseApprovals
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWorkflowMetadata200ResponseApprovals`
        """
        model = UpdateWorkflowMetadata200ResponseApprovals()
        if include_optional:
            return UpdateWorkflowMetadata200ResponseApprovals(
                state = 'in_progess',
                url = 'https://ironcladapp.com/public/api/v1/workflows/22e2ff72-56a1-4711-a4ca-41328d311e9f/approvals'
            )
        else:
            return UpdateWorkflowMetadata200ResponseApprovals(
        )
        """

    def testUpdateWorkflowMetadata200ResponseApprovals(self):
        """Test UpdateWorkflowMetadata200ResponseApprovals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
