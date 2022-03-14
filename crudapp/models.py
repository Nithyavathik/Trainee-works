from django.db import models

# Create your models here.

class Student(models.Model):
	serialno=models.IntegerField()
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	department=models.CharField(max_length=30)
	phonenumber=models.IntegerField()
	emailId=models.EmailField(max_length=100)

	class Meta:
		db_table="students"
		verbose_name_plural="students"

	def __str__(self):
		return (self.firstname+" "+self.lastname)
	
class StudentMarks(models.Model):
	StuId=models.ForeignKey(Student,related_name="Studentname")
	SubjectName=models.CharField(max_length=50)
	SubjectMark=models.IntegerField()

	class Meta:
		db_table="studentmarks"
		verbose_name_plural="Studentmarks"

	def __str__(self):
		return (str(self.StuId) +' '+ self.SubjectName + " " + str(self.SubjectMark))

class Marklist(models.Model):
	StId=models.ForeignKey(Student, on_delete=models.CASCADE)
	Language=models.IntegerField()
	Maths=models.IntegerField()
	Physics=models.IntegerField()
	Chemistry=models.IntegerField()
	Biology=models.IntegerField()
	
	class Meta:
		db_table="marklists"
		verbose_name_plural="Marklists"

	def __str__(self):
		return str(self.StId)
