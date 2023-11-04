from typing import List, Dict
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance
from hr_core.models.data import employees_details
from hr_core.models.data import attendance_data

employee_orm_dict = {}


def populate_employee(employee_dict_list: List[Dict]) -> None:
    '''
    employee_dict_list = [{'department': 'HR',
     'email': 'christy83@example.net',
     'employee_id': 1,
     'first_name': 'Michael',
     'job_role': 'MANAGER',
     'joining_date': datetime.datetime(2023, 6, 14, 0, 0),
     'last_name': 'Martinez',
     'phone_number': '432-678-1046x538'}]
    '''

    employee_orm_list = []
    for employee_dict in employee_dict_list:
        employee_orm_obj = Employee(
            employee_id=employee_dict['employee_id'],
            department=employee_dict['department'],
            first_name=employee_dict['first_name'],
            last_name=employee_dict['last_name'],
            phone_number=employee_dict['phone_number'],
            joining_date=employee_dict['joining_date'],
            job_role=employee_dict['job_role'],
            email=employee_dict['email']
        )
        employee_orm_dict[employee_dict['employee_id']] = employee_orm_obj
        employee_orm_list.append(employee_orm_obj)

    Employee.objects.bulk_create(employee_orm_list)


def populate_attendance(attendance_dict_list: List[Dict]) -> None:
    '''
    attendance_list = [
            {'clock_in_datetime': datetime.datetime(2022, 10, 8, 9, 0),
             'clock_out_datetime': datetime.datetime(2022, 10, 8, 17, 0),
             'employee_id': 0,
             'status': 'PRESENT'},
            {'clock_in_datetime': datetime.datetime(2022, 10, 9, 9, 0),
             'clock_out_datetime': None,
             'employee_id': 0,
             'status': 'SINGLE_PUNCH_ABSENT'}
        ]
    '''

    attendance_orm_list = []
    for attendance_dict in attendance_dict_list:
        attendance_orm_obj = Attendance(
            employee=employee_orm_dict[attendance_dict['employee_id']],
            clock_in_datetime=attendance_dict['clock_in_datetime'],
            clock_out_datetime=attendance_dict['clock_out_datetime'],
            status=attendance_dict['status']
        )
        attendance_orm_list.append(attendance_orm_obj)

    Attendance.objects.bulk_create(attendance_orm_list)


populate_employee(employees_details)
populate_attendance(attendance_data)
