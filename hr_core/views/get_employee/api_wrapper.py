from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from hr_core.storages.storage_implementation import StorageImplementation
from hr_core.presenters.presenter_implementation import PresenterImplementation
from hr_core.interactors.get_employee_interactor import GetEmployeeInteractor

import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    employee_id = kwargs['employee_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetEmployeeInteractor(storage=storage)
    return interactor.get_employee_wrapper(employee_id=employee_id, presenter=presenter)
