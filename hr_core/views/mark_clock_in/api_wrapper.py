from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from hr_core.models.employee import Employee
from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.presenters.presenter_implementation import PresenterImplementation
from hr_core.interactors.mark_clock_in_interactor import MarkClockInInteractor
import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user']
    employee_id = Employee.objects.get(user_id=user_id).employee_id
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = MarkClockInInteractor(storage=storage)

    return interactor.mark_clock_in_wrapper(employee_id=employee_id, presenter=presenter)
