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


class UserAttribute(object):
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
        'name': 'str',
        'label': 'str',
        'type': 'str',
        'default_value': 'str',
        'is_system': 'bool',
        'value_is_hidden': 'bool',
        'user_can_view': 'bool',
        'user_can_edit': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'label': 'label',
        'type': 'type',
        'default_value': 'default_value',
        'is_system': 'is_system',
        'value_is_hidden': 'value_is_hidden',
        'user_can_view': 'user_can_view',
        'user_can_edit': 'user_can_edit',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, label=None, type=None, default_value=None, is_system=None, value_is_hidden=None, user_can_view=None, user_can_edit=None, can=None):  # noqa: E501
        """UserAttribute - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._label = None
        self._type = None
        self._default_value = None
        self._is_system = None
        self._value_is_hidden = None
        self._user_can_view = None
        self._user_can_edit = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if default_value is not None:
            self.default_value = default_value
        if is_system is not None:
            self.is_system = is_system
        if value_is_hidden is not None:
            self.value_is_hidden = value_is_hidden
        if user_can_view is not None:
            self.user_can_view = user_can_view
        if user_can_edit is not None:
            self.user_can_edit = user_can_edit
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this UserAttribute.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this UserAttribute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAttribute.

        Unique Id  # noqa: E501

        :param id: The id of this UserAttribute.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserAttribute.  # noqa: E501

        Name of user attribute  # noqa: E501

        :return: The name of this UserAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAttribute.

        Name of user attribute  # noqa: E501

        :param name: The name of this UserAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this UserAttribute.  # noqa: E501

        Human-friendly label for user attribute  # noqa: E501

        :return: The label of this UserAttribute.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this UserAttribute.

        Human-friendly label for user attribute  # noqa: E501

        :param label: The label of this UserAttribute.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this UserAttribute.  # noqa: E501

        Type of user attribute (\"string\", \"number\", \"datetime\", \"yesno\", \"zipcode\")  # noqa: E501

        :return: The type of this UserAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserAttribute.

        Type of user attribute (\"string\", \"number\", \"datetime\", \"yesno\", \"zipcode\")  # noqa: E501

        :param type: The type of this UserAttribute.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this UserAttribute.  # noqa: E501

        Default value for when no value is set on the user  # noqa: E501

        :return: The default_value of this UserAttribute.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this UserAttribute.

        Default value for when no value is set on the user  # noqa: E501

        :param default_value: The default_value of this UserAttribute.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def is_system(self):
        """Gets the is_system of this UserAttribute.  # noqa: E501

        Attribute is a system default  # noqa: E501

        :return: The is_system of this UserAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """Sets the is_system of this UserAttribute.

        Attribute is a system default  # noqa: E501

        :param is_system: The is_system of this UserAttribute.  # noqa: E501
        :type: bool
        """

        self._is_system = is_system

    @property
    def value_is_hidden(self):
        """Gets the value_is_hidden of this UserAttribute.  # noqa: E501

        If true, users will not be able to view values of this attribute  # noqa: E501

        :return: The value_is_hidden of this UserAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._value_is_hidden

    @value_is_hidden.setter
    def value_is_hidden(self, value_is_hidden):
        """Sets the value_is_hidden of this UserAttribute.

        If true, users will not be able to view values of this attribute  # noqa: E501

        :param value_is_hidden: The value_is_hidden of this UserAttribute.  # noqa: E501
        :type: bool
        """

        self._value_is_hidden = value_is_hidden

    @property
    def user_can_view(self):
        """Gets the user_can_view of this UserAttribute.  # noqa: E501

        Non-admin users can see the values of their attributes and use them in filters  # noqa: E501

        :return: The user_can_view of this UserAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_view

    @user_can_view.setter
    def user_can_view(self, user_can_view):
        """Sets the user_can_view of this UserAttribute.

        Non-admin users can see the values of their attributes and use them in filters  # noqa: E501

        :param user_can_view: The user_can_view of this UserAttribute.  # noqa: E501
        :type: bool
        """

        self._user_can_view = user_can_view

    @property
    def user_can_edit(self):
        """Gets the user_can_edit of this UserAttribute.  # noqa: E501

        Users can change the value of this attribute for themselves  # noqa: E501

        :return: The user_can_edit of this UserAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_edit

    @user_can_edit.setter
    def user_can_edit(self, user_can_edit):
        """Sets the user_can_edit of this UserAttribute.

        Users can change the value of this attribute for themselves  # noqa: E501

        :param user_can_edit: The user_can_edit of this UserAttribute.  # noqa: E501
        :type: bool
        """

        self._user_can_edit = user_can_edit

    @property
    def can(self):
        """Gets the can of this UserAttribute.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this UserAttribute.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this UserAttribute.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this UserAttribute.  # noqa: E501
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
        if not isinstance(other, UserAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
