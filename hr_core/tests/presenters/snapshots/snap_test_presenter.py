# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenterImplementation.test_get_mark_clock_in_response 1'] = {
    'attendance_id': '1',
    'clock_in_date_time': '0001-01-01 01:00:00'
}

snapshots['TestPresenterImplementation.test_get_response_for_get_attendance_data 2'] = {
    'attendance_data': [
        {
            'attendance_id': '1',
            'clock_in_date_time': '0001-01-01 01:00:00',
            'clock_out_date_time': '0001-01-01 10:00:00',
            'status': 'PRESENT'
        }
    ]
}

snapshots['TestPresenterImplementation.test_raise_exception_for_employee_already_clocked_in 3'] = {
    'http_status_code': 400,
    'res_status': 'EMPLOYEE_ALREADY_CLOCKED_IN',
    'response': 'Employee Already Clocked in'
}

snapshots['TestPresenterImplementation.test_raise_exception_for_employee_already_clocked_out 4'] = {
    'http_status_code': 400,
    'res_status': 'EMPLOYEE_ALREADY_CLOCKED_OUT',
    'response': 'Employee Already Clocked out'
}

snapshots['TestPresenterImplementation.test_raise_exception_for_invalid_month INVALID MONTH'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MONTH',
    'response': 'Month must be in range 1 to 12'
}

snapshots['TestPresenterImplementation.test_raise_exception_for_invalid_year INVALID_YEAR'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_YEAR',
    'response': 'Year must be less then current year'
}

snapshots['TestPresenterImplementation.test_get_response_for_get_full_month_stats Full month Stats success response'] = {
    'total_absent_days': 1,
    'total_present_days': 1,
    'total_single_punch_in_days': 1,
    'total_working_days': 3
}

snapshots['TestPresenterImplementation.test_raise_exception_for_employee_not_clocked_in Employee Not Clocked In'] = {
    'http_status_code': 400,
    'res_status': 'EMPLOYEE_NOT_CLOCKED_IN',
    'response': 'Employee Not Clocked in'
}

snapshots['TestPresenterImplementation.test_get_mark_clock_out_response Clock Out Response'] = {
    'attendance_id': '1',
    'clock_out_date_time': '0001-01-01 01:00:00'
}

snapshots['TestPresenterImplementation.test_raise_exception_for_invalid_employee Invalid Employee id Response'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_EMPLOYEE_ID',
    'response': 'Employee Does not exist'
}

snapshots['TestPresenterImplementation.test_get_response_for_get_employee Employee details response'] = {
    'department': 'ENGINEERING',
    'email': 'himanshu22500@gmail.com',
    'employee_id': '1',
    'first_name': 'Himanshu',
    'job_role': 'JUNIOR_ENGINEER',
    'joining_date': '0001-01-01 01:00:00',
    'last_name': 'Mishra',
    'phone_number': '8172932823'
}
