from django.shortcuts import render

from .models import foto

from django.core.paginator import Paginator
# Create your views here.

def product(request):
        datos=foto.objects.all()
        paginator = Paginator(datos, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request,'product/product.html',{"page_obj": page_obj} )
