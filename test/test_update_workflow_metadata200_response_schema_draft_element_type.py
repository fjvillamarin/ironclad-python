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

from ironclad_python.models.update_workflow_metadata200_response_schema_draft_element_type import UpdateWorkflowMetadata200ResponseSchemaDraftElementType

class TestUpdateWorkflowMetadata200ResponseSchemaDraftElementType(unittest.TestCase):
    """UpdateWorkflowMetadata200ResponseSchemaDraftElementType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWorkflowMetadata200ResponseSchemaDraftElementType:
        """Test UpdateWorkflowMetadata200ResponseSchemaDraftElementType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWorkflowMetadata200ResponseSchemaDraftElementType`
        """
        model = UpdateWorkflowMetadata200ResponseSchemaDraftElementType()
        if include_optional:
            return UpdateWorkflowMetadata200ResponseSchemaDraftElementType(
                type = 'document',
                display_name = 'Example Document Attribute'
            )
        else:
            return UpdateWorkflowMetadata200ResponseSchemaDraftElementType(
        )
        """

    def testUpdateWorkflowMetadata200ResponseSchemaDraftElementType(self):
        """Test UpdateWorkflowMetadata200ResponseSchemaDraftElementType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
