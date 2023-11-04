from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDTO
from hr_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from hr_core.exceptions.custom_exceptions import InvalidMoth
from hr_core.exceptions.custom_exceptions import InvalidYear
from django.http import HttpResponse


class FullMonthStatsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_full_month_stats_wrapper(self, month: int, year: int, employee_id: str,
                                     presenter: PresenterInterface) -> HttpResponse:
        try:
            full_month_stats_dto = self.get_full_month_stats(month=month, year=year, employee_id=employee_id)
        except InvalidMoth:
            return presenter.raise_exception_for_invalid_month()
        except InvalidYear:
            return presenter.raise_exception_for_invalid_year()

        return presenter.get_response_for_get_full_month_stats(full_month_stats_dto=full_month_stats_dto)

    def get_full_month_stats(self, month: int, year: int, employee_id: str) -> FullMothStatsDTO:
        self.storage.validate_year(year=year)
        self.storage.validate_month(month=month)

        total_working_days = self.storage.get_total_present_days_month(employee_id=employee_id, month=month, year=year)
        total_present_days = self.storage.get_total_present_days_month(employee_id=employee_id, month=month, year=year)
        total_absent_days = self.storage.get_total_absent_days_month(employee_id=employee_id, month=month, year=year)
        total_single_punch_in_days = self.storage.get_single_punch_in_days_month(employee_id=employee_id, month=month,
                                                                                 year=year)

        return FullMothStatsDTO(
            total_working_days=total_working_days,
            total_present_days=total_present_days,
            total_absent_days=total_absent_days,
            total_single_punch_in_days=total_single_punch_in_days
        )
