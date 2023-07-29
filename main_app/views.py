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
    id_list = crystal.props.all().values_list('id')
    props_crystal_doesnt_have = Prop.objects.exclude(id__in=id_list)
    aquired_form = AquiredForm()
    return render(request, 'crystals/detail.html', {
        'crystal': crystal,
        'aquired_form': aquired_form,
        'props': props_crystal_doesnt_have
        })

class CrystalCreate(CreateView):
    model = Crystal
    fields = ['name', 'hardness', 'structure', 'color', 'transparency']

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ['hardness', 'structure', 'color', 'transparency']

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals'

def add_aquired(request, crystal_id):
    form = AquiredForm(request.POST)
    if form.is_valid():
        new_aquired = form.save(commit=False)
        new_aquired.crystal_id = crystal_id
        new_aquired.save()
    return redirect('detail', crystal_id=crystal_id)

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

def assoc_prop(request, crystal_id, prop_id):
   Crystal.objects.get(id=crystal_id).props.add(prop_id)
   return redirect('detail', crystal_id=crystal_id)

def unassoc_prop(request, crystal_id, prop_id):
   Crystal.objects.get(id=crystal_id).props.remove(prop_id)
   return redirect('detail', crystal_id=crystal_id)