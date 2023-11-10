"""
Valid Employee Id and one present attendance field
"""
import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from hr_core.tests.factories.models import EmployeeFactory
from hr_core.tests.factories.models import PresentAttendanceFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetAttendanceDataAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        # Arrange
        body = {}
        path_params = {"employee_id": "0"}
        test_date = datetime.date(year=2023, month=10, day=20)
        five_week_delta = datetime.timedelta(weeks=5)
        query_params = {'month': test_date.month, 'year': test_date.year}
        headers = {}
        employee = EmployeeFactory(joining_date=test_date - five_week_delta)
        attendance = PresentAttendanceFactory(employee=employee, clock_in_datetime=test_date,
                                              clock_out_datetime=test_date + datetime.timedelta(hours=9))

        # Act and Assert
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
