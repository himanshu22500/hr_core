import pytest

from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.models.employee import Employee
from hr_core.interactors.storage_interfaces.dtos import AttendanceParamDTO


@pytest.mark.django_db
def test_get_total_absent_days_month_with_no_clock_in_entry(create_employees):
    # Arrange
    sql_storage = StorageImplementation()
    employee_obj = Employee.objects.get(employee_id="1")
    attendance_param = AttendanceParamDTO(
        month=employee_obj.joining_date.month,
        year=employee_obj.joining_date.year,
        employee_id=employee_obj.employee_id
    )
    # Act
    # Assert

    assert sql_storage.get_total_absent_days_month(attendance_params=attendance_param) == 0
