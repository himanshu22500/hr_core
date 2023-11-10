from datetime import datetime

import pytest
from freezegun import freeze_time

from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO
from hr_core.models import Attendance
from hr_core.storages.storage_implementation import StorageImplementation


class TestCreateAndGetClockInAttendance:
    @pytest.mark.django_db
    @freeze_time(str(datetime.now()))
    def test_create_and_get_clockin_attendance(self, create_employees):
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
        assert attendance_dto.clock_in_date_time == now
