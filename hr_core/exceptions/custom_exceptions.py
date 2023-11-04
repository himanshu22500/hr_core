# TODO: better to have the emp_id
class InvalidEmployeeId(Exception):
    pass

# TODO: better to have the emp_id and already clocked in datetime if possible
class EmployeeAlreadyClockedIn(Exception):
    pass

# TODO: better to have the emp_id and already clocked out datetime if possible
class EmployeeAlreadyClockedOut(Exception):
    pass

# TODO: better to have the emp_id
class EmployeeNotClockedIn(Exception):
    pass

# TODO: better to have the invalid month
class InvalidMoth(Exception):
    pass

# TODO: better to have the invalid year
class InvalidYear(Exception):
    pass
