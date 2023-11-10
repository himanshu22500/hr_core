"""
Test for valid clockin with a fixed dummy date
"""
import datetime

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from hr_core.tests.factories.models import ClockInAttendanceFactory
from hr_core.tests.factories.models import EmployeeFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01MarkClockOutAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, api_user):
        # Arrange
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        # test_date = datetime.date(2023, 9, 9)
        test_date = "2023-09-09"

        # Act and Assert
        with freeze_time(test_date):
            now = datetime.datetime.now()
            employee = EmployeeFactory(user_id=str(api_user.user_id), joining_date=now)
            attendance = ClockInAttendanceFactory(employee=employee, clock_in_datetime=now)
            response = self.make_api_call(body=body,
                                          path_params=path_params,
                                          query_params=query_params,
                                          headers=headers,
                                          snapshot=snapshot)
