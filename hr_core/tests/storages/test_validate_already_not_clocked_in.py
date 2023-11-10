import pytest

from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedIn
from hr_core.storages.storage_implementation import StorageImplementation


class TestValidateAlreadyNotClockedIn:
    @pytest.mark.django_db
    def test_with_employee_not_clocked_today_raises_exception(self, create_clock_in_attendance):
        # Arrange
        sql_storage = StorageImplementation()

        # Assert
        with pytest.raises(EmployeeAlreadyClockedIn):
            sql_storage.validate_already_not_clocked_in(employee_id="1")
