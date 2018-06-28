from django.shortcuts import render
from django.http import HttpResponse
import json
from django.apps import apps
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
