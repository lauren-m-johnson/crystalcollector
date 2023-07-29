from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Crystal, Prop
from .forms import AquiredForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    crystals = Crystal.objects.all()
    return render(request, 'crystals/index.html', {
        'crystals': crystals
    })

def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    aquired_form = AquiredForm()
    return render(request, 'crystals/detail.html', { 'crystal': crystal, 'aquired_form': aquired_form})

def add_aquired(request, crystal_id):
    form = AquiredForm(request.POST)
    if form.is_valid():
        new_aquired = form.save(commit=False)
        new_aquired.crystal_id = crystal_id
        new_aquired.save()
    return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(CreateView):
    model = Crystal
    fields = '__all__'

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ['hardness', 'structure', 'color', 'transparency']

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals'

class PropList(ListView):
  model = Prop

class PropDetail(DetailView):
  model = Prop

class PropCreate(CreateView):
  model = Prop
  fields = '__all__'

class PropUpdate(UpdateView):
  model = Prop
  fields = ['property']

class PropDelete(DeleteView):
  model = Prop
  success_url = '/props'
