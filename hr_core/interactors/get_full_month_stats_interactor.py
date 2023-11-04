from hr_core.interactors.storage_interfaces.storage_interface import StorageInterface
from hr_core.interactors.storage_interfaces.dtos import FullMothStatsDto
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
            full_month_stats_dto = self.full_month_stats(month=month, year=year, employee_id=employee_id)
        except InvalidMoth:
            return presenter.raise_exception_for_invalid_month()
        except InvalidYear:
            return presenter.raise_exception_for_invalid_year()

        return presenter.get_response_for_get_full_month_stats(full_month_stats_dto=full_month_stats_dto)

    def full_month_stats(self, month: int, year: int, employee_id: str) -> FullMothStatsDto:
        self.storage.validate_year(year=year)
        self.storage.validate_month(month=month)

        full_month_stats_dto = self.storage.get_full_month_stats(employee_id=employee_id, month=month, year=year)
        return full_month_stats_dto
