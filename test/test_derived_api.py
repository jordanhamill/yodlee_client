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
from yodlee.api.derived_api import DerivedApi  # noqa: E501
from yodlee.rest import ApiException


class TestDerivedApi(unittest.TestCase):
    """DerivedApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.derived_api.DerivedApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_holding_summary(self):
        """Test case for get_holding_summary

        Get Holding Summary  # noqa: E501
        """
        pass

    def test_get_networth(self):
        """Test case for get_networth

        Get Networth Summary  # noqa: E501
        """
        pass

    def test_get_transaction_summary(self):
        """Test case for get_transaction_summary

        Get Transaction Summary  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
