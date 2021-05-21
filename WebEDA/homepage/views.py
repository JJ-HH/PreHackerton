from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.conf import settings

import os
import json


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})
        # return render(request, 'index.html', {"graph":graph})
