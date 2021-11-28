# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yodlee.configuration import Configuration


class UserAddress(object):
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
        'zip': 'str',
        'country': 'str',
        'address3': 'str',
        'address2': 'str',
        'city': 'str',
        'address1': 'str',
        'state': 'str'
    }

    attribute_map = {
        'zip': 'zip',
        'country': 'country',
        'address3': 'address3',
        'address2': 'address2',
        'city': 'city',
        'address1': 'address1',
        'state': 'state'
    }

    def __init__(self, zip=None, country=None, address3=None, address2=None, city=None, address1=None, state=None, _configuration=None):  # noqa: E501
        """UserAddress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._zip = None
        self._country = None
        self._address3 = None
        self._address2 = None
        self._city = None
        self._address1 = None
        self._state = None
        self.discriminator = None

        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country
        if address3 is not None:
            self.address3 = address3
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if address1 is not None:
            self.address1 = address1
        if state is not None:
            self.state = state

    @property
    def zip(self):
        """Gets the zip of this UserAddress.  # noqa: E501


        :return: The zip of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this UserAddress.


        :param zip: The zip of this UserAddress.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this UserAddress.  # noqa: E501


        :return: The country of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserAddress.


        :param country: The country of this UserAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def address3(self):
        """Gets the address3 of this UserAddress.  # noqa: E501


        :return: The address3 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this UserAddress.


        :param address3: The address3 of this UserAddress.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def address2(self):
        """Gets the address2 of this UserAddress.  # noqa: E501


        :return: The address2 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this UserAddress.


        :param address2: The address2 of this UserAddress.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this UserAddress.  # noqa: E501


        :return: The city of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UserAddress.


        :param city: The city of this UserAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def address1(self):
        """Gets the address1 of this UserAddress.  # noqa: E501


        :return: The address1 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this UserAddress.


        :param address1: The address1 of this UserAddress.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def state(self):
        """Gets the state of this UserAddress.  # noqa: E501


        :return: The state of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UserAddress.


        :param state: The state of this UserAddress.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(UserAddress, dict):
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
        if not isinstance(other, UserAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAddress):
            return True

        return self.to_dict() != other.to_dict()
