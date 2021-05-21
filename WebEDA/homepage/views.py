from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views import generic, View


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        graph = {}
        return render(request, 'index.html', graph)
