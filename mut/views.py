# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import LostID, Category, IDReplacement, Payment
from .forms import (
    LostIDForm, 
    FoundIDForm, 
    IDReplacementForm, 
    PaymentForm,
    ProfileForm
)


def home(request):
    lost_ids = LostID.objects.all()
    categories = Category.objects.all()
    context = {
        'lost_ids': lost_ids,
        'categories': categories,
        'lost_ids_found': LostID.objects.filter(status='FOUND'),
        'lost_ids_pending': LostID.objects.filter(status='PENDING'),
        'lost_ids_claimed': LostID.objects.filter(status='CLAIMED'),
    }
    return render(request, 'home.html', context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('homepage')



# Lost ID Management Views
def lost_id_list(request):
    lost_ids = LostID.objects.all().order_by('-date_reported')
    categories = Category.objects.all()
    
    # Filter by category if provided
    category_id = request.GET.get('category')
    if category_id:
        lost_ids = lost_ids.filter(category_id=category_id)
    
    context = {
        'lost_ids': lost_ids,
        'categories': categories
    }
    return render(request, 'lost_id/list.html', context)

def lost_id_detail(request, pk):
    lost_id = get_object_or_404(LostID, pk=pk)
    return render(request, 'lost_id/detail.html', {'lost_id': lost_id})

@login_required
def report_lost_id(request):
    if request.method == 'POST':
        form = LostIDForm(request.POST, request.FILES)
        if form.is_valid():
            lost_id = form.save(commit=False)
            lost_id.save()
            messages.success(request, 'Lost ID reported successfully.')
            return redirect('lost_id:lost_id_detail', pk=lost_id.pk)
    else:
        form = LostIDForm()
    return render(request, 'lost_id/report.html', {'form': form})

@login_required
def update_lost_id(request, pk):
    lost_id = get_object_or_404(LostID, pk=pk)
    if request.method == 'POST':
        form = LostIDForm(request.POST, request.FILES, instance=lost_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lost ID updated successfully.')
            return redirect('lost_id:lost_id_detail', pk=pk)
    else:
        form = LostIDForm(instance=lost_id)
    return render(request, 'lost_id/update.html', {'form': form, 'lost_id': lost_id})

@login_required
def delete_lost_id(request, pk):
    lost_id = get_object_or_404(LostID, pk=pk)
    if request.method == 'POST':
        lost_id.delete()
        messages.success(request, 'Lost ID deleted successfully.')
        return redirect('lost_id:lost_id_list')
    return render(request, 'lost_id/delete.html', {'lost_id': lost_id})

# Found ID Management Views
@login_required
def report_found_id(request):
    if request.method == 'POST':
        form = FoundIDForm(request.POST, request.FILES)
        if form.is_valid():
            found_id = form.save(commit=False)
            found_id.status = 'FOUND'
            found_id.save()
            messages.success(request, 'Found ID reported successfully.')
            return redirect('lost_id:lost_id_detail', pk=found_id.pk)
    else:
        form = FoundIDForm()
    return render(request, 'lost_id/report_found.html', {'form': form})

@login_required
def claim_id(request, pk):
    lost_id = get_object_or_404(LostID, pk=pk)
    if request.method == 'POST':
        lost_id.status = 'CLAIMED'
        lost_id.save()
        messages.success(request, 'ID claimed successfully.')
        return redirect('lost_id:lost_id_detail', pk=pk)
    return render(request, 'lost_id/claim.html', {'lost_id': lost_id})

# Search and Filter Views
def search_lost_ids(request):
    query = request.GET.get('q', '')
    lost_ids = LostID.objects.filter(
        Q(student_name__icontains=query) |
        Q(registration_number__icontains=query)
    )
    data = [{
        'id': id.id,
        'student_name': id.student_name,
        'registration_number': id.registration_number,
        'status': id.status
    } for id in lost_ids]
    return JsonResponse({'results': data})

def filter_lost_ids(request):
    category_id = request.GET.get('category')
    status = request.GET.get('status')
    
    lost_ids = LostID.objects.all()
    if category_id:
        lost_ids = lost_ids.filter(category_id=category_id)
    if status:
        lost_ids = lost_ids.filter(status=status)
        
    data = [{
        'id': id.id,
        'student_name': id.student_name,
        'registration_number': id.registration_number,
        'status': id.status
    } for id in lost_ids]
    return JsonResponse({'results': data})