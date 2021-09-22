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


class Consent(object):
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
        'data_access_frequency': 'str',
        'title_body': 'str',
        'consent_id': 'int',
        'provider_id': 'int',
        'consent_status': 'str',
        'provider_account_id': 'int',
        'scope': 'list[Scope]',
        'title': 'str',
        'expiration_date': 'str'
    }

    attribute_map = {
        'data_access_frequency': 'dataAccessFrequency',
        'title_body': 'titleBody',
        'consent_id': 'consentId',
        'provider_id': 'providerId',
        'consent_status': 'consentStatus',
        'provider_account_id': 'providerAccountId',
        'scope': 'scope',
        'title': 'title',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, data_access_frequency=None, title_body=None, consent_id=None, provider_id=None, consent_status=None, provider_account_id=None, scope=None, title=None, expiration_date=None, _configuration=None):  # noqa: E501
        """Consent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_access_frequency = None
        self._title_body = None
        self._consent_id = None
        self._provider_id = None
        self._consent_status = None
        self._provider_account_id = None
        self._scope = None
        self._title = None
        self._expiration_date = None
        self.discriminator = None

        if data_access_frequency is not None:
            self.data_access_frequency = data_access_frequency
        self.title_body = title_body
        self.consent_id = consent_id
        self.provider_id = provider_id
        self.consent_status = consent_status
        if provider_account_id is not None:
            self.provider_account_id = provider_account_id
        self.scope = scope
        self.title = title
        self.expiration_date = expiration_date

    @property
    def data_access_frequency(self):
        """Gets the data_access_frequency of this Consent.  # noqa: E501

        Data Access Frequency explains the number of times that this consent can be used.<br> Otherwise called as consent frequency type.  # noqa: E501

        :return: The data_access_frequency of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._data_access_frequency

    @data_access_frequency.setter
    def data_access_frequency(self, data_access_frequency):
        """Sets the data_access_frequency of this Consent.

        Data Access Frequency explains the number of times that this consent can be used.<br> Otherwise called as consent frequency type.  # noqa: E501

        :param data_access_frequency: The data_access_frequency of this Consent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONE_TIME", "RECURRING"]  # noqa: E501
        if (self._configuration.client_side_validation and
                data_access_frequency not in allowed_values):
            raise ValueError(
                "Invalid value for `data_access_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(data_access_frequency, allowed_values)
            )

        self._data_access_frequency = data_access_frequency

    @property
    def title_body(self):
        """Gets the title_body of this Consent.  # noqa: E501

        Description for the title.  # noqa: E501

        :return: The title_body of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._title_body

    @title_body.setter
    def title_body(self, title_body):
        """Sets the title_body of this Consent.

        Description for the title.  # noqa: E501

        :param title_body: The title_body of this Consent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title_body is None:
            raise ValueError("Invalid value for `title_body`, must not be `None`")  # noqa: E501

        self._title_body = title_body

    @property
    def consent_id(self):
        """Gets the consent_id of this Consent.  # noqa: E501

        Consent Id generated through POST Consent.  # noqa: E501

        :return: The consent_id of this Consent.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this Consent.

        Consent Id generated through POST Consent.  # noqa: E501

        :param consent_id: The consent_id of this Consent.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def provider_id(self):
        """Gets the provider_id of this Consent.  # noqa: E501

        Provider Id for which the consent needs to be generated.  # noqa: E501

        :return: The provider_id of this Consent.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Consent.

        Provider Id for which the consent needs to be generated.  # noqa: E501

        :param provider_id: The provider_id of this Consent.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def consent_status(self):
        """Gets the consent_status of this Consent.  # noqa: E501

        Status of the consent.  # noqa: E501

        :return: The consent_status of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._consent_status

    @consent_status.setter
    def consent_status(self, consent_status):
        """Sets the consent_status of this Consent.

        Status of the consent.  # noqa: E501

        :param consent_status: The consent_status of this Consent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and consent_status is None:
            raise ValueError("Invalid value for `consent_status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "CONSENT_GENERATED", "CONSENT_ACCEPTED", "CONSENT_AUTHORIZED", "CONSENT_MISMATCH"]  # noqa: E501
        if (self._configuration.client_side_validation and
                consent_status not in allowed_values):
            raise ValueError(
                "Invalid value for `consent_status` ({0}), must be one of {1}"  # noqa: E501
                .format(consent_status, allowed_values)
            )

        self._consent_status = consent_status

    @property
    def provider_account_id(self):
        """Gets the provider_account_id of this Consent.  # noqa: E501

        Unique identifier for the provider account resource. <br>This is created during account addition.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li></ul>  # noqa: E501

        :return: The provider_account_id of this Consent.  # noqa: E501
        :rtype: int
        """
        return self._provider_account_id

    @provider_account_id.setter
    def provider_account_id(self, provider_account_id):
        """Sets the provider_account_id of this Consent.

        Unique identifier for the provider account resource. <br>This is created during account addition.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li></ul>  # noqa: E501

        :param provider_account_id: The provider_account_id of this Consent.  # noqa: E501
        :type: int
        """

        self._provider_account_id = provider_account_id

    @property
    def scope(self):
        """Gets the scope of this Consent.  # noqa: E501

        Scope describes about the consent permissions and their purpose.  # noqa: E501

        :return: The scope of this Consent.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Consent.

        Scope describes about the consent permissions and their purpose.  # noqa: E501

        :param scope: The scope of this Consent.  # noqa: E501
        :type: list[Scope]
        """
        if self._configuration.client_side_validation and scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def title(self):
        """Gets the title of this Consent.  # noqa: E501

        Title for the consent form.  # noqa: E501

        :return: The title of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Consent.

        Title for the consent form.  # noqa: E501

        :param title: The title of this Consent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def expiration_date(self):
        """Gets the expiration_date of this Consent.  # noqa: E501

        Consent expiry date.  # noqa: E501

        :return: The expiration_date of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this Consent.

        Consent expiry date.  # noqa: E501

        :param expiration_date: The expiration_date of this Consent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

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
        if issubclass(Consent, dict):
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
        if not isinstance(other, Consent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Consent):
            return True

        return self.to_dict() != other.to_dict()