from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDTO, AttendanceParamDTO
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.exceptions.custom_exceptions import InvalidMoth
from hr_core.exceptions.custom_exceptions import InvalidYear
from django.http import HttpResponse


class FullMonthStatsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_full_month_stats_wrapper(self, attendance_params: AttendanceParamDTO,
                                     presenter: PresenterInterface) -> HttpResponse:
        try:
            full_month_stats_dto = self.get_full_month_stats(attendance_params)
        except InvalidMoth:
            return presenter.raise_exception_for_invalid_month()
        except InvalidYear:
            return presenter.raise_exception_for_invalid_year()

        return presenter.get_response_for_get_full_month_stats(full_month_stats_dto=full_month_stats_dto)

    def get_full_month_stats(self, attendance_params: AttendanceParamDTO) -> FullMothStatsDTO:
        self.validate_year(year=attendance_params.year)
        self.validate_month(month=attendance_params.month)

        total_working_days = self.storage.get_total_working_days_month(month=attendance_params.month,
                                                                       year=attendance_params.year)
        total_present_days = self.storage.get_total_present_days_month(attendance_params=attendance_params)
        total_absent_days = self.storage.get_total_absent_days_month(attendance_params=attendance_params)
        total_single_punch_in_days = self.storage.get_single_punch_in_days_month(attendance_params=attendance_params)

        return FullMothStatsDTO(
            total_working_days=total_working_days,
            total_present_days=total_present_days,
            total_absent_days=total_absent_days,
            total_single_punch_in_days=total_single_punch_in_days
        )

    @staticmethod
    def validate_month(month: int) -> None:
        is_month_valid = 1 <= month <= 12
        is_month_not_valid = not is_month_valid

        if is_month_not_valid:
            raise InvalidMoth(month=month)

    @staticmethod
    def validate_year(year: int) -> None:
        from datetime import date
        current_year = date.today().year
        is_year_valid = year <= current_year
        is_year_not_valid = not is_year_valid

        if is_year_not_valid:
            raise InvalidYear(year=year)
