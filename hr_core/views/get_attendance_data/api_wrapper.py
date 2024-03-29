from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.presenters.presenter_implementation import PresenterImplementation
from hr_core.interactors.get_attendance_data_interactor import GetAttendanceDataInteractor
from hr_core.interactors.storage_interfaces.dtos import AttendanceParamDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs['query_params']
    month = query_params['month']
    year = query_params['year']
    employee_id = kwargs['employee_id']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAttendanceDataInteractor(storage=storage)

    attendance_params = AttendanceParamDTO(
        month=month,
        year=year,
        employee_id=employee_id
    )

    return interactor.get_attendance_data_wrapper(attendance_params=attendance_params, presenter=presenter)
