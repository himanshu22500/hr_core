from abc import abstractmethod
from typing import List
from hr_core.interactors.storage_interfaces.dtos import AttendanceDTO, AttendanceParamDTO
from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDTO
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDTO
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDTO


class StorageInterface:

    @abstractmethod
    def get_attendance_data_for_month_year_dto(self, attendance_params: AttendanceParamDTO) -> List[AttendanceDTO]:
        pass

    @abstractmethod
    def get_employee(self, employee_id: str) -> EmployeeDetailsDTO:
        pass

    @abstractmethod
    def get_total_present_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        pass

    @abstractmethod
    def get_total_absent_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        pass

    @abstractmethod
    def get_total_single_punch_in_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        pass

    @abstractmethod
    def get_total_working_days_month(self, month: int, year: int) -> int:
        pass

    @abstractmethod
    def validate_employee_id(self, employee_id: str) -> None:
        pass

    @abstractmethod
    def create_and_get_clockin_attendance(self, employee_id: str) -> ClockInAttendanceDTO:
        pass

    @abstractmethod
    def create_and_get_clockout_attendance(self, employee_id: str) -> ClockOutAttendanceDTO:
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
