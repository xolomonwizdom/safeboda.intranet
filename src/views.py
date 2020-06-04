from django.views.generic import View
from django.shortcuts import render
from products.models import Notification, Question


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        recent_notifications = Notification.objects.all()[1:4]
        featured_qns = Question.objects.filter(featured=True)[:3]
        return render(request, self.template_name, {'notifications': recent_notifications, 'questions': featured_qns})