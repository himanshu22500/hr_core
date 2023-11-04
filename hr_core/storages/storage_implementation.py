import datetime
from typing import Optional, List, Dict

from django.db.models import Count, Q, F, Prefetch

from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.storage_interfaces.dtos import AttendanceDto
from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDto
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDto
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDto
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDto
from hr_core.constants.enums import AttendanceStatusType
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.exceptions.custom_exceptions import InvalidMoth
from hr_core.exceptions.custom_exceptions import InvalidYear
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedOut
from hr_core.constants.enums import AttendanceStatusType
from datetime import date
from django.db.models import Q
from hr_core.constants.enums import AttendanceStatusType


class StorageImplementation(StorageInterface):

    def get_attendance_data_for_month_year_employee(self, month: int,
                                                    year: int, employee_id: str) -> List[AttendanceDto]:
        self._mark_single_punch_absent(month=month, year=year, employee_id=employee_id)
        attendance_data_list = list(Attendance.objects.filter(
            Q(employee__employee_id=employee_id) &
            Q(clock_in_datetime__date__year=year) &
            Q(clock_in_datetime__date__month=month)
        ).values('clock_in_datetime', 'clock_out_datetime', 'status', 'id'))

        attendance_data_list_dto = self._convert_attendance_list_object_to_dto(attendance_data_list)
        return attendance_data_list_dto

    def _mark_single_punch_absent(self, month: int, year: int, employee_id: str) -> None:
        # Updating all values which is
        # Not today and
        # Not Clockout is none and
        # Status is marked PRESENT

        today = date.today()
        Attendance.objects.filter(
            ~Q(clock_in_datetime__date=today) & Q(clock_out_datetime=None) & Q(
                status=AttendanceStatusType.PRESENT.value)).update(
            status=AttendanceStatusType.SINGLE_PUNCH_ABSENT.value)

    @staticmethod
    def _convert_attendance_list_object_to_dto(attendance_object_list: List[Dict]) -> List[AttendanceDto]:
        attendance_dto_list = []
        for attendance_object in attendance_object_list:
            attendance_dto = AttendanceDto(
                attendance_id=attendance_object['id'],
                clock_in_date_time=attendance_object['clock_in_datetime'],
                clock_out_date_time=attendance_object['clock_out_datetime'],
                status=attendance_object['status']
            )
            attendance_dto_list.append(attendance_dto)
        return attendance_dto_list

    @staticmethod
    def _create_clock_in_attendance(employee_id: str) -> Attendance:
        employee = Employee.objects.get(employee_id=employee_id)
        attendance_entry = Attendance(employee=employee, clock_in_datetime=datetime.datetime.now(),
                                      clock_out_datetime=None, status=AttendanceStatusType.PRESENT.value)
        attendance_entry.save()
        return attendance_entry

    @staticmethod
    def _create_clock_out_attendance(employee_id: str) -> Attendance:
        today = date.today()
        attendance_entry = Attendance.objects.get(
            Q(employee__employee_id=employee_id) & Q(clock_in_datetime__date=today))
        attendance_entry.clock_out_datetime = datetime.datetime.now()
        attendance_entry.save()
        return attendance_entry

    @staticmethod
    def _convert_attendance_object_to_clock_in_dto(attendance: Attendance) -> ClockInAttendanceDto:
        clock_in_dto = ClockInAttendanceDto(attendance_id=attendance.pk,
                                            clock_in_date_time=attendance.clock_in_datetime)
        return clock_in_dto

    def create_and_get_clockin_attendance(self, employee_id: str) -> ClockInAttendanceDto:
        # TODO: try to avoid private methods in storage layer which involves model data modification code
        attendance_entry = self._create_clock_in_attendance(employee_id=employee_id)
        clock_in_attendance_dto = self._convert_attendance_object_to_clock_in_dto(attendance=attendance_entry)
        return clock_in_attendance_dto

    @staticmethod
    def _convert_attendance_object_to_clock_out_dto(attendance: Attendance) -> ClockOutAttendanceDto:
        clock_out_dto = ClockOutAttendanceDto(attendance_id=attendance.pk,
                                              clock_out_date_time=attendance.clock_out_datetime)
        return clock_out_dto

    def create_and_get_clockout_attendance(self, employee_id: str) -> ClockOutAttendanceDto:
        attendance_entry = self._create_clock_out_attendance(employee_id=employee_id)
        clock_out_attendance_dto = self._convert_attendance_object_to_clock_out_dto(attendance=attendance_entry)
        return clock_out_attendance_dto

    def validate_already_not_clocked_in(self, employee_id: str):
        today = date.today()
        # TODO: we should include clocked in datetime not null filter as well in below query
        #  because, when somehow we have an entry in attendance model with all as null values, then this code breaks
        is_entry_for_today_exist = Attendance.objects.filter(
            Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id)).exists()
        if is_entry_for_today_exist:
            raise EmployeeAlreadyClockedIn

    def validate_already_clocked_in(self, employee_id: str):
        today = date.today()
        # TODO: we should include clocked in datetime null filter as well in below query
        is_entry_for_today_exist = Attendance.objects.filter(
            Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id)).exists()

        no_entry_for_today = not is_entry_for_today_exist
        if no_entry_for_today:
            raise EmployeeNotClockedIn

    def validate_month(self, month: int) -> None:
        is_month_valid = 1 <= month <= 12
        is_month_not_valid = not is_month_valid

        if is_month_not_valid:
            raise InvalidMoth

    def validate_year(self, year: int) -> None:
        current_year = date.today().year
        is_year_valid = year <= current_year
        is_year_not_valid = not is_year_valid

        if is_year_not_valid:
            raise InvalidYear

    def get_full_month_stats(self, employee_id: str, month: int, year: int) -> FullMothStatsDto:
        # TODO: module level imports must be global imports
        import calendar
        # assuming all days are working days in a month
        total_working_days = calendar.monthrange(year=year, month=month)[1]

        # TODO: better to have this as separate storage method
        total_present_days = Attendance.objects.filter(
            Q(employee__employee_id=employee_id) & Q(status=AttendanceStatusType.PRESENT.value) & Q(
                clock_in_datetime__date__year=year) & Q(clock_in_datetime__date__month=month)).count()

        # TODO: better to have this as separate storage method
        total_absent_days = Attendance.objects.filter(
            Q(employee__employee_id=employee_id) & Q(status=AttendanceStatusType.ABSENT.value) & Q(
                clock_in_datetime__date__year=year) & Q(clock_in_datetime__date__month=month)).count()

        # TODO: this method has too much responsibility for a storage method,
        #  because if we are asked to add single punch absents, then also we need to change this method
        #  and this leaves the most of logic to storage which makes the interactor dry
        full_month_stats_dto = FullMothStatsDto(
            total_working_days=total_working_days, total_present_days=total_present_days,
            total_absent_days=total_absent_days
        )
        return full_month_stats_dto

    def validate_already_not_clocked_out(self, employee_id: str) -> None:
        today = date.today()
        attendance_object = Attendance.objects.get(
            Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id))

        already_clocked_out = attendance_object.clock_out_datetime != None
        if already_clocked_out:
            raise EmployeeAlreadyClockedOut

    @staticmethod
    def _convert_employee_object_to_dto(employee: Employee):
        employee_dto = EmployeeDetailsDto(
            employee_id=employee.employee_id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            phone_number=employee.phone_number,
            job_role=employee.job_role,
            department=employee.department,
            joining_date=employee.joining_date
        )
        return employee_dto

    def get_employee(self, employee_id: str) -> EmployeeDetailsDto:
        employee = Employee.objects.get(employee_id=employee_id)
        # TODO: kwargs should be used
        employee_dto = self._convert_employee_object_to_dto(employee)
        return employee_dto

    def validate_employee_id(self, employee_id: str):
        is_valid_employee_id = Employee.objects.filter(employee_id=employee_id).exists()
        is_invalid_employee_id = not is_valid_employee_id

        if is_invalid_employee_id:
            raise InvalidEmployeeId
