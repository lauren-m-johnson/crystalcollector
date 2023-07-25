from django.shortcuts import render

crystals = [
    {'name': 'Quartz', 'hardness': 7, 'structure': 'hexagonal'},
    {'name': 'Calcite', 'hardness': 3, 'structure': 'trigonal'},
    {'name': 'Halite', 'hardness': 2.5, 'structure': 'cubic'},
    {'name': 'Fluorite', 'hardness': 4, 'structure': 'cubic'},
    {'name': 'Diamond', 'hardness': 10, 'structure': 'cubic'},
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    return render(request, 'crystals/index.html', {
        'crystals': crystals
    })