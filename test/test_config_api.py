# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import looker
from looker.api.config_api import ConfigApi  # noqa: E501
from looker.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = looker.api.config_api.ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_legacy_features(self):
        """Test case for all_legacy_features

        Get All Legacy Features  # noqa: E501
        """
        pass

    def test_all_timezones(self):
        """Test case for all_timezones

        Get All Timezones  # noqa: E501
        """
        pass

    def test_backup_configuration(self):
        """Test case for backup_configuration

        Get Backup Configuration  # noqa: E501
        """
        pass

    def test_legacy_feature(self):
        """Test case for legacy_feature

        Get Legacy Feature  # noqa: E501
        """
        pass

    def test_update_backup_configuration(self):
        """Test case for update_backup_configuration

        Update Backup Configuration  # noqa: E501
        """
        pass

    def test_update_legacy_feature(self):
        """Test case for update_legacy_feature

        Update Legacy Feature  # noqa: E501
        """
        pass

    def test_update_whitelabel_configuration(self):
        """Test case for update_whitelabel_configuration

        Update Whitelabel configuration  # noqa: E501
        """
        pass

    def test_versions(self):
        """Test case for versions

        Get ApiVersion  # noqa: E501
        """
        pass

    def test_whitelabel_configuration(self):
        """Test case for whitelabel_configuration

        Get Whitelabel configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
