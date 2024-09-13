from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.
def index(request):
    return HttpResponse('Hola mundo!')
def index(request):
    #productos = Producto.objects.all().values() 
    productos = Producto.objects.all()
    #productoS = Producto.objects.filter(puntaje__gte=3) 
    #productoS = Producto.objects.get(pk=1) 
    #return JsonResponse(list(productos), safe=False)
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(
        request, 
        'detalle.html',
        context={'producto': producto},
    )
def formulario(request):
    if request.method == 'POST':        
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )