from enum import Enum


class JobRoleType(Enum):
    MANAGER = "MANAGER"
    JUNIOR_ENGINEER = "JUNIOR_ENGINEER"
    SENIOR_ENGINEER = "SENIOR_ENGINEER"


class DepartmentType(Enum):
    HR = "HR"
    ENGINEERING = "ENGINEERING"


class AttendanceStatusType(Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    HOLIDAY = "HOLIDAY"


class StatusCode(Enum):
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    SUCCESS = 200
    SUCCESS_CREATE = 201
