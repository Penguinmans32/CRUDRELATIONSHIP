from django.db import models

# Create your models here.

class JobTitle(models.Model):
    job_title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    cityId = models.IntegerField()
    email = models.EmailField()
    employment_start = models.DateField()
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmploymentTerms(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employment_terms")
    agreed_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_start_date = models.DateField()
    salary_end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.agreed_salary}"

class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class DepartmentHistory(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.department}"

class SalaryPayment(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_payments')
    salary = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.salary} ({self.start_date} to {self.end_date})"


class WorkingHours(models.Model):
        id = models.AutoField(primary_key=True)
        employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="working_hours")
        start_time = models.TimeField()
        end_time = models.TimeField()

        def __str__(self):
            return f"{self.employee} - {self.start_time} to {self.end_time}"

