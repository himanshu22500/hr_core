from abc import abstractmethod
from typing import List
from hr_core.interactors.storage_interfaces.storage_interface import EmployeeDetailsDto
from hr_core.interactors.storage_interfaces.storage_interface import ClockInAttendanceDto
from hr_core.interactors.storage_interfaces.storage_interface import ClockOutAttendanceDto
from hr_core.interactors.storage_interfaces.storage_interface import FullMothStatsDto
from hr_core.interactors.storage_interfaces.storage_interface import AttendanceDto

from django.http import HttpResponse


class PresenterInterface:
    @abstractmethod
    def get_response_for_get_employee(self, employee_details_dto: EmployeeDetailsDto) -> HttpResponse:
        pass

    def get_response_for_get_attendance_data(self, attendance_dto_list: List[AttendanceDto]) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_employee(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_mark_clock_in_response(self, clock_in_attendance_dto: ClockInAttendanceDto) -> HttpResponse:
        pass

    @abstractmethod
    def get_mark_clock_out_response(self, clock_out_attendance_dto: ClockOutAttendanceDto) -> HttpResponse:
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
    def get_response_for_get_full_month_stats(self, full_month_stats_dto: FullMothStatsDto) -> HttpResponse:
        pass
