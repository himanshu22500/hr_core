from typing import Optional
from dataclasses import dataclass
import datetime


@dataclass
class ClockInAttendanceDTO:
    attendance_id: str
    clock_in_date_time: datetime.datetime


@dataclass
class ClockOutAttendanceDTO:
    attendance_id: str
    clock_out_date_time: datetime.datetime


@dataclass
class EmployeeDetailsDTO:
    employee_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    job_role: str
    department: str
    joining_date: datetime.datetime


@dataclass
class AttendanceDTO:
    attendance_id: str
    clock_in_date_time: datetime.datetime
    clock_out_date_time: datetime.datetime
    status: str


@dataclass
class FullMothStatsDTO:
    total_working_days: int
    total_present_days: int
    total_absent_days: int
    total_single_punch_in_days: int


@dataclass
class AttendanceParamDTO:
    month: int
    year: int
    employee_id: str
