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

from ironclad_python.models.update_workflow_metadata200_response_creator import UpdateWorkflowMetadata200ResponseCreator

class TestUpdateWorkflowMetadata200ResponseCreator(unittest.TestCase):
    """UpdateWorkflowMetadata200ResponseCreator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWorkflowMetadata200ResponseCreator:
        """Test UpdateWorkflowMetadata200ResponseCreator
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWorkflowMetadata200ResponseCreator`
        """
        model = UpdateWorkflowMetadata200ResponseCreator()
        if include_optional:
            return UpdateWorkflowMetadata200ResponseCreator(
                display_name = 'Boba Fett',
                email = 'fett@intergalactic.com',
                id = '63d415e0dd0d828c3a878548'
            )
        else:
            return UpdateWorkflowMetadata200ResponseCreator(
        )
        """

    def testUpdateWorkflowMetadata200ResponseCreator(self):
        """Test UpdateWorkflowMetadata200ResponseCreator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
