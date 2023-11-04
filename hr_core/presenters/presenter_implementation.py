from typing import List, Dict

from hr_core.constants.exception_messages import INVALID_EMPLOYEE_ID, EMPLOYEE_ALREADY_CLOCKED_OUT
from hr_core.constants.exception_messages import EMPLOYEE_ALREADY_CLOCKED_IN
from hr_core.constants.exception_messages import INVALID_MONTH
from hr_core.constants.exception_messages import INVALID_YEAR
from hr_core.constants.exception_messages import EMPLOYEE_NOT_CLOCKED_IN
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.storage_interfaces.storage_interface import EmployeeDetailsDTO, ClockInAttendanceDTO, \
    FullMothStatsDTO, AttendanceDTO
from hr_core.interactors.storage_interfaces.storage_interface import ClockOutAttendanceDTO
from hr_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):
    def get_mark_clock_in_response(self, clock_in_attendance_dto: ClockInAttendanceDTO) -> HttpResponse:
        clock_in_attendance_dict = {
            "attendance_id": str(clock_in_attendance_dto.attendance_id),
            "clock_in_date_time": str(clock_in_attendance_dto.clock_in_date_time)
        }
        return self.prepare_201_created_response(response_dict=clock_in_attendance_dict)

    def get_response_for_get_attendance_data(self, attendance_dto_list: List[AttendanceDTO]) -> HttpResponse:
        attendance_data_list = self._get_attendance_data_list(attendance_dto_list=attendance_dto_list)
        response_dict = {
            "attendance_data": attendance_data_list
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def _get_attendance_data_list(attendance_dto_list: List[AttendanceDTO]) -> List[Dict]:
        attendance_data_list = []
        for attendance_dto in attendance_dto_list:
            attendance_data_dict = {
                "attendance_id": attendance_dto.attendance_id,
                "clock_in_date_time": str(attendance_dto.clock_in_date_time),
                "clock_out_date_time": str(attendance_dto.clock_out_date_time),
                "status": attendance_dto.status
            }
            attendance_data_list.append(attendance_data_dict)

        return attendance_data_list

    def raise_exception_for_employee_already_clocked_in(self) -> HttpResponse:
        response_dict = {
            "response": EMPLOYEE_ALREADY_CLOCKED_IN[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPLOYEE_ALREADY_CLOCKED_IN[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_employee_already_clocked_out(self) -> HttpResponse:
        response_dict = {
            "response": EMPLOYEE_ALREADY_CLOCKED_OUT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPLOYEE_ALREADY_CLOCKED_OUT[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_invalid_month(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_MONTH[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MONTH[1]
        }

        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_invalid_year(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_YEAR[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_YEAR[1]
        }

        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def get_response_for_get_full_month_stats(self, full_month_stats_dto: FullMothStatsDTO) -> HttpResponse:
        response_dict = {
            "total_working_days": full_month_stats_dto.total_working_days,
            "total_present_days": full_month_stats_dto.total_present_days,
            "total_absent_days": full_month_stats_dto.total_absent_days,
            "total_single_punch_in_days": full_month_stats_dto.total_single_punch_in_days
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    def raise_exception_for_employee_not_clocked_in(self) -> HttpResponse:
        response_dict = {
            "response": EMPLOYEE_NOT_CLOCKED_IN[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPLOYEE_NOT_CLOCKED_IN[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def get_response_for_get_employee(self, employee_details_dto: EmployeeDetailsDTO) -> HttpResponse:
        employee_details_dict = self._get_employee_details(employee_details_dto)
        return self.prepare_200_success_response(response_dict=employee_details_dict)

    def get_mark_clock_out_response(self, clock_out_attendance_dto: ClockOutAttendanceDTO) -> HttpResponse:
        clock_out_attendance_dict = {
            "attendance_id": str(clock_out_attendance_dto.attendance_id),
            "clock_out_date_time": str(clock_out_attendance_dto.clock_out_date_time)
        }
        return self.prepare_200_success_response(response_dict=clock_out_attendance_dict)

    @staticmethod
    def _get_employee_details(employee_dto: EmployeeDetailsDTO) -> Dict:
        employee_details_dict = {
            "employee_id": employee_dto.employee_id,
            "first_name": employee_dto.first_name,
            "last_name": employee_dto.last_name,
            "email": employee_dto.email,
            "phone_number": employee_dto.phone_number,
            "job_role": employee_dto.job_role,
            "department": employee_dto.department,
            "joining_date": str(employee_dto.joining_date)
        }
        return employee_details_dict

    def raise_exception_for_invalid_employee(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_EMPLOYEE_ID[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_EMPLOYEE_ID[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)
