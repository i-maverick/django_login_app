from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from . import forms
from . import models

@login_required
def index(request):
    test = models.TestModel.objects.all()
    return render(request, template_name='app/index.html', context={'test': test})


class MainView(FormView):
    form_class = forms.MainForm
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        print(request)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print(request)


def input_text(request):
    data = {'code': 200, 'text': 'Ok'}
    return JsonResponse(data)
