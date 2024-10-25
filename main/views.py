from typing import Any
from .models import User
from django.views import View
from .forms import studentRegistration
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.


class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = studentRegistration()
        data = User.objects.all()

        context = {
            "form": form,
            "data": data
        }

        return context

    def post(self, request):

        form = studentRegistration(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/")


class UserUpdate(View):

    def get(self, request, id):

        user = User.objects.get(pk=id)
        frm = studentRegistration(instance=user)

        return render(request, 'enroll/updatestudent.html', {'form': frm, 'id': id})

    def post(self, request, id):

        user = User.objects.get(pk=id)
        frm = studentRegistration(request.POST, instance=user)

        if frm.is_valid():
            frm.save()

        return HttpResponseRedirect('/')


class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args: Any, **kwargs):

        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
