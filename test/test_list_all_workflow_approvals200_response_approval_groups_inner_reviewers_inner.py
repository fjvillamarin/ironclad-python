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

from ironclad_python.models.list_all_workflow_approvals200_response_approval_groups_inner_reviewers_inner import ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner

class TestListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner(unittest.TestCase):
    """ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner:
        """Test ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner`
        """
        model = ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner()
        if include_optional:
            return ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner(
                role = 'finance',
                display_name = 'Finance',
                reviewer_type = 'role',
                status = 'pending'
            )
        else:
            return ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner(
        )
        """

    def testListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner(self):
        """Test ListAllWorkflowApprovals200ResponseApprovalGroupsInnerReviewersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
