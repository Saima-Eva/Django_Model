
from django.contrib import admin
from django.urls import path

from.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentPage', studentPage, name="studentPageUrl"),
    path('teacherPage', teacherPage, name="teacherPageUrl"),
    path('employeePage', employeePage, name="employeePageUrl"),
]
