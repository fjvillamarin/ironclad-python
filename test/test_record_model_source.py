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

from ironclad_python.models.record_model_source import RecordModelSource

class TestRecordModelSource(unittest.TestCase):
    """RecordModelSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordModelSource:
        """Test RecordModelSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordModelSource`
        """
        model = RecordModelSource()
        if include_optional:
            return RecordModelSource(
                type = 'workflow',
                workflow_id = 'abcd1234'
            )
        else:
            return RecordModelSource(
        )
        """

    def testRecordModelSource(self):
        """Test RecordModelSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
