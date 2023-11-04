from abc import abstractmethod
from typing import List
from hr_core.interactors.storage_interfaces.storage_interface import EmployeeDetailsDTO
from hr_core.interactors.storage_interfaces.storage_interface import ClockInAttendanceDTO
from hr_core.interactors.storage_interfaces.storage_interface import ClockOutAttendanceDTO
from hr_core.interactors.storage_interfaces.storage_interface import FullMothStatsDTO
from hr_core.interactors.storage_interfaces.storage_interface import AttendanceDTO

from django.http import HttpResponse


class PresenterInterface:
    @abstractmethod
    def get_response_for_get_employee(self, employee_details_dto: EmployeeDetailsDTO) -> HttpResponse:
        pass

    # TODO: missed abstractmethod decorator
    def get_response_for_get_attendance_data(self, attendance_dto_list: List[AttendanceDTO]) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_employee(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_mark_clock_in_response(self, clock_in_attendance_dto: ClockInAttendanceDTO) -> HttpResponse:
        pass

    @abstractmethod
    def get_mark_clock_out_response(self, clock_out_attendance_dto: ClockOutAttendanceDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_employee_already_clocked_in(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_employee_already_clocked_out(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_employee_not_clocked_in(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_month(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_year(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_response_for_get_full_month_stats(self, full_month_stats_dto: FullMothStatsDTO) -> HttpResponse:
        pass
