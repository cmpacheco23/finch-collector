from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Dog, Bowl
from .forms import WalkForm
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
  walk_form = WalkForm()
  return render(request, 'dogs/detail.html', {'dog': dog, 'walk_form': walk_form})

def add_walk(request, dog_id):
  form = WalkForm(request.POST)
  if form.is_valid():
    new_walk = form.save(commit=False)
    new_walk.dog_id = dog_id
    new_walk.save()
  return redirect('dog-detail', dog_id=dog_id)

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'pawrent', 'age']
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'pawrent', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url= '/dogs/'

class BowlCreate(CreateView):
  model = Bowl
  fields = '__all__'