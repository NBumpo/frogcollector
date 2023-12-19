from django.shortcuts import render
# Import the Cat Model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
from .forms import FeedingForm
from django.shortcuts import render, redirect
...

def frogs_index(request):
  frogs = Frog.objects.all()
  return render(request, 'frogs/index.html', { 'frogs': frogs })
# Create your views here.
frogs = [
  {'name': 'Kermit', 'color': 'lime green', 'description': 'likes to sing', 'age': 60},
  {'name': 'Kaeru', 'color': 'gray', 'description': 'carefree', 'age': 1},
]

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__'
#   success_url = '/frogs/{frog_id}'

class FrogUpdate(UpdateView):
    model = Frog
    # don't allow updating of the name
    fields = ['color', 'description', 'age']
    # the redirect is happening the get_absolute_url method in the models
    # to go to the detail page


class FrogDelete(DeleteView):
    model = Frog
    success_url = '/frogs'  # redirect to the index page

def home(request):
    return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')



def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'frogs/detail.html', {
    # include the cat and feeding_form in the context
    'frog': frog, 'feeding_form': feeding_form
  })

def add_feeding(request, frog_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.frog_id = frog_id
    new_feeding.save()
  return redirect('detail', frog_id=frog_id)
