from django.contrib import admin


# Register your models here.
from myapp.models import Student_Model
from myapp.models import Teachers_Model
from myapp.models import Employee_Model

admin.site.register(Student_Model)
admin.site.register(Teachers_Model)
admin.site.register(Employee_Model)
