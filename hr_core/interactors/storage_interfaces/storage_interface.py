from abc import abstractmethod
from typing import List
from hr_core.interactors.storage_interfaces.dtos import AttendanceDto
from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDto
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDto
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDto
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDto


class StorageInterface:

    @abstractmethod
    def get_attendance_data_for_month_year_employee(self, month: int,
                                                    year: int, employee_id: str) -> List[AttendanceDto]:
        pass

    @abstractmethod
    def get_employee(self, employee_id: str) -> EmployeeDetailsDto:
        pass

    @abstractmethod
    def get_total_present_days_month(self, employee_id: str, month: int, year: int) -> int:
        pass

    @abstractmethod
    def get_total_absent_days_month(self, employee_id: str, month: int, year: int) -> int:
        pass

    @abstractmethod
    def get_single_punch_in_days_month(self, employee_id: str, month: int, year: int) -> int:
        pass

    def get_total_working_days_month(self, month: int, year: int) -> int:
        from calendar import monthrange
        return monthrange(year=year, month=month)[1]

    @abstractmethod
    def validate_employee_id(self, employee_id: str) -> None:
        pass

    @abstractmethod
    def validate_month(self, month: int) -> None:
        pass

    @abstractmethod
    def validate_year(self, year: int) -> None:
        pass

    @abstractmethod
    def create_and_get_clockin_attendance(self, employee_id: str) -> ClockInAttendanceDto:
        pass

    @abstractmethod
    def create_and_get_clockout_attendance(self, employee_id: str) -> ClockOutAttendanceDto:
        pass

    @abstractmethod
    def validate_already_not_clocked_in(self, employee_id: str) -> None:
        pass

    @abstractmethod
    def validate_already_not_clocked_out(self, employee_id: str) -> None:
        pass

    @abstractmethod
    def validate_already_clocked_in(self, employee_id: str) -> None:
        pass
