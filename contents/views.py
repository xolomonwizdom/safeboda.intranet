from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Activity

class ActivityList(ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = 'activity.html'


def search(request):
    queryset = Activity.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset,
    }
    return render(request, 'search_results.html', context)
