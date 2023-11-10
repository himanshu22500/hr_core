"""
# TODO: Update test case description
"""
import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from hr_core.tests.factories.models import EmployeeFactory
from hr_core.tests.factories.models import PresentAttendanceFactory
from hr_core.tests.factories.models import SinglePunchInAbsentAttendanceFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetFullMonthStatsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"employee_id": '0'}
        test_date = datetime.datetime(year=2023, month=2, day=20)
        test_time_delta = datetime.timedelta(hours=9)
        query_params = {'month': test_date.month, 'year': test_date.year}
        headers = {}
        employee = EmployeeFactory()

        present = PresentAttendanceFactory(employee=employee,
                                           clock_in_datetime=test_date,
                                           clock_out_datetime=test_date + test_time_delta
                                           )

        absent = SinglePunchInAbsentAttendanceFactory(employee=employee,
                                                      clock_in_datetime=test_date)
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
