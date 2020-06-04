from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from products.models import Notification, Question


@method_decorator(login_required, name='dispatch')
class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        recent_notifications = Notification.objects.all()[1:4]
        featured_qns = Question.objects.filter(featured=True)[:3]
        return render(request, self.template_name, {'notifications': recent_notifications, 'questions': featured_qns})