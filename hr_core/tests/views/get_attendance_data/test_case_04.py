"""
Invalid year value for getting details
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from hr_core.tests.factories.models import EmployeeFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04GetAttendanceDataAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"employee_id": "0"}
        query_params = {'month': 12, 'year': 2024}
        headers = {}
        employee = EmployeeFactory()
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
