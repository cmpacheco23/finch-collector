from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', {'dog': dog})

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'pawrent', 'age']
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'pawrent', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url= '/dogs/'