# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yodlee.api_client import ApiClient


class DocumentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_document(self, document_id, **kwargs):  # noqa: E501
        """Delete Document  # noqa: E501

        The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).<br>Documents can be deleted only if the document related dataset attributes are subscribed.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: documentId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_document_with_http_info(document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_document_with_http_info(document_id, **kwargs)  # noqa: E501
            return data

    def delete_document_with_http_info(self, document_id, **kwargs):  # noqa: E501
        """Delete Document  # noqa: E501

        The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).<br>Documents can be deleted only if the document related dataset attributes are subscribed.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_with_http_info(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: documentId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if self.api_client.client_side_validation and ('document_id' not in params or
                                                       params['document_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `document_id` when calling `delete_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

        query_params = []

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
            '/documents/{documentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_document(self, document_id, **kwargs):  # noqa: E501
        """Download a Document  # noqa: E501

        The get document details service allows consumers to download a document. The document is provided in base64.<br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_document(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: documentId (required)
        :return: DocumentDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_document_with_http_info(document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_document_with_http_info(document_id, **kwargs)  # noqa: E501
            return data

    def download_document_with_http_info(self, document_id, **kwargs):  # noqa: E501
        """Download a Document  # noqa: E501

        The get document details service allows consumers to download a document. The document is provided in base64.<br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_document_with_http_info(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: documentId (required)
        :return: DocumentDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if self.api_client.client_side_validation and ('document_id' not in params or
                                                       params['document_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `document_id` when calling `download_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

        query_params = []

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
            '/documents/{documentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentDownloadResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_documents(self, **kwargs):  # noqa: E501
        """Get Documents  # noqa: E501

        The get documents service allows customers to search or retrieve metadata related to documents. <br>The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. <br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_documents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keyword: The string used to search a document by its name.
        :param str account_id: The unique identifier of an account. Retrieve documents for a given accountId.
        :param str doc_type: Accepts only one of the following valid document types: STMT, TAX, and EBILL.
        :param str from_date: The date from which documents have to be retrieved.
        :param str to_date: The date to which documents have to be retrieved.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_documents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_documents_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_documents_with_http_info(self, **kwargs):  # noqa: E501
        """Get Documents  # noqa: E501

        The get documents service allows customers to search or retrieve metadata related to documents. <br>The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. <br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_documents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keyword: The string used to search a document by its name.
        :param str account_id: The unique identifier of an account. Retrieve documents for a given accountId.
        :param str doc_type: Accepts only one of the following valid document types: STMT, TAX, and EBILL.
        :param str from_date: The date from which documents have to be retrieved.
        :param str to_date: The date to which documents have to be retrieved.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'account_id', 'doc_type', 'from_date', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_documents" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('Keyword', params['keyword']))  # noqa: E501
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'doc_type' in params:
            query_params.append(('docType', params['doc_type']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

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
            '/documents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
