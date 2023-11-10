import pytest

from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.storages.storage_implementation import StorageImplementation


class TestValidateEmployeeId:
    @pytest.mark.django_db
    def test_with_invalid_employee_id_raises_exception(self):
        employee_id = "invalid"
        sql_storage = StorageImplementation()

        with pytest.raises(InvalidEmployeeId):
            sql_storage.validate_employee_id(employee_id=employee_id)
