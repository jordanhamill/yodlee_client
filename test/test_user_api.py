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
from yodlee.api.user_api import UserApi  # noqa: E501
from yodlee.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = yodlee.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_access_tokens(self):
        """Test case for get_access_tokens

        Get Access Tokens  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get User Details  # noqa: E501
        """
        pass

    def test_register_user(self):
        """Test case for register_user

        Register User  # noqa: E501
        """
        pass

    def test_saml_login(self):
        """Test case for saml_login

        Saml Login  # noqa: E501
        """
        pass

    def test_unregister(self):
        """Test case for unregister

        Delete User  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update User Details  # noqa: E501
        """
        pass

    def test_user_logout(self):
        """Test case for user_logout

        User Logout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
