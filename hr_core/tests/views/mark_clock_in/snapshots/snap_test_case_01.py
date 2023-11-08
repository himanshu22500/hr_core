# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01MarkClockInAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01MarkClockInAPITestCase.test_case body'] = {
    'attendance_id': '1',
    'clock_in_date_time': '2023-11-08 12:01:04.956179'
}
