from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
def about(request):
  return render(request, 'about.html')

class Dog:
  def __init__(self, name, breed, description, age): 
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'Kinda rude.', 3),
  Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def dog_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})