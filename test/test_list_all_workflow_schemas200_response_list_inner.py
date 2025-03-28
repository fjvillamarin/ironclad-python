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

from ironclad_python.models.list_all_workflow_schemas200_response_list_inner import ListAllWorkflowSchemas200ResponseListInner

class TestListAllWorkflowSchemas200ResponseListInner(unittest.TestCase):
    """ListAllWorkflowSchemas200ResponseListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllWorkflowSchemas200ResponseListInner:
        """Test ListAllWorkflowSchemas200ResponseListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllWorkflowSchemas200ResponseListInner`
        """
        model = ListAllWorkflowSchemas200ResponseListInner()
        if include_optional:
            return ListAllWorkflowSchemas200ResponseListInner(
                id = 'a1b2c3d4',
                name = 'MNDA',
                var_schema = openapi_client.models.update_workflow_metadata_200_response_schema.update_workflow_metadata_200_response_schema(
                    counterparty_name = openapi_client.models.update_workflow_metadata_200_response_schema_counterparty_name.update_workflow_metadata_200_response_schema_counterpartyName(
                        type = 'string', 
                        display_name = 'Example String Attribute', ), 
                    amount = openapi_client.models.update_workflow_metadata_200_response_schema_amount.update_workflow_metadata_200_response_schema_amount(
                        type = 'number', 
                        display_name = 'Example Number Attribute', ), 
                    fee = openapi_client.models.update_workflow_metadata_200_response_schema_fee.update_workflow_metadata_200_response_schema_fee(
                        type = 'monetaryAmount', 
                        display_name = 'Example Monetary Amount Attribute', ), 
                    draft = openapi_client.models.update_workflow_metadata_200_response_schema_draft.update_workflow_metadata_200_response_schema_draft(
                        type = 'array', 
                        element_type = openapi_client.models.update_workflow_metadata_200_response_schema_draft_element_type.update_workflow_metadata_200_response_schema_draft_elementType(
                            type = 'document', 
                            display_name = 'Example Document Attribute', ), ), 
                    line_items = openapi_client.models.update_workflow_metadata_200_response_schema_line_items.update_workflow_metadata_200_response_schema_lineItems(
                        type = 'array', ), ),
                permissions = ["launch","view"]
            )
        else:
            return ListAllWorkflowSchemas200ResponseListInner(
        )
        """

    def testListAllWorkflowSchemas200ResponseListInner(self):
        """Test ListAllWorkflowSchemas200ResponseListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
