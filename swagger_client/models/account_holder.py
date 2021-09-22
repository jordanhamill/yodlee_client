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


class AccountHolder(object):
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
        'identifier': 'list[Identifier]',
        'gender': 'str',
        'ownership': 'str',
        'name': 'Name'
    }

    attribute_map = {
        'identifier': 'identifier',
        'gender': 'gender',
        'ownership': 'ownership',
        'name': 'name'
    }

    def __init__(self, identifier=None, gender=None, ownership=None, name=None, _configuration=None):  # noqa: E501
        """AccountHolder - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._gender = None
        self._ownership = None
        self._name = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if gender is not None:
            self.gender = gender
        if ownership is not None:
            self.ownership = ownership
        if name is not None:
            self.name = name

    @property
    def identifier(self):
        """Gets the identifier of this AccountHolder.  # noqa: E501

        Identifiers of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The identifier of this AccountHolder.  # noqa: E501
        :rtype: list[Identifier]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this AccountHolder.

        Identifiers of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param identifier: The identifier of this AccountHolder.  # noqa: E501
        :type: list[Identifier]
        """

        self._identifier = identifier

    @property
    def gender(self):
        """Gets the gender of this AccountHolder.  # noqa: E501

        Identifiers of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The gender of this AccountHolder.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this AccountHolder.

        Identifiers of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param gender: The gender of this AccountHolder.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def ownership(self):
        """Gets the ownership of this AccountHolder.  # noqa: E501

        Indicates the ownership of the account.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The ownership of this AccountHolder.  # noqa: E501
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this AccountHolder.

        Indicates the ownership of the account.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param ownership: The ownership of this AccountHolder.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY", "CUSTODIAN", "OTHERS", "POWER_OF_ATTORNEY", "TRUSTEE", "JOINT_OWNER", "BENEFICIARY", "AAS", "BUSINESS", "DBA", "TRUST"]  # noqa: E501
        if (self._configuration.client_side_validation and
                ownership not in allowed_values):
            raise ValueError(
                "Invalid value for `ownership` ({0}), must be one of {1}"  # noqa: E501
                .format(ownership, allowed_values)
            )

        self._ownership = ownership

    @property
    def name(self):
        """Gets the name of this AccountHolder.  # noqa: E501

        Name of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The name of this AccountHolder.  # noqa: E501
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountHolder.

        Name of the account holder.<br><br><b>Aggregated / Manual</b>: Aggregated <br><b>Applicable containers</b>: bank<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param name: The name of this AccountHolder.  # noqa: E501
        :type: Name
        """

        self._name = name

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
        if issubclass(AccountHolder, dict):
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
        if not isinstance(other, AccountHolder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHolder):
            return True

        return self.to_dict() != other.to_dict()