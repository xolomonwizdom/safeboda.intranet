from django.views.generic import ListView

from .models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'