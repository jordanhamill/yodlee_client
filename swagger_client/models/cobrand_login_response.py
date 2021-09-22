# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yodlee_client.configuration import Configuration


class CobrandLoginResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session': 'CobrandSession',
        'cobrand_id': 'int',
        'application_id': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'session': 'session',
        'cobrand_id': 'cobrandId',
        'application_id': 'applicationId',
        'locale': 'locale'
    }

    def __init__(self, session=None, cobrand_id=None, application_id=None, locale=None, _configuration=None):  # noqa: E501
        """CobrandLoginResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session = None
        self._cobrand_id = None
        self._application_id = None
        self._locale = None
        self.discriminator = None

        if session is not None:
            self.session = session
        if cobrand_id is not None:
            self.cobrand_id = cobrand_id
        if application_id is not None:
            self.application_id = application_id
        if locale is not None:
            self.locale = locale

    @property
    def session(self):
        """Gets the session of this CobrandLoginResponse.  # noqa: E501


        :return: The session of this CobrandLoginResponse.  # noqa: E501
        :rtype: CobrandSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this CobrandLoginResponse.


        :param session: The session of this CobrandLoginResponse.  # noqa: E501
        :type: CobrandSession
        """

        self._session = session

    @property
    def cobrand_id(self):
        """Gets the cobrand_id of this CobrandLoginResponse.  # noqa: E501

        Unique identifier of the cobrand (customer) in the system.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :return: The cobrand_id of this CobrandLoginResponse.  # noqa: E501
        :rtype: int
        """
        return self._cobrand_id

    @cobrand_id.setter
    def cobrand_id(self, cobrand_id):
        """Sets the cobrand_id of this CobrandLoginResponse.

        Unique identifier of the cobrand (customer) in the system.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :param cobrand_id: The cobrand_id of this CobrandLoginResponse.  # noqa: E501
        :type: int
        """

        self._cobrand_id = cobrand_id

    @property
    def application_id(self):
        """Gets the application_id of this CobrandLoginResponse.  # noqa: E501

        The application identifier.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :return: The application_id of this CobrandLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CobrandLoginResponse.

        The application identifier.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :param application_id: The application_id of this CobrandLoginResponse.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def locale(self):
        """Gets the locale of this CobrandLoginResponse.  # noqa: E501

        The customer's locale that will be considered for the localization functionality.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :return: The locale of this CobrandLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CobrandLoginResponse.

        The customer's locale that will be considered for the localization functionality.<br><br><b>Endpoints</b>:<ul><li>POST cobrand/login</li></ul>  # noqa: E501

        :param locale: The locale of this CobrandLoginResponse.  # noqa: E501
        :type: str
        """

        self._locale = locale

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CobrandLoginResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CobrandLoginResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CobrandLoginResponse):
            return True

        return self.to_dict() != other.to_dict()