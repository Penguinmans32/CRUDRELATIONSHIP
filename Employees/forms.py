from django import forms
from .models import Employee, JobTitle, EmploymentTerms, Department, DepartmentHistory, SalaryPayment, WorkingHours  # Ensure WorkingHours is imported

class JobTitleForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JobTitle
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    employment_start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee
        fields = '__all__'


class EmploymentTermsForm(forms.ModelForm):
    salary_start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    salary_end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EmploymentTerms
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentHistoryForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DepartmentHistory
        fields = '__all__'


# New SalaryPayment Form
class SalaryPaymentForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = SalaryPayment  # Ensure this matches your SalaryPayment model
        fields = ['employee', 'salary', 'start_date', 'end_date']  # Adjust the fields as needed


class WorkingHoursForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = WorkingHours
        fields = '__all__'
