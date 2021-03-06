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


class LoanPayoffDetails(object):
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
        'pay_by_date': 'str',
        'payoff_amount': 'Money',
        'outstanding_balance': 'Money'
    }

    attribute_map = {
        'pay_by_date': 'payByDate',
        'payoff_amount': 'payoffAmount',
        'outstanding_balance': 'outstandingBalance'
    }

    def __init__(self, pay_by_date=None, payoff_amount=None, outstanding_balance=None, _configuration=None):  # noqa: E501
        """LoanPayoffDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pay_by_date = None
        self._payoff_amount = None
        self._outstanding_balance = None
        self.discriminator = None

        if pay_by_date is not None:
            self.pay_by_date = pay_by_date
        if payoff_amount is not None:
            self.payoff_amount = payoff_amount
        if outstanding_balance is not None:
            self.outstanding_balance = outstanding_balance

    @property
    def pay_by_date(self):
        """Gets the pay_by_date of this LoanPayoffDetails.  # noqa: E501

        The date by which the payoff amount should be paid.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The pay_by_date of this LoanPayoffDetails.  # noqa: E501
        :rtype: str
        """
        return self._pay_by_date

    @pay_by_date.setter
    def pay_by_date(self, pay_by_date):
        """Sets the pay_by_date of this LoanPayoffDetails.

        The date by which the payoff amount should be paid.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param pay_by_date: The pay_by_date of this LoanPayoffDetails.  # noqa: E501
        :type: str
        """

        self._pay_by_date = pay_by_date

    @property
    def payoff_amount(self):
        """Gets the payoff_amount of this LoanPayoffDetails.  # noqa: E501

        The loan payoff amount.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The payoff_amount of this LoanPayoffDetails.  # noqa: E501
        :rtype: Money
        """
        return self._payoff_amount

    @payoff_amount.setter
    def payoff_amount(self, payoff_amount):
        """Sets the payoff_amount of this LoanPayoffDetails.

        The loan payoff amount.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param payoff_amount: The payoff_amount of this LoanPayoffDetails.  # noqa: E501
        :type: Money
        """

        self._payoff_amount = payoff_amount

    @property
    def outstanding_balance(self):
        """Gets the outstanding_balance of this LoanPayoffDetails.  # noqa: E501

        The outstanding balance on the loan account. The outstanding balance amount may differ from the payoff amount. It is usually the sum of outstanding principal, unpaid interest, and fees, if any.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The outstanding_balance of this LoanPayoffDetails.  # noqa: E501
        :rtype: Money
        """
        return self._outstanding_balance

    @outstanding_balance.setter
    def outstanding_balance(self, outstanding_balance):
        """Sets the outstanding_balance of this LoanPayoffDetails.

        The outstanding balance on the loan account. The outstanding balance amount may differ from the payoff amount. It is usually the sum of outstanding principal, unpaid interest, and fees, if any.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: loan<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param outstanding_balance: The outstanding_balance of this LoanPayoffDetails.  # noqa: E501
        :type: Money
        """

        self._outstanding_balance = outstanding_balance

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
        if issubclass(LoanPayoffDetails, dict):
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
        if not isinstance(other, LoanPayoffDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanPayoffDetails):
            return True

        return self.to_dict() != other.to_dict()
