from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import OfficeStationary
from django.contrib import messages

def stationary_list(request):
    items = OfficeStationary.objects.all()
    return render(request, 'stationary_list.html', {'items': items})

def add_stationary(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        purchase_date = request.POST.get('purchase_date')
        activation_date = request.POST.get('activation_date')
        expiry_date = request.POST.get('expiry_date')
        mail_id = request.POST.get('mail_id')
        warranty_years = request.POST.get('warranty_years')
        make_in = request.POST.get('make_in')

        OfficeStationary.objects.create(
            product_name=product_name,
            purchase_date=purchase_date,
            activation_date=activation_date,
            expiry_date = expiry_date,
            mail_id=mail_id,
            warranty_years=warranty_years,
            make_in=make_in
        )
        messages.success(request, "Stationary item added successfully!")
        return redirect('stationary_list')
    
    return render(request, 'add_stationary.html')

def update_stationary(request, pk):
    item = get_object_or_404(OfficeStationary, pk=pk)
    if request.method == 'POST':
        item.product_name = request.POST.get('product_name')
        item.purchase_date = request.POST.get('purchase_date')
        item.activation_date = request.POST.get('activation_date')
        item.expiry_date = request.POST.get('expiry_date')
        item.mail_id = request.POST.get('mail_id')
        item.warranty_years = request.POST.get('warranty_years')
        item.make_in = request.POST.get('make_in')
        item.save()
        messages.success(request, "Stationary item updated successfully!")
        return redirect('stationary_list')
    
    return render(request, 'update_stationary.html', {'item': item})

def delete_stationary(request, pk):
    item = get_object_or_404(OfficeStationary, pk=pk)
    item.delete()
    messages.success(request, "Stationary item deleted successfully!")
    return redirect('stationary_list')
