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


class DerivedNetworth(object):
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
        '_date': 'str',
        'liability': 'Money',
        'historical_balances': 'list[DerivedNetworthHistoricalBalance]',
        'networth': 'Money',
        'asset': 'Money'
    }

    attribute_map = {
        '_date': 'date',
        'liability': 'liability',
        'historical_balances': 'historicalBalances',
        'networth': 'networth',
        'asset': 'asset'
    }

    def __init__(self, _date=None, liability=None, historical_balances=None, networth=None, asset=None, _configuration=None):  # noqa: E501
        """DerivedNetworth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._liability = None
        self._historical_balances = None
        self._networth = None
        self._asset = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if liability is not None:
            self.liability = liability
        if historical_balances is not None:
            self.historical_balances = historical_balances
        if networth is not None:
            self.networth = networth
        if asset is not None:
            self.asset = asset

    @property
    def _date(self):
        """Gets the _date of this DerivedNetworth.  # noqa: E501

        The date as of when the networth information is provided.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :return: The _date of this DerivedNetworth.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DerivedNetworth.

        The date as of when the networth information is provided.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :param _date: The _date of this DerivedNetworth.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def liability(self):
        """Gets the liability of this DerivedNetworth.  # noqa: E501

        The liability amount that the user owes.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :return: The liability of this DerivedNetworth.  # noqa: E501
        :rtype: Money
        """
        return self._liability

    @liability.setter
    def liability(self, liability):
        """Sets the liability of this DerivedNetworth.

        The liability amount that the user owes.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :param liability: The liability of this DerivedNetworth.  # noqa: E501
        :type: Money
        """

        self._liability = liability

    @property
    def historical_balances(self):
        """Gets the historical_balances of this DerivedNetworth.  # noqa: E501

        Balances of the accounts over the period of time.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :return: The historical_balances of this DerivedNetworth.  # noqa: E501
        :rtype: list[DerivedNetworthHistoricalBalance]
        """
        return self._historical_balances

    @historical_balances.setter
    def historical_balances(self, historical_balances):
        """Sets the historical_balances of this DerivedNetworth.

        Balances of the accounts over the period of time.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :param historical_balances: The historical_balances of this DerivedNetworth.  # noqa: E501
        :type: list[DerivedNetworthHistoricalBalance]
        """

        self._historical_balances = historical_balances

    @property
    def networth(self):
        """Gets the networth of this DerivedNetworth.  # noqa: E501

        Networth of the user.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :return: The networth of this DerivedNetworth.  # noqa: E501
        :rtype: Money
        """
        return self._networth

    @networth.setter
    def networth(self, networth):
        """Sets the networth of this DerivedNetworth.

        Networth of the user.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :param networth: The networth of this DerivedNetworth.  # noqa: E501
        :type: Money
        """

        self._networth = networth

    @property
    def asset(self):
        """Gets the asset of this DerivedNetworth.  # noqa: E501

        The asset value that the user owns.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :return: The asset of this DerivedNetworth.  # noqa: E501
        :rtype: Money
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this DerivedNetworth.

        The asset value that the user owns.<br><br><b>Applicable containers</b>: bank, creditcard, investment, insurance, realEstate, loan<br>  # noqa: E501

        :param asset: The asset of this DerivedNetworth.  # noqa: E501
        :type: Money
        """

        self._asset = asset

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
        if issubclass(DerivedNetworth, dict):
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
        if not isinstance(other, DerivedNetworth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivedNetworth):
            return True

        return self.to_dict() != other.to_dict()
