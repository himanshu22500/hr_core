from datetime import datetime
import pytest

from hr_core.models.attendance import Attendance
from hr_core.models.employee import Employee
from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDTO
from hr_core.constants.enums import AttendanceStatusType


@pytest.mark.django_db
def test_create_and_get_clockout_attendance(create_employees):
    # Arrange
    sql_storage = StorageImplementation()
    employee_obj = Employee.objects.get(employee_id="1")
    Attendance.objects.create(
        employee=employee_obj,
        clock_in_datetime=datetime.now(),
        status=AttendanceStatusType.PRESENT.value
    )

    # Act
    attendance_dto = sql_storage.create_and_get_clockout_attendance(employee_id="1")
    attendance_obj = Attendance.objects.get(id=attendance_dto.attendance_id)

    # Assert
    # assert attendance_obj.clock_out_datetime == datetime.now() # Find how to do this
    assert attendance_obj.employee.employee_id == "1"
    assert attendance_dto.attendance_id == attendance_obj.id
    assert attendance_dto.clock_out_date_time == attendance_obj.clock_out_datetime
