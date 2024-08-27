from django.shortcuts import render, redirect
from .models import NewAllPlant, NewPlant
from .forms import PlantForm, NewPlantForm
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db import models 
from .forms import ImageUploadForm,PlantSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'index.html')

def algae(request):
    # algae_items = NewPlant.objects.filter(type='Algae')
    chloro_items = NewAllPlant.objects.filter(classification='Chlorophyta')
    rho_items = NewAllPlant.objects.filter(classification='Rhodophyta')
    return render(request, 'algae.html', {'chloro_items' : chloro_items, 'rhodo_items' : rho_items})

def bryophytes(request):
    return render(request, 'bryophytes.html')

def gymnosperms(request):
    gymno_items = NewPlant.objects.filter(type='Gymnosperms')
    return render(request, 'gymnosperms.html', {'gymno_items': gymno_items})

def angiosperms(request):
    angio_items = NewPlant.objects.filter(type='Angiosperms')
    return render(request, 'angiosperms.html', {'angio_items': angio_items})

def pteridophytes(request):
    pteri_items = NewAllPlant.objects.filter(classification='Pteridophyte')
    return render(request, 'pteridophytes.html', {'pterido_items': pteri_items})

def monocotyledons(request):
    arac_items = NewAllPlant.objects.filter(classification='Araceae')
    poa_items = NewAllPlant.objects.filter(classification='Poaceae')
    lili_items = NewAllPlant.objects.filter(classification='Liliaceae')
    return render(request, 'monocotyledons.html', {'arac_items': arac_items, 'poa_items': poa_items, 'lili_items': lili_items})

def dicotyledons(request):
    acant_items = NewAllPlant.objects.filter(classification='Acanthacae')
    amar_items = NewAllPlant.objects.filter(classification='Amaryllidaceae')
    lor_items = NewAllPlant.objects.filter(classification='Loranthaceae')
    return render(request, 'dicotyledons.html', {'acant_items': acant_items, 'amar_items' : amar_items, 'lor_items' : lor_items})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('H_backend:upload_image')
    else:
        form = PlantForm()
    return render(request, 'plants/upload_image.html', {'form': form})

# def search_images(request):
#     query = request.GET.get('query')
#     if query:
#         results = NewAllPlant.objects.filter(
#             family_icontains=query 
#         )
#     else:
#         results = NewAllPlant.objects.all()
#     return render(request, 'plants/search_results.html', {'plants': results})

@login_required
def analytics(request):
    # Count the number of plants by family
    family_counts = NewAllPlant.objects.values('family').annotate(total=Count('family')).order_by('-total')

    context = {
        'family_counts': family_counts,
    }

    return render(request, 'plants/analytics.html', context)

def search(request):
    form = PlantSearchForm(request.GET or None)
    results = None

    if form.is_valid():
        name = form.cleaned_data.get('name')
        family = form.cleaned_data.get('family')
        locality = form.cleaned_data.get('locality')
        collector = form.cleaned_data.get('collector')
        collection_date = form.cleaned_data.get('collection_date')

        # Build your query here
        query = NewAllPlant.objects.all()

        if name:
            query = query.filter(scientific_name__icontains=name)
        if family:
            query = query.filter(family__icontains=family)
        if locality:
            query = query.filter(location__icontains=locality)
        if collector:
            query = query.filter(collector__icontains=collector)

        results = query

    return render(request, 'plants/search_results.html', {'form': form, 'results': results})

@login_required
def edit_plant(request, plant_id):
    plant = get_object_or_404(NewAllPlant, id=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)  # Redirect to a detailed view of the plant
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/edit_plant.html', {'form': form, 'plant': plant})

# Delete View
def delete_plant(request, plant_id):
    plant = get_object_or_404(NewAllPlant, id=plant_id)
    if request.method == "POST":
        plant.delete()
        return redirect('plant_list')  # Assuming you have a list page
    return render(request, 'admin/delete_plant.html', {'plant': plant})



@staff_member_required
def custom_admin_dashboard(request):
    Plant = NewAllPlant.objects.all()
    return render(request, 'admin/custom_dashboard.html', {'plants': Plant})
