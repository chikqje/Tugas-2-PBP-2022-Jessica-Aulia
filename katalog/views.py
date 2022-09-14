from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    list_item = CatalogItem.objects.all()
    context = {
    'list_item': list_item,
    'nama': 'Jessica Aulia',
    'NPM': '2106633512'
}
    return render(request, "katalog.html",context)
