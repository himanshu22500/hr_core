from datetime import datetime


class InvalidEmployeeId(Exception):
    def __init__(self, employee_id: str):
        self.employee_id = employee_id


class EmployeeAlreadyClockedIn(Exception):
    def __init__(self, employee_id: str, clock_in_datetime: datetime):
        self.employee_id = employee_id
        self.clock_in_datetime = clock_in_datetime


class EmployeeAlreadyClockedOut(Exception):
    def __init__(self, employee_id: str, clock_out_datetime: datetime):
        self.employee_id = employee_id
        self.clock_out_datetime = clock_out_datetime


class EmployeeNotClockedIn(Exception):
    def __init__(self, employee_id: str):
        self.employee_id = employee_id


class InvalidMoth(Exception):
    def __init__(self, month: int):
        self.month = month


class InvalidYear(Exception):
    def __init__(self, year: int):
        self.year = year
