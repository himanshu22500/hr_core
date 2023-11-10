import pytest

from hr_core.models.employee import Employee
from hr_core.storages.storage_implementation import StorageImplementation


class TestGetEmployee:
    @pytest.mark.django_db
    def test_with_valid_employee_id_gives_employee_details_dto(self, create_employees):
        # Arrange
        employee_id = "1"
        sql_storage = StorageImplementation()
        employee_object = Employee.objects.get(employee_id=employee_id)

        # Act
        employee_details = sql_storage.get_employee(employee_id=employee_id)

        # Assert
        assert employee_details.employee_id == employee_object.employee_id
        assert employee_details.email == employee_object.email
        assert employee_details.department == employee_object.department
        assert employee_details.job_role == employee_object.job_role
        assert employee_details.first_name == employee_object.first_name
        assert employee_details.last_name == employee_object.last_name
        assert employee_details.joining_date == employee_object.joining_date
