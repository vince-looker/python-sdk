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


class LookmlModelExploreFieldMapLayer(object):
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
        'url': 'str',
        'feature_key': 'str',
        'property_key': 'str',
        'property_label_key': 'str',
        'projection': 'str',
        'format': 'str',
        'extents_json_url': 'str',
        'max_zoom_level': 'int',
        'min_zoom_level': 'int'
    }

    attribute_map = {
        'url': 'url',
        'feature_key': 'feature_key',
        'property_key': 'property_key',
        'property_label_key': 'property_label_key',
        'projection': 'projection',
        'format': 'format',
        'extents_json_url': 'extents_json_url',
        'max_zoom_level': 'max_zoom_level',
        'min_zoom_level': 'min_zoom_level'
    }

    def __init__(self, url=None, feature_key=None, property_key=None, property_label_key=None, projection=None, format=None, extents_json_url=None, max_zoom_level=None, min_zoom_level=None):  # noqa: E501
        """LookmlModelExploreFieldMapLayer - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._feature_key = None
        self._property_key = None
        self._property_label_key = None
        self._projection = None
        self._format = None
        self._extents_json_url = None
        self._max_zoom_level = None
        self._min_zoom_level = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if feature_key is not None:
            self.feature_key = feature_key
        if property_key is not None:
            self.property_key = property_key
        if property_label_key is not None:
            self.property_label_key = property_label_key
        if projection is not None:
            self.projection = projection
        if format is not None:
            self.format = format
        if extents_json_url is not None:
            self.extents_json_url = extents_json_url
        if max_zoom_level is not None:
            self.max_zoom_level = max_zoom_level
        if min_zoom_level is not None:
            self.min_zoom_level = min_zoom_level

    @property
    def url(self):
        """Gets the url of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        URL to the map layer resource.  # noqa: E501

        :return: The url of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LookmlModelExploreFieldMapLayer.

        URL to the map layer resource.  # noqa: E501

        :param url: The url of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def feature_key(self):
        """Gets the feature_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..  # noqa: E501

        :return: The feature_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._feature_key

    @feature_key.setter
    def feature_key(self, feature_key):
        """Sets the feature_key of this LookmlModelExploreFieldMapLayer.

        Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..  # noqa: E501

        :param feature_key: The feature_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._feature_key = feature_key

    @property
    def property_key(self):
        """Gets the property_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.  # noqa: E501

        :return: The property_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this LookmlModelExploreFieldMapLayer.

        Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.  # noqa: E501

        :param property_key: The property_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._property_key = property_key

    @property
    def property_label_key(self):
        """Gets the property_label_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        Which property from the TopoJSON data to use to label the region. When null, property_key should be used.  # noqa: E501

        :return: The property_label_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._property_label_key

    @property_label_key.setter
    def property_label_key(self, property_label_key):
        """Sets the property_label_key of this LookmlModelExploreFieldMapLayer.

        Which property from the TopoJSON data to use to label the region. When null, property_key should be used.  # noqa: E501

        :param property_label_key: The property_label_key of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._property_label_key = property_label_key

    @property
    def projection(self):
        """Gets the projection of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.  # noqa: E501

        :return: The projection of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._projection

    @projection.setter
    def projection(self, projection):
        """Sets the projection of this LookmlModelExploreFieldMapLayer.

        The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.  # noqa: E501

        :param projection: The projection of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._projection = projection

    @property
    def format(self):
        """Gets the format of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        Specifies the data format of the region information. Valid values are: \"topojson\", \"vector_tile_region\".  # noqa: E501

        :return: The format of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LookmlModelExploreFieldMapLayer.

        Specifies the data format of the region information. Valid values are: \"topojson\", \"vector_tile_region\".  # noqa: E501

        :param format: The format of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def extents_json_url(self):
        """Gets the extents_json_url of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.  # noqa: E501

        :return: The extents_json_url of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: str
        """
        return self._extents_json_url

    @extents_json_url.setter
    def extents_json_url(self, extents_json_url):
        """Sets the extents_json_url of this LookmlModelExploreFieldMapLayer.

        Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.  # noqa: E501

        :param extents_json_url: The extents_json_url of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: str
        """

        self._extents_json_url = extents_json_url

    @property
    def max_zoom_level(self):
        """Gets the max_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.  # noqa: E501

        :return: The max_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: int
        """
        return self._max_zoom_level

    @max_zoom_level.setter
    def max_zoom_level(self, max_zoom_level):
        """Sets the max_zoom_level of this LookmlModelExploreFieldMapLayer.

        The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.  # noqa: E501

        :param max_zoom_level: The max_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: int
        """

        self._max_zoom_level = max_zoom_level

    @property
    def min_zoom_level(self):
        """Gets the min_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501

        The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.  # noqa: E501

        :return: The min_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :rtype: int
        """
        return self._min_zoom_level

    @min_zoom_level.setter
    def min_zoom_level(self, min_zoom_level):
        """Sets the min_zoom_level of this LookmlModelExploreFieldMapLayer.

        The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.  # noqa: E501

        :param min_zoom_level: The min_zoom_level of this LookmlModelExploreFieldMapLayer.  # noqa: E501
        :type: int
        """

        self._min_zoom_level = min_zoom_level

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
        if not isinstance(other, LookmlModelExploreFieldMapLayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
