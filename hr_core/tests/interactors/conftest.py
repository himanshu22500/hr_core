from datetime import datetime
from datetime import timedelta
import pytest
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance
from hr_core.constants.enums import JobRoleType
from hr_core.constants.enums import DepartmentType
from hr_core.constants.enums import AttendanceStatusType

from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDTO
from hr_core.interactors.storage_interfaces.dtos import AttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDTO


@pytest.fixture()
def employee_details_dto():
    return EmployeeDetailsDTO(
        employee_id="1",
        first_name="Himanshu",
        last_name="Mishra",
        email="himanshu22500@gmail.com",
        phone_number="8172932823",
        job_role=JobRoleType.JUNIOR_ENGINEER.value,
        department=DepartmentType.ENGINEERING.value,
        joining_date=datetime(1, 1, 1, 1, 0, 0, 0)
    )


@pytest.fixture()
def attendance_dto():
    return AttendanceDTO(
        attendance_id="1",
        clock_in_date_time=datetime(1, 1, 1, 1, 0, 0, 0),
        clock_out_date_time=datetime(1, 1, 1, 1, 0, 0, 0) + timedelta(hours=9),
        status=AttendanceStatusType.PRESENT.value
    )


@pytest.fixture()
def full_month_stats_dto():
    return FullMothStatsDTO(
        total_working_days=3,
        total_present_days=1,
        total_absent_days=1,
        total_single_punch_in_days=1
    )


@pytest.fixture()
def attendance_dtos():
    return [
        AttendanceDTO(
            attendance_id="1",
            clock_in_date_time=datetime(1, 1, 1, 1, 0, 0, 0),
            clock_out_date_time=datetime(1, 1, 1, 1, 0, 0, 0) + timedelta(hours=9),
            status=AttendanceStatusType.PRESENT.value
        )
    ]


@pytest.fixture()
def clock_in_attendance_dto():
    return ClockInAttendanceDTO(
        attendance_id="1",
        clock_in_date_time=datetime(1, 1, 1, 1, 0, 0, 0)
    )


@pytest.fixture()
def clock_out_attendance_dto():
    return ClockOutAttendanceDTO(
        attendance_id="1",
        clock_out_date_time=datetime(1, 1, 1, 1, 0, 0, 0)
    )
