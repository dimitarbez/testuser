from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):

    context = {}

    return render(request, 'food/index.html', context)


def out_of_stock(request):

    if request.method == 'POST':
        form_data = ProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            product: Product = form_data.save(commit=False)
            product.user = request.user
            product.image = form_data.cleaned_data['image']
            product.save()
            return redirect('/index/')

    products = Product.objects.filter(quantity=0).filter(
        category__is_active=True
    ).all()

    form = ProductForm()

    return render(request, 'food/outofstock.html', {'products': products, 'form': form})
