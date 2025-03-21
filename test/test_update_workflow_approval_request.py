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

from ironclad_python.models.update_workflow_approval_request import UpdateWorkflowApprovalRequest

class TestUpdateWorkflowApprovalRequest(unittest.TestCase):
    """UpdateWorkflowApprovalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWorkflowApprovalRequest:
        """Test UpdateWorkflowApprovalRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWorkflowApprovalRequest`
        """
        model = UpdateWorkflowApprovalRequest()
        if include_optional:
            return UpdateWorkflowApprovalRequest(
                user = openapi_client.models.update_workflow_approval_request_user.update_workflow_approval_request_user(
                    email = 'fett@intergalactic.com', 
                    type = 'email', ),
                status = 'approved'
            )
        else:
            return UpdateWorkflowApprovalRequest(
                user = openapi_client.models.update_workflow_approval_request_user.update_workflow_approval_request_user(
                    email = 'fett@intergalactic.com', 
                    type = 'email', ),
                status = 'approved',
        )
        """

    def testUpdateWorkflowApprovalRequest(self):
        """Test UpdateWorkflowApprovalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
