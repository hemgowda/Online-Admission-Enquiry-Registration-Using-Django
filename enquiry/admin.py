from django.contrib import admin
from enquiry.models import Admission,Student,Department

# Register your models here.



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    ordering = ('name',)
    search_fields = ('name','email')
    list_filter = ('name', 'email')
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('D_name','start_year')
    ordering = ('D_name',)
    search_fields = ('D_name', 'start_year')
    list_filter = ('D_name', 'start_year')

admin.site.register(Admission)