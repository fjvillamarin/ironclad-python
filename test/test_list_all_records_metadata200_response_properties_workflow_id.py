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

from ironclad_python.models.list_all_records_metadata200_response_properties_workflow_id import ListAllRecordsMetadata200ResponsePropertiesWorkflowId

class TestListAllRecordsMetadata200ResponsePropertiesWorkflowId(unittest.TestCase):
    """ListAllRecordsMetadata200ResponsePropertiesWorkflowId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAllRecordsMetadata200ResponsePropertiesWorkflowId:
        """Test ListAllRecordsMetadata200ResponsePropertiesWorkflowId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllRecordsMetadata200ResponsePropertiesWorkflowId`
        """
        model = ListAllRecordsMetadata200ResponsePropertiesWorkflowId()
        if include_optional:
            return ListAllRecordsMetadata200ResponsePropertiesWorkflowId(
                display_name = 'Workflow ID',
                type = 'string',
                visible = True
            )
        else:
            return ListAllRecordsMetadata200ResponsePropertiesWorkflowId(
        )
        """

    def testListAllRecordsMetadata200ResponsePropertiesWorkflowId(self):
        """Test ListAllRecordsMetadata200ResponsePropertiesWorkflowId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
