import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
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
        j = '{"select1": 1, "select2": 2, "select3": 3, "check1": 1, "check3": 1}'
        j1 = json.loads(j)
        print(j1)
        form = self.form_class(initial=j1)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})


def input_text(request):
    data = {'code': 200, 'text': 'Ok'}
    return JsonResponse(data)


def main(request):
    return render_to_response('app/main.html', context={'test': 'test', 'data': 'data'})


def load_test(request):
    id = request.GET['id']
    return HttpResponse(render_to_string('app/load_test.html', context={'id': id}))
