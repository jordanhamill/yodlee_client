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
from yodlee.api.transactions_api import TransactionsApi  # noqa: E501
from yodlee.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_run_transaction_categorization_rules(self):
        """Test case for create_or_run_transaction_categorization_rules

        Create or Run Transaction Categorization Rule  # noqa: E501
        """
        pass

    def test_create_transaction_category(self):
        """Test case for create_transaction_category

        Create Category  # noqa: E501
        """
        pass

    def test_delete_transaction_categorization_rule(self):
        """Test case for delete_transaction_categorization_rule

        Delete Transaction Categorization Rule  # noqa: E501
        """
        pass

    def test_delete_transaction_category(self):
        """Test case for delete_transaction_category

        Delete Category  # noqa: E501
        """
        pass

    def test_get_transaction_categories(self):
        """Test case for get_transaction_categories

        Get Transaction Category List  # noqa: E501
        """
        pass

    def test_get_transaction_categorization_rules(self):
        """Test case for get_transaction_categorization_rules

        Get Transaction Categorization Rules  # noqa: E501
        """
        pass

    def test_get_transaction_categorization_rules_deprecated(self):
        """Test case for get_transaction_categorization_rules_deprecated

        Get Transaction Categorization Rules  # noqa: E501
        """
        pass

    def test_get_transactions(self):
        """Test case for get_transactions

        Get Transactions  # noqa: E501
        """
        pass

    def test_get_transactions_count(self):
        """Test case for get_transactions_count

        Get Transactions Count  # noqa: E501
        """
        pass

    def test_run_transaction_categorization_rule(self):
        """Test case for run_transaction_categorization_rule

        Run Transaction Categorization Rule  # noqa: E501
        """
        pass

    def test_update_transaction(self):
        """Test case for update_transaction

        Update Transaction  # noqa: E501
        """
        pass

    def test_update_transaction_categorization_rule(self):
        """Test case for update_transaction_categorization_rule

        Update Transaction Categorization Rule  # noqa: E501
        """
        pass

    def test_update_transaction_category(self):
        """Test case for update_transaction_category

        Update Category  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
