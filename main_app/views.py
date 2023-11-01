from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Bowl
from .forms import WalkForm
# Add the following import

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def dog_index(request):
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  bowls_dog_doesnt_have = Bowl.objects.exclude(id__in=dog.bowls.all().values_list('id'))
  walk_form = WalkForm()
  return render(request, 'dogs/detail.html', {'dog': dog, 'walk_form': walk_form, 'bowls': bowls_dog_doesnt_have})

@login_required
def add_walk(request, dog_id):
  form = WalkForm(request.POST)
  if form.is_valid():
    new_walk = form.save(commit=False)
    new_walk.dog_id = dog_id
    new_walk.save()
  return redirect('dog-detail', dog_id=dog_id)

class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']
  
class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url= '/dogs/'

class BowlCreate(LoginRequiredMixin, CreateView):
  model = Bowl
  fields = '__all__'

class BowlList(LoginRequiredMixin, ListView):
  model = Bowl

class BowlDetail(LoginRequiredMixin, DetailView):
  model = Bowl

class BowlUpdate(LoginRequiredMixin, UpdateView):
  model = Bowl
  fields = ['size', 'color']

class BowlDelete(LoginRequiredMixin, DeleteView):
  model = Bowl
  success_url = '/bowls/'

@login_required
def assoc_bowl(request, dog_id, bowl_id):
  Dog.objects.get(id=dog_id).bowls.add(bowl_id)
  return redirect('dog-detail', dog_id=dog_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dog-index')
    else:
      error_message= 'Invalid signup - try again'
  form = UserCreationForm()
  context = {'form':form, 'error_message': error_message}
  return render(request, 'signup.html', context)