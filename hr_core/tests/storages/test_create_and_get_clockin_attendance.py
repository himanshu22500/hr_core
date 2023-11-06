from datetime import datetime
import pytest

from hr_core.models import Attendance
from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO


@pytest.mark.django_db
def test_create_and_get_clockin_attendance(create_employees):
    # Arrange
    employee_id = "1"
    sql_storage = StorageImplementation()
    now = datetime.now()
    clock_in_attendance_dto = ClockInAttendanceDTO(attendance_id="1", clock_in_date_time=now)

    # Act
    attendance_dto = sql_storage.create_and_get_clockin_attendance(employee_id=employee_id)
    attendance_obj = Attendance.objects.get(id=attendance_dto.attendance_id)

    # Assert
    assert attendance_obj.clock_out_datetime == None
    assert attendance_obj.employee.employee_id == employee_id
    assert attendance_dto.attendance_id == attendance_obj.id
    assert attendance_dto.clock_in_date_time == attendance_obj.clock_in_datetime
    # assert attendance_dto.clock_in_date_time == now # How do i Do this find
