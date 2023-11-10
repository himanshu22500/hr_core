import pytest

from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.storages.storage_implementation import StorageImplementation


class TestValidateAlreadyClockedIn:
    @pytest.mark.django_db
    def test_with_employee_not_clocked_in_today_raises_exception(self):
        # Arrange
        sql_storage = StorageImplementation()

        # Assert
        with pytest.raises(EmployeeNotClockedIn):
            sql_storage.validate_already_clocked_in(employee_id="1")
