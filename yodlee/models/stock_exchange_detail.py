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


class StockExchangeDetail(object):
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
        'symbol': 'str',
        'country_code': 'str',
        'currency_code': 'str',
        'exchange_code': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'country_code': 'countryCode',
        'currency_code': 'currencyCode',
        'exchange_code': 'exchangeCode'
    }

    def __init__(self, symbol=None, country_code=None, currency_code=None, exchange_code=None, _configuration=None):  # noqa: E501
        """StockExchangeDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._symbol = None
        self._country_code = None
        self._currency_code = None
        self._exchange_code = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if country_code is not None:
            self.country_code = country_code
        if currency_code is not None:
            self.currency_code = currency_code
        if exchange_code is not None:
            self.exchange_code = exchange_code

    @property
    def symbol(self):
        """Gets the symbol of this StockExchangeDetail.  # noqa: E501

        Ticker symbol representing particular securities listed on an exchange.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :return: The symbol of this StockExchangeDetail.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this StockExchangeDetail.

        Ticker symbol representing particular securities listed on an exchange.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :param symbol: The symbol of this StockExchangeDetail.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def country_code(self):
        """Gets the country_code of this StockExchangeDetail.  # noqa: E501

        Country codes are geocodes developed to represent countries and dependent areas.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :return: The country_code of this StockExchangeDetail.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this StockExchangeDetail.

        Country codes are geocodes developed to represent countries and dependent areas.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :param country_code: The country_code of this StockExchangeDetail.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def currency_code(self):
        """Gets the currency_code of this StockExchangeDetail.  # noqa: E501

        ISO codes of currency.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :return: The currency_code of this StockExchangeDetail.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this StockExchangeDetail.

        ISO codes of currency.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :param currency_code: The currency_code of this StockExchangeDetail.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def exchange_code(self):
        """Gets the exchange_code of this StockExchangeDetail.  # noqa: E501

        An Exchange code is a four-character code used to identify stock markets and other trading exchanges within global trading.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :return: The exchange_code of this StockExchangeDetail.  # noqa: E501
        :rtype: str
        """
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, exchange_code):
        """Sets the exchange_code of this StockExchangeDetail.

        An Exchange code is a four-character code used to identify stock markets and other trading exchanges within global trading.<br><br><b>Applicable containers</b>: investment, insurance<br>  # noqa: E501

        :param exchange_code: The exchange_code of this StockExchangeDetail.  # noqa: E501
        :type: str
        """

        self._exchange_code = exchange_code

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
        if issubclass(StockExchangeDetail, dict):
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
        if not isinstance(other, StockExchangeDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StockExchangeDetail):
            return True

        return self.to_dict() != other.to_dict()
