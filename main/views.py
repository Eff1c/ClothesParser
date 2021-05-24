from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Clothing, ClothingSex, ClothingType

class IndexView(generic.ListView):
    paginate_by = 8
    model = Clothing
    template_name = 'main/index.html'
    context_object_name = 'page_obj'


def index(request, sex=None, clothing_type=None):
    if sex:
        sex_obg = get_object_or_404(ClothingSex, sex=sex)
        if clothing_type:
            clothing_type_obg = get_object_or_404(ClothingType, name=clothing_type)
            clothing = get_list_or_404(Clothing, sex=sex_obg.id, type=clothing_type_obg.id)

        else:
            clothing = get_list_or_404(Clothing, sex=sex_obg.id)

    else:
        clothing_type_obg = get_object_or_404(ClothingType, name=clothing_type)
        clothing = get_list_or_404(Clothing, type=clothing_type_obg.id)

    paginate_by = 8
    paginator = Paginator(clothing, paginate_by)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/index.html', {
        'page_obj': page_obj,
    })


class About(generic.ListView):
    model = Clothing
    template_name = 'main/about.html'


def search(request):
    query = request.GET.get('q')
    clothing = Clothing.objects.filter(name__icontains=query)

    paginate_by = 8
    paginator = Paginator(clothing, paginate_by)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'main/index.html',
        {
            'page_obj': page_obj,
            'query': query,
        }
    )