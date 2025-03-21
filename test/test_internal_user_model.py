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

from ironclad_python.models.internal_user_model import InternalUserModel

class TestInternalUserModel(unittest.TestCase):
    """InternalUserModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalUserModel:
        """Test InternalUserModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalUserModel`
        """
        model = InternalUserModel()
        if include_optional:
            return InternalUserModel(
                type = 'internalUser',
                display_name = 'Boba Fett',
                email = 'boba@ironclad.boba',
                user_id = '63d415e0dd0d828c3a878548',
                company_name = 'Ironclad'
            )
        else:
            return InternalUserModel(
                type = 'internalUser',
                display_name = 'Boba Fett',
                email = 'boba@ironclad.boba',
                user_id = '63d415e0dd0d828c3a878548',
                company_name = 'Ironclad',
        )
        """

    def testInternalUserModel(self):
        """Test InternalUserModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
