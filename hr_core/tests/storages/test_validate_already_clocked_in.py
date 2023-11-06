import pytest

from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance
from hr_core.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_already_clocked_in_given_if_employee_not_clocked_in_today_raises_exception():
    # Arrange
    sql_storage = StorageImplementation()

    # Assert
    with pytest.raises(EmployeeNotClockedIn):
        sql_storage.validate_already_clocked_in(employee_id="1")
