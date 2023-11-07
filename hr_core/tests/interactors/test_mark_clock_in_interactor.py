import pytest
from mock import create_autospec
from mock.mock import Mock
from calendar import monthrange
from datetime import datetime

from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.mark_clock_in_interactor import MarkClockInInteractor
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedIn
from hr_core.tests.factories.storage_dtos import ClockInAttendanceDTOFactory


class TestMarkClockInInteractor:
    def test_mark_clock_in_with_employee_clocked_in_raises_exception(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockInInteractor(storage=storage)

        storage.validate_already_not_clocked_in.side_effect = EmployeeAlreadyClockedIn(employee_id="1",
                                                                                       clock_in_datetime=datetime.now())

        # Act

        # Assert
        with pytest.raises(EmployeeAlreadyClockedIn):
            interactor.mark_clock_in(employee_id="1")

    def test_mark_clock_in_employee_already_not_clocked_in_returns_dto(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockInInteractor(storage=storage)

        storage_clock_in_object = ClockInAttendanceDTOFactory()
        storage.create_and_get_clockin_attendance.return_value = storage_clock_in_object

        # Act
        clock_in_dto = interactor.mark_clock_in(employee_id="1")

        # Assert
        assert clock_in_dto == storage_clock_in_object

    def test_mark_clock_in_wrapper_with_already_clocked_in_bad_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockInInteractor(storage=storage)

        storage.validate_already_not_clocked_in.side_effect = EmployeeAlreadyClockedIn(employee_id="1",
                                                                                       clock_in_datetime=datetime.now())
        already_clocked_in_response = Mock()
        presenter.raise_exception_for_employee_already_clocked_in.return_value = already_clocked_in_response

        # Act
        bad_response = interactor.mark_clock_in_wrapper(employee_id="1", presenter=presenter)

        # Assert
        assert bad_response == already_clocked_in_response

    def test_mark_clock_in_wrapper_with_success_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MarkClockInInteractor(storage=storage)

        clock_in_success_response = Mock()
        presenter.get_mark_clock_in_response.return_value = clock_in_success_response

        # Act
        clock_in_response = interactor.mark_clock_in_wrapper(employee_id="1", presenter=presenter)

        # Assert
        assert clock_in_response == clock_in_success_response
