# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFullMonthStatsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetFullMonthStatsAPITestCase.test_case body'] = {
    'total_absent_days': 0,
    'total_present_days': 0,
    'total_single_punch_in_days': 0,
    'total_working_days': 31
}
