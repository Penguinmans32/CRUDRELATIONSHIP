from django import forms
from .models import Employee, JobTitle, EmploymentTerms

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
