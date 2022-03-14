from django.contrib import admin
from crudapp.models import Student, StudentMarks

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list = ['serialno', 'firstname', 'lastname', 'gender', 'department', 'phonenumber', 'emailId']

class StudentMarksAdmin(admin.ModelAdmin):
	list = ['StuId', 'SubjectName', 'SubjectMark']


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentMarks, StudentAdmin)


