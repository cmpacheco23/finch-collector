from django.shortcuts import render
from .models import Dog
# Add the following import

# Define the home view
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')

def dog_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogs})

