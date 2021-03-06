# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CredentialsApi3(object):
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
        'id': 'int',
        'client_id': 'str',
        'created_at': 'str',
        'is_disabled': 'bool',
        'type': 'str',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'client_id': 'client_id',
        'created_at': 'created_at',
        'is_disabled': 'is_disabled',
        'type': 'type',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, id=None, client_id=None, created_at=None, is_disabled=None, type=None, url=None, can=None):  # noqa: E501
        """CredentialsApi3 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._client_id = None
        self._created_at = None
        self._is_disabled = None
        self._type = None
        self._url = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if client_id is not None:
            self.client_id = client_id
        if created_at is not None:
            self.created_at = created_at
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this CredentialsApi3.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this CredentialsApi3.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CredentialsApi3.

        Unique Id  # noqa: E501

        :param id: The id of this CredentialsApi3.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this CredentialsApi3.  # noqa: E501

        API key client_id  # noqa: E501

        :return: The client_id of this CredentialsApi3.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CredentialsApi3.

        API key client_id  # noqa: E501

        :param client_id: The client_id of this CredentialsApi3.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def created_at(self):
        """Gets the created_at of this CredentialsApi3.  # noqa: E501

        Timestamp for the creation of this credential  # noqa: E501

        :return: The created_at of this CredentialsApi3.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CredentialsApi3.

        Timestamp for the creation of this credential  # noqa: E501

        :param created_at: The created_at of this CredentialsApi3.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CredentialsApi3.  # noqa: E501

        Has this credential been disabled?  # noqa: E501

        :return: The is_disabled of this CredentialsApi3.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CredentialsApi3.

        Has this credential been disabled?  # noqa: E501

        :param is_disabled: The is_disabled of this CredentialsApi3.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def type(self):
        """Gets the type of this CredentialsApi3.  # noqa: E501

        Short name for the type of this kind of credential  # noqa: E501

        :return: The type of this CredentialsApi3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialsApi3.

        Short name for the type of this kind of credential  # noqa: E501

        :param type: The type of this CredentialsApi3.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this CredentialsApi3.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this CredentialsApi3.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CredentialsApi3.

        Link to get this item  # noqa: E501

        :param url: The url of this CredentialsApi3.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this CredentialsApi3.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this CredentialsApi3.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this CredentialsApi3.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this CredentialsApi3.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CredentialsApi3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
