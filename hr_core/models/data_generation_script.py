from typing import List, Dict
from pprint import pprint
from faker import Faker
# from hr_core.constants.enums import JobRoleType
# from hr_core.constants.enums import DepartmentType
# from hr_core.constants.enums import AttendanceStatusType
import calendar

from enum import Enum


class JobRoleType(Enum):
    MANAGER = "MANAGER"
    JUNIOR_ENGINEER = "JUNIOR_ENGINEER"
    SENIOR_ENGINEER = "SENIOR_ENGINEER"


class DepartmentType(Enum):
    HR = "HR"
    ENGINEERING = "ENGINEERING"


class AttendanceStatusType(Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    HOLIDAY = "HOLIDAY"
    SINGLE_PUNCH_ABSENT = "SINGLE_PUNCH_ABSENT"


class StatusCode(Enum):
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    SUCCESS = 200
    SUCCESS_CREATE = 201


import random

fake = Faker()

job_roles = [role.value for role in JobRoleType]
departments = [department.value for department in DepartmentType]
from datetime import datetime

joining_year = [2023, 2022]
valid_months = [i for i in range(1, 13)]
valid_dates = [i for i in range(1, 20)]
valid_status = [status.value for status in AttendanceStatusType]
valid_working_hours = [hour for hour in range(9, 18)]


def get_employee_details_list() -> List[Dict]:
    employees_details_list = []
    for i in range(2, 7):
        employees_details = {
            "employee_id": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "job_role": random.choice(job_roles),
            "department": random.choice(departments),
            "joining_date": datetime(random.choice(joining_year), random.choice(valid_months),
                                     random.choice(valid_dates))
        }
        employees_details_list.append(employees_details)

    return employees_details_list


def get_attendance_data_for_employee(employee_details: Dict) -> List[Dict]:
    employee_id = employee_details['employee_id']
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    joining_year = employee_details['joining_date'].year
    joining_month = employee_details['joining_date'].month
    joining_day = employee_details['joining_date'].day

    attendance_data_list = []

    for year in range(joining_year, current_year):
        for month in valid_months:
            total_working_days = calendar.monthrange(year=year, month=month)[1]
            for day in range(1, total_working_days + 1):
                if year == joining_year and month < joining_month: continue
                if year == joining_year and month == joining_month and day < joining_day: continue
                status = random.choice(valid_status)
                if status == AttendanceStatusType.PRESENT.value:
                    attendance_this_date = {}
                    attendance_this_date['employee_id'] = employee_id
                    attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
                    attendance_this_date['clock_out_datetime'] = datetime(year=year, month=month, day=day,
                                                                          hour=random.choice(valid_working_hours))
                    attendance_this_date['status'] = status
                    attendance_data_list.append(attendance_this_date)
                elif status == AttendanceStatusType.SINGLE_PUNCH_ABSENT.value:
                    attendance_this_date = {}
                    attendance_this_date['employee_id'] = employee_id
                    attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
                    attendance_this_date['clock_out_datetime'] = None
                    attendance_this_date['status'] = status
                    attendance_data_list.append(attendance_this_date)

    # this year
    for month in range(1, current_month):
        year = current_year
        total_working_days = calendar.monthrange(year=year, month=month)[1]
        for day in range(1, total_working_days + 1):
            status = random.choice(valid_status)
            if status == AttendanceStatusType.PRESENT.value:
                attendance_this_date = {}
                attendance_this_date['employee_id'] = employee_id
                attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
                attendance_this_date['clock_out_datetime'] = datetime(year=year, month=month, day=day,
                                                                      hour=random.choice(valid_working_hours))
                attendance_this_date['status'] = status
                attendance_data_list.append(attendance_this_date)
            elif status == AttendanceStatusType.SINGLE_PUNCH_ABSENT.value:
                attendance_this_date = {}
                attendance_this_date['employee_id'] = employee_id
                attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
                attendance_this_date['clock_out_datetime'] = None
                attendance_this_date['status'] = status
                attendance_data_list.append(attendance_this_date)

    # This month
    for day in range(1, current_day):
        year = current_year
        month = current_month
        status = random.choice(valid_status)
        if status == AttendanceStatusType.PRESENT.value:
            attendance_this_date = {}
            attendance_this_date['employee_id'] = employee_id
            attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
            attendance_this_date['clock_out_datetime'] = datetime(year=year, month=month, day=day,
                                                                  hour=random.choice(valid_working_hours))
            attendance_this_date['status'] = status
            attendance_data_list.append(attendance_this_date)
        elif status == AttendanceStatusType.SINGLE_PUNCH_ABSENT.value:
            attendance_this_date = {}
            attendance_this_date['employee_id'] = employee_id
            attendance_this_date['clock_in_datetime'] = datetime(year=year, month=month, day=day, hour=9)
            attendance_this_date['clock_out_datetime'] = None
            attendance_this_date['status'] = status
            attendance_data_list.append(attendance_this_date)

    return attendance_data_list


employees_details = get_employee_details_list()
print("employees_details = ", end="")
pprint(employees_details)

attendance_data = []
for employee_details in employees_details:
    employee_attendance_data = get_attendance_data_for_employee(employee_details=employee_details)
    attendance_data.extend(employee_attendance_data)

print("attendance_data = ", end="")
pprint(attendance_data)
