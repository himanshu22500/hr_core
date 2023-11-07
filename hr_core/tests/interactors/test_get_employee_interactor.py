import pytest
from mock import create_autospec
from mock.mock import Mock

from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.get_employee_interactor import GetEmployeeInteractor
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId


class TestGetEmployeeInteractor:

    def test_get_employee_with_invalid_employee_id_raises_exception(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetEmployeeInteractor(storage=storage)
        storage.validate_employee_id.side_effect = InvalidEmployeeId("Invalid")

        # Act

        # Assert
        with pytest.raises(InvalidEmployeeId):
            interactor.get_employee(employee_id="Invalid")

    def test_get_employee_with_valid_input_returns_employee_details_dto(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetEmployeeInteractor(storage=storage)
        storage_get_employee_return_value = Mock()
        storage.get_employee.return_value = storage_get_employee_return_value

        # Act
        employee_details = interactor.get_employee(employee_id="1")

        # Assert
        assert employee_details == storage_get_employee_return_value

    def test_get_employee_wrapper_for_bad_request(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetEmployeeInteractor(storage=storage)
        storage.validate_employee_id.side_effect = InvalidEmployeeId("Invalid")
        raise_exception_return_value = Mock()
        presenter.raise_exception_for_invalid_employee.return_value = raise_exception_return_value

        # Act
        bad_request_response = interactor.get_employee_wrapper(employee_id="Invalid", presenter=presenter)

        # Assert
        assert bad_request_response == raise_exception_return_value

    def test_get_employee_wrapper_for_valid_request_success_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetEmployeeInteractor(storage=storage)
        return_value_get_employee_response = Mock()
        presenter.get_response_for_get_employee.return_value = return_value_get_employee_response

        # Act
        success_response = interactor.get_employee_wrapper(employee_id="valid", presenter=presenter)

        # Assert
        assert success_response == return_value_get_employee_response
