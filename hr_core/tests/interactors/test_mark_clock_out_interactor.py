import pytest
from mock import create_autospec
from mock.mock import Mock
from calendar import monthrange
from datetime import datetime

from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.mark_clock_out_interactor import MarkClockOutInteractor
from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedOut
from hr_core.tests.factories.storage_dtos import ClockOutAttendanceDTOFactory


class TestMarkClockOutInteractor:
    def test_mark_clock_out_with_employee_already_clocked_out(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockOutInteractor(storage=storage)

        storage.validate_already_not_clocked_out.side_effect = EmployeeAlreadyClockedOut(employee_id="1",
                                                                                         clock_out_datetime=datetime.now())

        # Act

        # Assert
        with pytest.raises(EmployeeAlreadyClockedOut):
            interactor.mark_clock_out(employee_id="1")

    def test_mark_clock_out_with_employee_already_not_clocked_out_returns_dto(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockOutInteractor(storage=storage)

        storage_clock_out_object = ClockOutAttendanceDTOFactory()
        storage.create_and_get_clockout_attendance.return_value = storage_clock_out_object

        # Act
        clock_out_dto = interactor.mark_clock_out(employee_id="1")

        # Assert
        assert clock_out_dto == storage_clock_out_object

    def test_mark_clock_in_wrapper_with_already_clocked_in_bad_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockOutInteractor(storage=storage)

        storage.validate_already_not_clocked_out.side_effect = EmployeeAlreadyClockedOut(employee_id="1",
                                                                                         clock_out_datetime=datetime.now())
        already_clocked_out_response = Mock()
        presenter.raise_exception_for_employee_already_clocked_out.return_value = already_clocked_out_response

        # Act
        bad_response = interactor.mark_clock_out_wrapper(employee_id="1", presenter=presenter)

        # Assert
        assert bad_response == already_clocked_out_response

    def test_mark_clock_out_wrapper_with_success_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockOutInteractor(storage=storage)

        clock_out_success_response = Mock()
        presenter.get_mark_clock_out_response.return_value = clock_out_success_response

        # Act
        clock_out_response = interactor.mark_clock_out_wrapper(employee_id="1", presenter=presenter)

        # Assert
        assert clock_out_response == clock_out_success_response
