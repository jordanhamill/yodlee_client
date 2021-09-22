# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yodlee
from yodlee.api.enrich_data_api import EnrichDataApi  # noqa: E501
from yodlee.rest import ApiException


class TestEnrichDataApi(unittest.TestCase):
    """EnrichDataApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.enrich_data_api.EnrichDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_push_user_data(self):
        """Test case for push_user_data

        Push UserData  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
