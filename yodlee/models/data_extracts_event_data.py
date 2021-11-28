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


class DataExtractsEventData(object):
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
        'from_date': 'str',
        'user_data': 'list[DataExtractsEventUserData]',
        'user_count': 'int',
        'to_date': 'str'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'user_data': 'userData',
        'user_count': 'userCount',
        'to_date': 'toDate'
    }

    def __init__(self, from_date=None, user_data=None, user_count=None, to_date=None, _configuration=None):  # noqa: E501
        """DataExtractsEventData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._from_date = None
        self._user_data = None
        self._user_count = None
        self._to_date = None
        self.discriminator = None

        if from_date is not None:
            self.from_date = from_date
        if user_data is not None:
            self.user_data = user_data
        if user_count is not None:
            self.user_count = user_count
        if to_date is not None:
            self.to_date = to_date

    @property
    def from_date(self):
        """Gets the from_date of this DataExtractsEventData.  # noqa: E501


        :return: The from_date of this DataExtractsEventData.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this DataExtractsEventData.


        :param from_date: The from_date of this DataExtractsEventData.  # noqa: E501
        :type: str
        """

        self._from_date = from_date

    @property
    def user_data(self):
        """Gets the user_data of this DataExtractsEventData.  # noqa: E501


        :return: The user_data of this DataExtractsEventData.  # noqa: E501
        :rtype: list[DataExtractsEventUserData]
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this DataExtractsEventData.


        :param user_data: The user_data of this DataExtractsEventData.  # noqa: E501
        :type: list[DataExtractsEventUserData]
        """

        self._user_data = user_data

    @property
    def user_count(self):
        """Gets the user_count of this DataExtractsEventData.  # noqa: E501


        :return: The user_count of this DataExtractsEventData.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this DataExtractsEventData.


        :param user_count: The user_count of this DataExtractsEventData.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def to_date(self):
        """Gets the to_date of this DataExtractsEventData.  # noqa: E501


        :return: The to_date of this DataExtractsEventData.  # noqa: E501
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this DataExtractsEventData.


        :param to_date: The to_date of this DataExtractsEventData.  # noqa: E501
        :type: str
        """

        self._to_date = to_date

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
        if issubclass(DataExtractsEventData, dict):
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
        if not isinstance(other, DataExtractsEventData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataExtractsEventData):
            return True

        return self.to_dict() != other.to_dict()
