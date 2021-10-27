from django.shortcuts import render, redirect
from .models import Date
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def categories_dates_index(request):
  # dates = Date.objects.filter(user=request.user)
  return render(request, 'dates/index.html')

def my_dates(request):
  return render (request, 'dates/my_dates.html')

@login_required
def dates_detail(request, date_id):
  date = Date.objects.get(id=date_id)
  return render(request, 'dates/detail.html', {
    'date': date
  })  

def assoc_dates(request, User, date_id):
  Date.objects.get(id=date_id).User.add(date_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)