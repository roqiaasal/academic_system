from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

class University(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    established_year = models.IntegerField()
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.name

class AcademicDegree(models.Model):
    name = models.CharField(max_length=100)
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    blace_of_birth = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name
    
class Certificate(models.Model):
    name = models.CharField(max_length=100)


    
class Qualification(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    cetificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    data_of_issue = models.DateField()
    University = models.ForeignKey(University, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)  
    general_specialty = models.CharField(max_length=200)
    specific_specialty = models.CharField(max_length=200)  
    
class courses(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    course_vocabulary = models.TextField()

class subjects(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.IntegerField(null = True, blank = True)
    course_part = models.CharField(max_length=100)    

class SupervisionType(models.Model):  
    name = models.CharField(max_length=100)
    
class supervision(models.Model):
    search_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_start = models.DateField()
    date_of_finish = models.DateField()
    year = models.IntegerField()
    Academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    Supervision_type = models.ForeignKey(SupervisionType, on_delete=models.CASCADE)