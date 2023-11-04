from django.db import models
from hr_core.constants.enums import JobRoleType
from hr_core.constants.enums import DepartmentType
from django.utils.timezone import now


class Employee(models.Model):
    user_id = models.CharField(max_length=255)
    employee_id = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    JobRole_Choice = (
        (JobRoleType.MANAGER.value, JobRoleType.MANAGER.value),
        (JobRoleType.JUNIOR_ENGINEER.value, JobRoleType.JUNIOR_ENGINEER.value),
        (JobRoleType.SENIOR_ENGINEER.value, JobRoleType.SENIOR_ENGINEER.value)
    )
    job_role = models.CharField(max_length=30, choices=JobRole_Choice)
    Department_Choice = (
        (DepartmentType.HR.value, DepartmentType.HR.value),
        (DepartmentType.ENGINEERING.value, DepartmentType.ENGINEERING.value)
    )
    department = models.CharField(max_length=255, choices=Department_Choice)
    joining_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
