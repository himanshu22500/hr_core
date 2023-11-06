import pytest

from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_employee_id_given_invalid_employee_id_raises_exception():
    employee_id = "invalid"
    sql_storage = StorageImplementation()

    with pytest.raises(InvalidEmployeeId):
        sql_storage.validate_employee_id(employee_id=employee_id)
