from django.views.generic import ListView

from .models import Product, Question

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'


class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'faq.html'