from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages

from .forms import RegistrationForm


class RegistrationView(View):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.team = form.cleaned_data.get('team')
            user.save()
            messages.success(request, 'Registration successful')
        return redirect('login')

