"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from hr_core.tests.factories.models import EmployeeFactory
from hr_core.tests.factories.models import PresentAttendanceFactory


class TestCase01MarkClockOutAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, api_user):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        employee = EmployeeFactory(user_id=str(api_user.user_id))
        attendance = PresentAttendanceFactory(employee=employee)
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
