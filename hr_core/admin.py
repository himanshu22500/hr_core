from django.contrib import admin
from hr_core.models.employee import Employee
from hr_core.models.attendance import Attendance

admin.site.register(Employee)
admin.site.register(Attendance)
