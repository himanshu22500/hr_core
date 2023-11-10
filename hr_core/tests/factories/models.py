import datetime

import factory

from hr_core.constants.enums import AttendanceStatusType
from hr_core.constants.enums import DepartmentType
from hr_core.constants.enums import JobRoleType
from hr_core.models.attendance import Attendance
from hr_core.models.employee import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    employee_id = factory.sequence(lambda n: f"{n}")
    user_id = factory.sequence(lambda n: f"{n}")

    first_name = factory.sequence(lambda n: f"first_name{n}")
    last_name = factory.sequence(lambda n: f"first_name{n}")
    email = factory.sequence(lambda n: f"email{n}")
    phone_number = factory.sequence(lambda n: f"first_name{n}")
    joining_date = datetime.datetime.now()
    job_role = factory.Iterator([job_role.value for job_role in JobRoleType])
    department = factory.Iterator([department.value for department in DepartmentType])


class PresentAttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance

    employee = factory.SubFactory(EmployeeFactory)
    clock_in_datetime = factory.LazyFunction(datetime.datetime.now)
    clock_out_datetime = factory.LazyFunction(datetime.datetime.now)
    status = AttendanceStatusType.PRESENT.value


class ClockInAttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance

    employee = factory.SubFactory(EmployeeFactory)
    clock_in_datetime = factory.LazyFunction(datetime.datetime.now)
    clock_out_datetime = None
    status = AttendanceStatusType.PRESENT.value


class SinglePunchInAbsentAttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance

    employee = factory.SubFactory(EmployeeFactory)
    clock_in_datetime = factory.LazyFunction(datetime.datetime.now)
    clock_out_datetime = None
    status = AttendanceStatusType.SINGLE_PUNCH_ABSENT.value
