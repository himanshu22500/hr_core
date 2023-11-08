"""
# TODO: Update test case description
"""
import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from hr_core.tests.factories.models import EmployeeFactory


class TestCase01GetEmployeeAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        # Arrange
        employee = EmployeeFactory()
        employee.save()

        body = {}
        path_params = {"employee_id": "0"}
        query_params = {}
        headers = {}

        # Act and Assert
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
