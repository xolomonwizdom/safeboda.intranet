from django.shortcuts import render
from django.views.generic import ListView
from .models import Document


class DocumentListView(ListView):
    model = Document
    template_name = 'files.html'
    context_object_name = 'docs'
