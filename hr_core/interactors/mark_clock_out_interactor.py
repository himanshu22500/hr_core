from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface, ClockInAttendanceDto
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDto
from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedOut
from django.http import HttpResponse


class MarkClockOutInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def mark_clock_out_wrapper(self, employee_id: str, presenter: PresenterInterface) -> HttpResponse:
        try:
            clock_out_attendance_dto = self.mark_clock_out(employee_id=employee_id)
        except EmployeeNotClockedIn:
            return presenter.raise_exception_for_employee_not_clocked_in()
        except EmployeeAlreadyClockedOut:
            return presenter.raise_exception_for_employee_already_clocked_out()

        return presenter.get_mark_clock_out_response(clock_out_attendance_dto)

    def mark_clock_out(self, employee_id: str) -> ClockOutAttendanceDto:
        self.storage.validate_already_clocked_in(employee_id=employee_id)
        self.storage.validate_already_not_clocked_out(employee_id=employee_id)

        clock_out_attendance_dto = self.storage.create_and_get_clockout_attendance(employee_id=employee_id)
        return clock_out_attendance_dto
