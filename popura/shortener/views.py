from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from django.http import HttpResponse

from .models import Url


def index(request):
    return HttpResponse("Hello, world.")


def redirect(request, slug):
    try:
        url = Url.objects.get(slug=slug)
    except Url.DoesNotExist:
        return HttpResponseNotFound('Does not exist')

    return HttpResponseRedirect(url.url)