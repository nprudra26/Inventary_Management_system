from django.shortcuts import render, get_object_or_404, redirect
from .models import Repair
from django.contrib import messages
from datetime import datetime

def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, 'repair_list.html', {'repairs': repairs})

def add_repair(request):
    if request.method == 'POST':
        device_type = request.POST.get('device_type')
        emp_name = request.POST.get('emp_name')
        device_id = request.POST.get('device_id')
        outward_date = request.POST.get('outward_date')
        inward_date = request.POST.get('inward_date') or None
        purpose_of_repair = request.POST.get('purpose_of_repair')
        client_name = request.POST.get('client_name')

        repair = Repair(
            device_type=device_type,
            emp_name=emp_name,
            device_id=device_id,
            outward_date=outward_date,
            inward_date=inward_date,
            purpose_of_repair=purpose_of_repair,
            client_name=client_name
        )
        repair.save()
        messages.success(request, "Repair record added successfully.")
        return redirect('repair_list')

    return render(request, 'add_repair.html')

def update_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.device_type = request.POST.get('device_type')
        repair.emp_name = request.POST.get('emp_name')
        repair.device_id = request.POST.get('device_id')
        repair.outward_date = request.POST.get('outward_date') or None
        repair.inward_date = request.POST.get('inward_date') or None
        repair.purpose_of_repair = request.POST.get('purpose_of_repair')
        repair.client_name = request.POST.get('client_name')
        repair.save()
        messages.success(request, "Repair record updated successfully.")
        return redirect('repair_list')

    return render(request, 'update_repair.html', {'repair': repair})

def delete_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    repair.delete()
    messages.success(request, "Repair record deleted successfully.")
    return redirect('repair_list')
