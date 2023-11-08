# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01MarkClockOutAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01MarkClockOutAPITestCase.test_case body'] = {
    'attendance_id': '1',
    'clock_out_date_time': '2023-11-08 12:05:52.368687'
}
