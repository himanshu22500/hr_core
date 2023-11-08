# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetEmployeeAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetEmployeeAPITestCase.test_case body'] = {
    'department': 'HR',
    'email': 'email0',
    'employee_id': '0',
    'first_name': 'first_name0',
    'job_role': 'MANAGER',
    'joining_date': '2023-02-20 00:00:00',
    'last_name': 'first_name0',
    'phone_number': 'first_name0'
}
