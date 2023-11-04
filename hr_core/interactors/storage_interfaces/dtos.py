from dataclasses import dataclass
import datetime


@dataclass
class ClockInAttendanceDto:
    attendance_id: str
    clock_in_date_time: datetime.datetime


@dataclass
class ClockOutAttendanceDto:
    attendance_id: str
    clock_out_date_time: datetime.datetime


# TODO: Actually our dto naming convention is a little bit different,
# TODO: we will have DTO suffix instead of Dto
@dataclass
class EmployeeDetailsDto:
    employee_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    job_role: str
    department: str
    joining_date: datetime.datetime


@dataclass
class AttendanceDto:
    attendance_id: str
    clock_in_date_time: datetime.datetime
    clock_out_date_time: datetime.datetime
    status: str


@dataclass
class FullMothStatsDto:
    total_working_days: int
    total_present_days: int
    total_absent_days: int
    total_single_punch_in_days: int
