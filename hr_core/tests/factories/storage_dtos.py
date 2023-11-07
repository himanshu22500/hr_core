import datetime

from hr_core.interactors.storage_interfaces.dtos import AttendanceDTO, ClockOutAttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDTO
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO
from hr_core.constants.enums import AttendanceStatusType
import factory


class AttendanceDTOFactory(factory.Factory):
    class Meta:
        model = AttendanceDTO

    attendance_id = "1"
    clock_in_date_time = datetime.datetime
    clock_out_date_time = datetime.datetime
    status = AttendanceStatusType.PRESENT.value


class FullMonthStatsDTOFactory(factory.Factory):
    class Meta:
        model = FullMothStatsDTO

    total_working_days = 1
    total_present_days = 1
    total_absent_days = 1
    total_single_punch_in_days = 1


class ClockOutAttendanceDTOFactory(factory.Factory):
    class Meta:
        model = ClockOutAttendanceDTO

    attendance_id = "1"
    clock_out_date_time = datetime.datetime.now()


class ClockInAttendanceDTOFactory(factory.Factory):
    class Meta:
        model = ClockInAttendanceDTO

    attendance_id = "1"
    clock_in_date_time = datetime.datetime.now()
