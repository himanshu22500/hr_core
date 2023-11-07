import pytest
from mock import create_autospec
from mock.mock import Mock

from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.get_attendance_data_interactor import GetAttendanceDataInteractor
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.exceptions.custom_exceptions import InvalidMonth
from hr_core.exceptions.custom_exceptions import InvalidYear
from hr_core.interactors.storage_interfaces.dtos import AttendanceParamDTO
from hr_core.tests.factories.storage_dtos import AttendanceDTOFactory


class TestGetAttendanceDataInteractor:

    def test_get_attendance_data_with_invalid_month_raises_exception(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        attendance_params = AttendanceParamDTO(
            month=13,
            year=2023,
            employee_id="1"
        )

        # Act

        # Assert
        with pytest.raises(InvalidMonth):
            interactor.get_attendance_data(attendance_params=attendance_params)

    def test_get_attendance_data_with_invalid_year_raises_exception(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)
        attendance_params = AttendanceParamDTO(month=12, year=2024, employee_id="1")

        # Act

        # Assert
        with pytest.raises(InvalidYear):
            interactor.get_attendance_data(attendance_params=attendance_params)

    def test_get_attendance_data_invalid_employee_id(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        attendance_params = AttendanceParamDTO(
            month=12,
            year=2023,
            employee_id="Invalid"
        )

        storage.validate_employee_id.side_effect = InvalidEmployeeId("Invalid")
        # Act

        # Assert
        with pytest.raises(InvalidEmployeeId):
            interactor.get_attendance_data(attendance_params=attendance_params)

    def test_get_attendance_data_with_valid_params(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        attendance_params = AttendanceParamDTO(
            month=10,
            year=2023,
            employee_id="valid"
        )

        storage_attendance_data_response = AttendanceDTOFactory()
        storage.get_attendance_data_for_month_year_dto.return_value = storage_attendance_data_response

        get_attendance_return_value = interactor.get_attendance_data(attendance_params=attendance_params)
        # Act

        # Assert
        assert get_attendance_return_value == storage_attendance_data_response

    def test_get_attendance_data_wrapper_for_invalid_employee_id_bad_request(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        storage.validate_employee_id.side_effect = InvalidEmployeeId("Invalid")
        raise_exception_return_value = Mock()
        presenter.raise_exception_for_invalid_employee.return_value = raise_exception_return_value
        attendance_params = AttendanceParamDTO(
            month=10,
            year=2023,
            employee_id="Invalid"
        )

        # Act
        bad_request_response = interactor.get_attendance_data_wrapper(attendance_params=attendance_params,
                                                                      presenter=presenter)
        # Assert
        assert bad_request_response == raise_exception_return_value

    def test_get_attendance_data_wrapper_for_invalid_month_bad_request(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        raise_exception_return_value = Mock()
        presenter.raise_exception_for_invalid_month.return_value = raise_exception_return_value
        attendance_params = AttendanceParamDTO(
            month=13,
            year=2023,
            employee_id="valid"
        )

        # Act
        bad_request_response = interactor.get_attendance_data_wrapper(attendance_params=attendance_params,
                                                                      presenter=presenter)
        # Assert
        assert bad_request_response == raise_exception_return_value

    def test_get_attendance_data_wrapper_for_invalid_year_bad_request(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        raise_exception_return_value = Mock()
        presenter.raise_exception_for_invalid_year.return_value = raise_exception_return_value
        attendance_params = AttendanceParamDTO(
            month=12,
            year=2024,
            employee_id="valid"
        )

        # Act
        bad_request_response = interactor.get_attendance_data_wrapper(attendance_params=attendance_params,
                                                                      presenter=presenter)
        # Assert
        assert bad_request_response == raise_exception_return_value

    def test_get_employee_wrapper_for_valid_request_success_response(self):
        # Arrange
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetAttendanceDataInteractor(storage=storage)

        return_value_get_attendance = Mock()
        presenter.get_response_for_get_attendance_data.return_value = return_value_get_attendance
        attendance_params = AttendanceParamDTO(
            month=12,
            year=2023,
            employee_id="valid"
        )

        # Act
        success_response = interactor.get_attendance_data_wrapper(attendance_params=attendance_params,
                                                                  presenter=presenter)
        # Assert
        assert success_response == return_value_get_attendance
