"""
Test with valid Employee_id , Response with 200
"""
import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from hr_core.tests.factories.models import EmployeeFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetEmployeeAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        # Arrange
        test_joining_date = datetime.datetime(year=2023, month=8, day=20)
        employee = EmployeeFactory(joining_date=test_joining_date)

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
