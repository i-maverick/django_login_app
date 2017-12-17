from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


@login_required
def index(request):
    test = models.TestModel.objects.all()
    return render(request, template_name='app/index.html', context={'test': test})
