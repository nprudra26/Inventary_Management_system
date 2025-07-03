from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Employee

def get_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        handover_date = request.POST.get('handover_date')
        model_name = request.POST.get('model_name')
        laptop_name = request.POST.get('laptop_name')
        processor = request.POST.get('processor')
        windows = request.POST.get('windows')
        ssd = request.POST.get('ssd')
        ram = request.POST.get('ram')
        device_id = request.POST.get('device_id')
        product_serial_no = request.POST.get('product_serial_no')
        username = request.POST.get('username')
        hostname = request.POST.get('hostname')
        password = request.POST.get('password')
        dlp = request.POST.get('dlp')
        option_type = request.POST.get('option_type')

        try:
            Employee.objects.create(
                emp_name=emp_name,
                handover_date=handover_date,
                model_name=model_name,
                laptop_name=laptop_name,
                processor=processor,
                windows=windows,
                ssd=ssd,
                ram=ram,
                device_id=device_id,
                product_serial_no=product_serial_no,
                username= username,
                hostname = hostname,
                password=password,
                dlp=dlp,
                option_type=option_type)
            return redirect('get_employee')
        except IntegrityError as e:
            return render(request, 'add_employee.html', {'error': f'An error occurred: {str(e)}'})

    return render(request, 'add_employee.html')

def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.emp_name = request.POST.get('emp_name')
        employee.handover_date = request.POST.get('handover_date')
        employee.model_name = request.POST.get('model_name')
        employee.laptop_name = request.POST.get('laptop_name')
        employee.processor = request.POST.get('processor')
        employee.windows = request.POST.get('windows')
        employee.ssd = request.POST.get('ssd')
        employee.ram = request.POST.get('ram')
        employee.device_id = request.POST.get('device_id')
        employee.product_serial_no = request.POST.get('product_serial_no')
        employee.password = request.POST.get('password')
        employee.username = request.POST.get('username')
        employee.hostname = request.POST.get('hostname')
        employee.dlp = request.POST.get('dlp')
        employee.option_type = request.POST.get('option_type')
        employee.save()
        return redirect('get_employee')

    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('get_employee')
