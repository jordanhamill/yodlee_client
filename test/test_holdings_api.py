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
from yodlee.api.holdings_api import HoldingsApi  # noqa: E501
from yodlee.rest import ApiException


class TestHoldingsApi(unittest.TestCase):
    """HoldingsApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.holdings_api.HoldingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_asset_classification_list(self):
        """Test case for get_asset_classification_list

        Get Asset Classification List  # noqa: E501
        """
        pass

    def test_get_holding_type_list(self):
        """Test case for get_holding_type_list

        Get Holding Type List  # noqa: E501
        """
        pass

    def test_get_holdings(self):
        """Test case for get_holdings

        Get Holdings  # noqa: E501
        """
        pass

    def test_get_securities(self):
        """Test case for get_securities

        Get Security Details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
