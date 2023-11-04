from typing import Dict

from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from django.http import HttpResponse
from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDto


class GetEmployeeInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_employee_wrapper(self, employee_id: str, presenter: PresenterInterface) -> HttpResponse:
        try:
            employee_details_dto = self.get_employee(employee_id=employee_id)
        except InvalidEmployeeId:
            return presenter.raise_exception_for_invalid_employee()

        return presenter.get_response_for_get_employee(
            employee_details_dto=employee_details_dto)

    def get_employee(self, employee_id: str, ) -> EmployeeDetailsDto:
        self.storage.validate_employee_id(employee_id=employee_id)
        employee_details_dto = \
            self.storage.get_employee(employee_id=employee_id)
        return employee_details_dto
