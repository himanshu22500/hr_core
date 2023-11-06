import datetime
from typing import List, Dict
from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.storage_interfaces.dtos import AttendanceDTO, AttendanceParamDTO
from hr_core.interactors.storage_interfaces.dtos import EmployeeDetailsDTO
from hr_core.interactors.storage_interfaces.dtos import ClockInAttendanceDTO
from hr_core.interactors.storage_interfaces.dtos import ClockOutAttendanceDTO
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance
from hr_core.exceptions.custom_exceptions import InvalidEmployeeId
from hr_core.exceptions.custom_exceptions import InvalidMoth
from hr_core.exceptions.custom_exceptions import InvalidYear
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeNotClockedIn
from hr_core.exceptions.custom_exceptions import EmployeeAlreadyClockedOut
from datetime import date
from django.db.models import Q
from hr_core.constants.enums import AttendanceStatusType


class StorageImplementation(StorageInterface):

    def get_employee(self, employee_id: str) -> EmployeeDetailsDTO:
        employee = Employee.objects.get(employee_id=employee_id)
        employee_dto = self._convert_employee_object_to_dto(employee=employee)
        return employee_dto

    def validate_employee_id(self, employee_id: str):
        is_valid_employee_id = Employee.objects.filter(employee_id=employee_id).exists()
        is_invalid_employee_id = not is_valid_employee_id

        if is_invalid_employee_id:
            raise InvalidEmployeeId(employee_id=employee_id)

    def get_attendance_data_for_month_year_dto(self, attendance_params: AttendanceParamDTO) -> List[AttendanceDTO]:
        self.mark_single_punch_absent()
        attendance_data_list = list(Attendance.objects.filter(
            Q(employee__employee_id=attendance_params.employee_id) &
            Q(clock_in_datetime__date__year=attendance_params.year) &
            Q(clock_in_datetime__date__month=attendance_params.month)
        ).values('clock_in_datetime', 'clock_out_datetime', 'status', 'id'))

        attendance_data_list_dto = self._convert_attendance_list_object_to_dto(attendance_data_list)
        return attendance_data_list_dto

    def create_and_get_clockin_attendance(self, employee_id: str) -> ClockInAttendanceDTO:
        employee = Employee.objects.get(employee_id=employee_id)
        attendance_entry = Attendance(employee=employee, clock_in_datetime=datetime.datetime.now(),
                                      clock_out_datetime=None, status=AttendanceStatusType.PRESENT.value)
        attendance_entry.save()
        clock_in_attendance_dto = self._convert_attendance_object_to_clock_in_dto(attendance=attendance_entry)
        return clock_in_attendance_dto

    def create_and_get_clockout_attendance(self, employee_id: str) -> ClockOutAttendanceDTO:
        today = date.today()
        attendance_entry = Attendance.objects.get(
            Q(employee__employee_id=employee_id) & Q(clock_in_datetime__date=today))
        attendance_entry.clock_out_datetime = datetime.datetime.now()
        attendance_entry.save()
        clock_out_attendance_dto = self._convert_attendance_object_to_clock_out_dto(attendance=attendance_entry)
        return clock_out_attendance_dto

    def validate_already_not_clocked_in(self, employee_id: str):
        today = date.today()
        try:
            attendance_object = Attendance.objects.get(
                Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id))
        except Attendance.DoesNotExist:
            pass
        else:
            raise EmployeeAlreadyClockedIn(employee_id=employee_id,
                                           clock_in_datetime=attendance_object.clock_in_datetime)

    def validate_already_clocked_in(self, employee_id: str):
        today = date.today()
        is_entry_for_today_exist = Attendance.objects.filter(
            Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id)).exists()

        no_entry_for_today = not is_entry_for_today_exist
        if no_entry_for_today:
            raise EmployeeNotClockedIn(employee_id=employee_id)

    def get_total_present_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        return Attendance.objects.filter(
            Q(employee__employee_id=attendance_params.employee_id) & Q(status=AttendanceStatusType.PRESENT.value) & Q(
                clock_in_datetime__date__year=attendance_params.year) & Q(
                clock_in_datetime__date__month=attendance_params.month)).count()

    def get_total_absent_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        return Attendance.objects.filter(
            Q(employee__employee_id=attendance_params.employee_id) & Q(status=AttendanceStatusType.ABSENT.value) & Q(
                clock_in_datetime__date__year=attendance_params.year) & Q(
                clock_in_datetime__date__month=attendance_params.month)).count()

    def get_total_single_punch_in_days_month(self, attendance_params: AttendanceParamDTO) -> int:
        return Attendance.objects.filter(
            Q(employee__employee_id=attendance_params.employee_id) & Q(
                status=AttendanceStatusType.SINGLE_PUNCH_ABSENT.value) & Q(
                clock_in_datetime__date__year=attendance_params.year) & Q(
                clock_in_datetime__date__month=attendance_params.month)).count()

    def validate_already_not_clocked_out(self, employee_id: str) -> None:
        today = date.today()
        attendance_object = Attendance.objects.get(
            Q(clock_in_datetime__date=today) & Q(employee__employee_id=employee_id))

        already_clocked_out = attendance_object.clock_out_datetime != None
        if already_clocked_out:
            raise EmployeeAlreadyClockedOut(employee_id=employee_id,
                                            clock_out_datetime=attendance_object.clock_out_datetime)

    @staticmethod
    def _convert_employee_object_to_dto(employee: Employee):
        employee_dto = EmployeeDetailsDTO(
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

    @staticmethod
    def _convert_attendance_object_to_clock_out_dto(attendance: Attendance) -> ClockOutAttendanceDTO:
        clock_out_dto = ClockOutAttendanceDTO(attendance_id=attendance.pk,
                                              clock_out_date_time=attendance.clock_out_datetime)
        return clock_out_dto

    @staticmethod
    def _convert_attendance_object_to_clock_in_dto(attendance: Attendance) -> ClockInAttendanceDTO:
        clock_in_dto = ClockInAttendanceDTO(attendance_id=attendance.pk,
                                            clock_in_date_time=attendance.clock_in_datetime)
        return clock_in_dto

    @staticmethod
    def _convert_attendance_list_object_to_dto(attendance_object_list: List[Dict]) -> List[AttendanceDTO]:
        attendance_dto_list = []
        for attendance_object in attendance_object_list:
            attendance_dto = AttendanceDTO(
                attendance_id=attendance_object['id'],
                clock_in_date_time=attendance_object['clock_in_datetime'],
                clock_out_date_time=attendance_object['clock_out_datetime'],
                status=attendance_object['status']
            )
            attendance_dto_list.append(attendance_dto)
        return attendance_dto_list

    def mark_single_punch_absent(self) -> None:
        # Updating all values which is
        # Not today and
        # Not Clockout is none and
        # Status is marked PRESENT

        today = date.today()
        Attendance.objects.filter(
            ~Q(clock_in_datetime__date=today) & Q(clock_out_datetime=None) & Q(
                status=AttendanceStatusType.PRESENT.value)).update(
            status=AttendanceStatusType.SINGLE_PUNCH_ABSENT.value)
