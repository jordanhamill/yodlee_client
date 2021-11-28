# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yodlee
from yodlee.api.accounts_api import AccountsApi  # noqa: E501
from yodlee.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_manual_account(self):
        """Test case for create_manual_account

        Add Manual Account  # noqa: E501
        """
        pass

    def test_delete_account(self):
        """Test case for delete_account

        Delete Account  # noqa: E501
        """
        pass

    def test_evaluate_address(self):
        """Test case for evaluate_address

        Evaluate Address  # noqa: E501
        """
        pass

    def test_get_account(self):
        """Test case for get_account

        Get Account Details  # noqa: E501
        """
        pass

    def test_get_all_accounts(self):
        """Test case for get_all_accounts

        Get Accounts  # noqa: E501
        """
        pass

    def test_get_associated_accounts(self):
        """Test case for get_associated_accounts

        Associated Accounts  # noqa: E501
        """
        pass

    def test_get_historical_balances(self):
        """Test case for get_historical_balances

        Get Historical Balances  # noqa: E501
        """
        pass

    def test_get_latest_balances(self):
        """Test case for get_latest_balances

        Get Latest Balances  # noqa: E501
        """
        pass

    def test_migrate_accounts(self):
        """Test case for migrate_accounts

        Migrate Accounts  # noqa: E501
        """
        pass

    def test_update_account(self):
        """Test case for update_account

        Update Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
