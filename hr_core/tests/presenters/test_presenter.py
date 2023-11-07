import pytest
import json

from hr_core.presenters.presenter_implementation import PresenterImplementation


class TestPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_get_mark_clock_in_response(self, snapshot, presenter, attendance_dto, clock_in_attendance_dto):
        # Arrange
        actual_response = presenter.get_mark_clock_in_response(clock_in_attendance_dto)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "1")

    def test_get_response_for_get_attendance_data(self, snapshot, presenter, attendance_dtos):
        # Arrange
        actual_response = presenter.get_response_for_get_attendance_data(attendance_dtos)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "2")

    def test_raise_exception_for_employee_already_clocked_in(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_employee_already_clocked_in()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "3")

    def test_raise_exception_for_employee_already_clocked_out(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_employee_already_clocked_out()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "4")

    def test_raise_exception_for_invalid_month(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_invalid_month()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID MONTH")

    def test_raise_exception_for_invalid_year(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_invalid_year()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_YEAR")

    def test_get_response_for_get_full_month_stats(self, snapshot, presenter, full_month_stats_dto):
        # Arrange
        actual_response = presenter.get_response_for_get_full_month_stats(full_month_stats_dto=full_month_stats_dto)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Full month Stats success response")

    def test_raise_exception_for_employee_not_clocked_in(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_employee_not_clocked_in()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Employee Not Clocked In")

    def test_get_response_for_get_employee(self, snapshot, presenter, employee_details_dto):
        # Arrange
        actual_response = presenter.get_response_for_get_employee(employee_details_dto=employee_details_dto)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Employee details response")

    def test_get_mark_clock_out_response(self, snapshot, presenter, clock_out_attendance_dto):
        # Arrange
        actual_response = presenter.get_mark_clock_out_response(clock_out_attendance_dto=clock_out_attendance_dto)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Clock Out Response")

    def test_raise_exception_for_invalid_employee(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_invalid_employee()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Invalid Employee id Response")
