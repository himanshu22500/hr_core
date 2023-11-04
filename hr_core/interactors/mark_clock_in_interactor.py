from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedIn
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO


class MarkClockInInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def mark_clock_in_wrapper(self, employee_id, presenter: PresenterInterface):
        try:
            clock_in_attendance_dto = self.mark_clock_in(employee_id=employee_id)
        except EmployeeAlreadyClockedIn:
            return presenter.raise_exception_for_employee_already_clocked_in()

        return presenter.get_mark_clock_in_response(clock_in_attendance_dto=clock_in_attendance_dto)

    def mark_clock_in(self, employee_id: str) -> ClockInAttendanceDTO:
        self.storage.validate_already_not_clocked_in(employee_id=employee_id)

        clock_in_attendance_dto = self.storage.create_and_get_clockin_attendance(employee_id=employee_id)
        return clock_in_attendance_dto
