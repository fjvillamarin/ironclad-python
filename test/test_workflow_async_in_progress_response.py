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

from ironclad_python.models.workflow_async_in_progress_response import WorkflowAsyncInProgressResponse

class TestWorkflowAsyncInProgressResponse(unittest.TestCase):
    """WorkflowAsyncInProgressResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowAsyncInProgressResponse:
        """Test WorkflowAsyncInProgressResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowAsyncInProgressResponse`
        """
        model = WorkflowAsyncInProgressResponse()
        if include_optional:
            return WorkflowAsyncInProgressResponse(
                status = 'in_progress',
                request_payload = openapi_client.models.workflow_request_model.WorkflowRequestModel(
                    template = '600b296c3e15a234ab88f884', 
                    creator = openapi_client.models.creator_email_model.CreatorEmailModel(
                        type = 'email', 
                        email = 'example@example.com', ), 
                    attributes = openapi_client.models.attributes_model.AttributesModel(
                        counterparty_name = 'Example Company', 
                        draft = [
                            openapi_client.models.attributes_model_draft_inner.AttributesModel_draft_inner(
                                url = 'https://www.law.berkeley.edu/wp-content/uploads/2018/12/Resume-Samples-1.pdf', )
                            ], 
                        paper_source = 'Counterparty paper', ), )
            )
        else:
            return WorkflowAsyncInProgressResponse(
                status = 'in_progress',
                request_payload = openapi_client.models.workflow_request_model.WorkflowRequestModel(
                    template = '600b296c3e15a234ab88f884', 
                    creator = openapi_client.models.creator_email_model.CreatorEmailModel(
                        type = 'email', 
                        email = 'example@example.com', ), 
                    attributes = openapi_client.models.attributes_model.AttributesModel(
                        counterparty_name = 'Example Company', 
                        draft = [
                            openapi_client.models.attributes_model_draft_inner.AttributesModel_draft_inner(
                                url = 'https://www.law.berkeley.edu/wp-content/uploads/2018/12/Resume-Samples-1.pdf', )
                            ], 
                        paper_source = 'Counterparty paper', ), ),
        )
        """

    def testWorkflowAsyncInProgressResponse(self):
        """Test WorkflowAsyncInProgressResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
