# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAttendanceDataAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetAttendanceDataAPITestCase.test_case body'] = {
    'attendance_data': [
        {
            'clock_in_date_time': '2023-10-20 00:00:00',
            'clock_out_date_time': '2023-10-20 00:00:00',
            'status': 'PRESENT'
        }
    ]
}
