from typing import List
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from django.http import HttpResponse
from hr_core.interactors.storage_interfaces.dtos import AttendanceDTO
from hr_core.exceptions.custom_exceptions import InvalidMoth
from hr_core.exceptions.custom_exceptions import InvalidYear


class GetAttendanceDataInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_attendance_data_wrapper(self, month: int, year: int, employee_id: str,
                                    presenter: PresenterInterface) -> HttpResponse:
        try:
            attendance_data_dto_list = self.get_attendance_data(month=month, year=year, employee_id=employee_id)
        except InvalidMoth:
            return presenter.raise_exception_for_invalid_month()
        except InvalidYear:
            return presenter.raise_exception_for_invalid_year()

        return presenter.get_response_for_get_attendance_data(attendance_dto_list=attendance_data_dto_list)

    def get_attendance_data(self, month: int, year: int, employee_id: str) -> List[AttendanceDTO]:
        # todo: better to follow kwargs evn for one arg
        # todo: validate month and year are completely python logic so, writing them in storage layer is not appropriate
        self.storage.validate_month(month)
        self.storage.validate_year(year)

        # todo: attendance_data_dto_list can be renamed as attendance_data_dtos (we can add plural form instead of list suffix)
        attendance_data_dto_list = self.storage.get_attendance_data_for_month_year_employee(month=month, year=year,
                                                                                            employee_id=employee_id)
        return attendance_data_dto_list
