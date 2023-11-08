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


@pytest.fixture()
def create_employees():
    employees = [
        {
            "user_id": None,
            "employee_id": "1",
            "first_name": "Himanshu",
            "last_name": "Mishra",
            "email": "h@gmail.com",
            "phone_number": "8172932823",
            "job_role": JobRoleType.JUNIOR_ENGINEER.value,
            "department": DepartmentType.ENGINEERING.value,
            "joining_date": datetime.now()
        }
    ]

    for employee in employees:
        Employee.objects.create(
            user_id=employee['user_id'],
            employee_id=employee['employee_id'],
            first_name=employee['first_name'],
            last_name=employee['last_name'],
            email=employee['email'],
            phone_number=employee['phone_number'],
            job_role=employee['job_role'],
            department=employee['department'],
            joining_date=employee['joining_date']
        )


@pytest.fixture()
def create_clock_in_attendance(create_employees):
    attendances = [
        {
            "employee_id": "1",
            "clock_in_datetime": datetime.now(),
            "clock_out_datetime": None,
            "status": AttendanceStatusType.PRESENT.value
        }
    ]

    for attendance in attendances:
        employee_obj = Employee.objects.get(employee_id=attendance['employee_id'])
        Attendance.objects.create(
            employee=employee_obj,
            clock_in_datetime=attendance['clock_in_datetime'],
            clock_out_datetime=attendance['clock_out_datetime'],
            status=attendance['status']
        )


@pytest.fixture()
def create_clock_out_attendance(create_employees):
    attendances = [
        {
            "employee_id": "1",
            "clock_in_datetime": datetime.now(),
            "clock_out_datetime": datetime.now() + timedelta(hours=9),
            "status": AttendanceStatusType.PRESENT.value
        }
    ]

    for attendance in attendances:
        employee_obj = Employee.objects.get(employee_id=attendance['employee_id'])
        Attendance.objects.create(
            employee=employee_obj,
            clock_in_datetime=attendance['clock_in_datetime'],
            clock_out_datetime=attendance['clock_out_datetime'],
            status=attendance['status']
        )


@pytest.fixture()
def create_single_punch_in_attendance(create_employees):
    attendances = [
        {
            "employee_id": "1",
            "clock_in_datetime": datetime.now() - timedelta(hours=24),
            "clock_out_datetime": None,
            "status": AttendanceStatusType.SINGLE_PUNCH_ABSENT.value
        }
    ]

    for attendance in attendances:
        employee_obj = Employee.objects.get(employee_id=attendance['employee_id'])
        Attendance.objects.create(
            employee=employee_obj,
            clock_in_datetime=attendance['clock_in_datetime'],
            clock_out_datetime=attendance['clock_out_datetime'],
            status=attendance['status']
        )


@pytest.fixture()
def employee_details_dtos():
    employee_details_dtos = [
        EmployeeDetailsDTO(
            employee_id="1",
            first_name="Himanshu",
            last_name="Mishra",
            email="himanshu22500@gmail.com",
            phone_number="8172932823",
            job_role=JobRoleType.JUNIOR_ENGINEER.value,
            department=DepartmentType.ENGINEERING.value,
            joining_date=datetime.now()
        )
    ]
    return employee_details_dtos


@pytest.fixture()
def attendance_dtos():
    attendance_dtos = [
        AttendanceDTO(
            attendance_id="1",
            clock_in_date_time=datetime.now(),
            clock_out_date_time=datetime.now() + timedelta(hours=9),
            status=AttendanceStatusType.PRESENT.value
        )
    ]
    return attendance_dtos
