from django.db import models
from hr_core.models.employee import Employee
from hr_core.constants.enums import AttendanceStatusType


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name="employee")
    clock_in_datetime = models.DateTimeField()
    clock_out_datetime = models.DateTimeField(null=True, blank=True)
    AttendanceStatus_Choice = (
        (AttendanceStatusType.PRESENT.value, AttendanceStatusType.PRESENT.value),
        (AttendanceStatusType.ABSENT.value, AttendanceStatusType.ABSENT.value),
        (AttendanceStatusType.HOLIDAY.value, AttendanceStatusType.HOLIDAY.value)
    )
    status = models.CharField(max_length=15, choices=AttendanceStatus_Choice)

    from django.contrib.auth.admin import UserAdmin, User
    def __str__(self):
        return "%s %s" % (self.employee, self.status)
