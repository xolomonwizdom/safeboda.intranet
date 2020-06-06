from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import ProductType, Question

class ProductListView(ListView):
    model = ProductType
    context_object_name = 'products'
    template_name = 'products.html'


@method_decorator(login_required, name='dispatch')
class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'faq.html'