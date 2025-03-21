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

from ironclad_python.models.list_all_workflow_approvals200_response_approval_groups_inner import ListAllWorkflowApprovals200ResponseApprovalGroupsInner

class TestListAllWorkflowApprovals200ResponseApprovalGroupsInner(unittest.TestCase):
    """ListAllWorkflowApprovals200ResponseApprovalGroupsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllWorkflowApprovals200ResponseApprovalGroupsInner:
        """Test ListAllWorkflowApprovals200ResponseApprovalGroupsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllWorkflowApprovals200ResponseApprovalGroupsInner`
        """
        model = ListAllWorkflowApprovals200ResponseApprovalGroupsInner()
        if include_optional:
            return ListAllWorkflowApprovals200ResponseApprovalGroupsInner(
                reviewers = [
                    openapi_client.models.list_all_workflow_approvals_200_response_approval_groups_inner_reviewers_inner.list_all_workflow_approvals_200_response_approvalGroups_inner_reviewers_inner(
                        role = 'finance', 
                        display_name = 'Finance', 
                        reviewer_type = 'role', 
                        status = 'pending', )
                    ]
            )
        else:
            return ListAllWorkflowApprovals200ResponseApprovalGroupsInner(
        )
        """

    def testListAllWorkflowApprovals200ResponseApprovalGroupsInner(self):
        """Test ListAllWorkflowApprovals200ResponseApprovalGroupsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
