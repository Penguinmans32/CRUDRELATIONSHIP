from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, JobTitle, EmploymentTerms, Department, DepartmentHistory, SalaryPayment, WorkingHours  # Import WorkingHours
from .forms import EmployeeForm, JobTitleForm, EmploymentTermsForm, DepartmentForm, DepartmentHistoryForm, SalaryPaymentForm, WorkingHoursForm  # Ensure you have a WorkingHoursForm

# Create your views here.

# JobTitle views
def job_title_list(request):
    job_titles = JobTitle.objects.all()
    return render(request, 'job_title_list.html', {'job_titles': job_titles})

def job_title_create(request):
    form = JobTitleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job_title_list')
    return render(request, 'job_title_form.html', {'form': form})

def job_title_update(request, pk):
    job_title = get_object_or_404(JobTitle, pk=pk)
    form = JobTitleForm(request.POST or None, instance=job_title)
    if form.is_valid():
        form.save()
        return redirect('job_title_list')
    return render(request, 'job_title_form.html', {'form': form})

def job_title_delete(request, pk):
    job_title = get_object_or_404(JobTitle, pk=pk)
    if request.method == 'POST':
        job_title.delete()
        return redirect('job_title_list')
    return render(request, 'job_title_confirm_delete.html', {'object': job_title})

# Employee views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'object': employee})

# EmploymentTerms views
def employment_terms_list(request):
    employment_terms = EmploymentTerms.objects.all()
    return render(request, 'employment_terms_list.html', {'terms': employment_terms})

def employment_terms_create(request):
    form = EmploymentTermsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employment_terms_list')
    return render(request, 'employment_terms_form.html', {'form': form})

def employment_terms_update(request, pk):
    term = get_object_or_404(EmploymentTerms, pk=pk)
    form = EmploymentTermsForm(request.POST or None, instance=term)
    if form.is_valid():
        form.save()
        return redirect('employment_terms_list')
    return render(request, 'employment_terms_form.html', {'form': form})

def employment_terms_delete(request, pk):
    term = get_object_or_404(EmploymentTerms, pk=pk)
    if request.method == 'POST':
        term.delete()
        return redirect('employment_terms_list')
    return render(request, 'employment_terms_confirm_delete.html', {'object': term})

# SalaryPayment views
def salary_payment_list(request):
    salary_payments = SalaryPayment.objects.all()
    return render(request, 'salary_payment_list.html', {'salary_payments': salary_payments})

def salary_payment_create(request):
    form = SalaryPaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('salary_payment_list')
    return render(request, 'salary_payment_form.html', {'form': form})

def salary_payment_update(request, pk):
    salary_payment = get_object_or_404(SalaryPayment, pk=pk)
    form = SalaryPaymentForm(request.POST or None, instance=salary_payment)
    if form.is_valid():
        form.save()
        return redirect('salary_payment_list')
    return render(request, 'salary_payment_form.html', {'form': form})

def salary_payment_delete(request, pk):
    salary_payment = get_object_or_404(SalaryPayment, pk=pk)
    if request.method == 'POST':
        salary_payment.delete()
        return redirect('salary_payment_list')
    return render(request, 'salary_payment_confirm_delete.html', {'salary_payment': salary_payment})

# WorkingHours views
def working_hours_list(request):
    working_hours = WorkingHours.objects.all()
    return render(request, 'working_hours_list.html', {'working_hours': working_hours})

def working_hours_create(request):
    form = WorkingHoursForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('working_hours_list')
    return render(request, 'working_hours_form.html', {'form': form})

def working_hours_update(request, pk):
    working_hours = get_object_or_404(WorkingHours, pk=pk)
    form = WorkingHoursForm(request.POST or None, instance=working_hours)
    if form.is_valid():
        form.save()
        return redirect('working_hours_list')
    return render(request, 'working_hours_form.html', {'form': form})

def working_hours_delete(request, pk):
    working_hours = get_object_or_404(WorkingHours, pk=pk)
    if request.method == 'POST':
        working_hours.delete()
        return redirect('working_hours_list')
    return render(request, 'working_hours_confirm_delete.html', {'working_hours': working_hours})

# Index view
def index(request):
    urls = {
        'Job Titles': {
            'List': reverse('job_title_list'),
            'Create': reverse('job_title_create')
        },
        'Employees': {
            'List': reverse('employee_list'),
            'Create': reverse('employee_create')
        },
        'Employment Terms': {
            'List': reverse('employment_terms_list'),
            'Create': reverse('employment_terms_create')
        },
        'Departments': {
            'List': reverse('department_list'),
            'Create': reverse('department_create')
        },
        'Department History': {
            'List': reverse('department_history_list'),
            'Create': reverse('department_history_create')
        },
        'Salary Payments': {
            'List': reverse('salary_payment_list'),
            'Create': reverse('salary_payment_create')
        },
        'Working Hours': {
            'List': reverse('working_hours_list'),
            'Create': reverse('working_hours_create')
        }
    }
    return render(request, 'index.html', {'urls': urls})

# Department views
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'object': department})

# Department History Views
def department_history_list(request):
    history = DepartmentHistory.objects.all()
    return render(request, 'department_history_list.html', {'history': history})

def department_history_create(request):
    if request.method == "POST":
        form = DepartmentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_history_list')
    else:
        form = DepartmentHistoryForm()
    return render(request, 'department_history_form.html', {'form': form})

def department_history_update(request, pk):
    history = get_object_or_404(DepartmentHistory, pk=pk)
    if request.method == "POST":
        form = DepartmentHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('department_history_list')
    else:
        form = DepartmentHistoryForm(instance=history)
    return render(request, 'department_history_form.html', {'form': form})

def department_history_delete(request, pk):
    history = get_object_or_404(DepartmentHistory, pk=pk)
    if request.method == 'POST':
        history.delete()
        return redirect('department_history_list')
    return render(request, 'department_history_confirm_delete.html', {'history': history})
