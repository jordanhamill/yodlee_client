# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yodlee_client.api_client import ApiClient


class VerificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_verification_status(self, **kwargs):  # noqa: E501
        """Get Verification Status  # noqa: E501

        The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.<br>For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_verification_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Comma separated accountId
        :param str provider_account_id: Comma separated providerAccountId
        :param str verification_type: verificationType
        :return: VerificationStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_verification_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_verification_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_verification_status_with_http_info(self, **kwargs):  # noqa: E501
        """Get Verification Status  # noqa: E501

        The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.<br>For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_verification_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Comma separated accountId
        :param str provider_account_id: Comma separated providerAccountId
        :param str verification_type: verificationType
        :return: VerificationStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'provider_account_id', 'verification_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_verification_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'provider_account_id' in params:
            query_params.append(('providerAccountId', params['provider_account_id']))  # noqa: E501
        if 'verification_type' in params:
            query_params.append(('verificationType', params['verification_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/verification', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerificationStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def initiate_matching_or_challenge_deposite_verification(self, verification_param, **kwargs):  # noqa: E501
        """Initiaite Matching Service and Challenge Deposit  # noqa: E501

        The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership. The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings). <ul><li>MS verification - The MS verification can be initiated only for an already aggregated account or a providerAccount. The prerequisite for the MS verification process is to request the following ACCT_PROFILE dataset attributes:</li><ul><li>FULL_ACCT_NUMBER</li><li>BANK_TRANSFER_CODE (optional based on the configuration done for the customer)</li><li>HOLDER_NAME</li></ul>In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. Contact the Yodlee CustomerCare team to configure the full name or only the last name match.</li></ul><ul><li>Challenge deposit account verification - Once the CDV process is initiated, Yodlee will post the microtransaction (i.e., credit and debit) in the user's account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details. The CDV process is currently supported only in the United States.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_matching_or_challenge_deposite_verification(verification_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerificationRequest verification_param: verification information (required)
        :return: VerificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.initiate_matching_or_challenge_deposite_verification_with_http_info(verification_param, **kwargs)  # noqa: E501
        else:
            (data) = self.initiate_matching_or_challenge_deposite_verification_with_http_info(verification_param, **kwargs)  # noqa: E501
            return data

    def initiate_matching_or_challenge_deposite_verification_with_http_info(self, verification_param, **kwargs):  # noqa: E501
        """Initiaite Matching Service and Challenge Deposit  # noqa: E501

        The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership. The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings). <ul><li>MS verification - The MS verification can be initiated only for an already aggregated account or a providerAccount. The prerequisite for the MS verification process is to request the following ACCT_PROFILE dataset attributes:</li><ul><li>FULL_ACCT_NUMBER</li><li>BANK_TRANSFER_CODE (optional based on the configuration done for the customer)</li><li>HOLDER_NAME</li></ul>In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. Contact the Yodlee CustomerCare team to configure the full name or only the last name match.</li></ul><ul><li>Challenge deposit account verification - Once the CDV process is initiated, Yodlee will post the microtransaction (i.e., credit and debit) in the user's account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details. The CDV process is currently supported only in the United States.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_matching_or_challenge_deposite_verification_with_http_info(verification_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerificationRequest verification_param: verification information (required)
        :return: VerificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verification_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_matching_or_challenge_deposite_verification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verification_param' is set
        if self.api_client.client_side_validation and ('verification_param' not in params or
                                                       params['verification_param'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `verification_param` when calling `initiate_matching_or_challenge_deposite_verification`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'verification_param' in params:
            body_params = params['verification_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/verification', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_challenge_deposit(self, verification_param, **kwargs):  # noqa: E501
        """Verify Challenge Deposit  # noqa: E501

        The put verification service is used to complete the CDV process.<br> In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee.<br> For a successful verification of the account's ownership both microtransaction details should match.<br>The CDV process is currently supported only in the United States.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_challenge_deposit(verification_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateVerificationRequest verification_param: verification information (required)
        :return: VerificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_challenge_deposit_with_http_info(verification_param, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_challenge_deposit_with_http_info(verification_param, **kwargs)  # noqa: E501
            return data

    def verify_challenge_deposit_with_http_info(self, verification_param, **kwargs):  # noqa: E501
        """Verify Challenge Deposit  # noqa: E501

        The put verification service is used to complete the CDV process.<br> In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee.<br> For a successful verification of the account's ownership both microtransaction details should match.<br>The CDV process is currently supported only in the United States.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_challenge_deposit_with_http_info(verification_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateVerificationRequest verification_param: verification information (required)
        :return: VerificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verification_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_challenge_deposit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verification_param' is set
        if self.api_client.client_side_validation and ('verification_param' not in params or
                                                       params['verification_param'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `verification_param` when calling `verify_challenge_deposit`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'verification_param' in params:
            body_params = params['verification_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/verification', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)