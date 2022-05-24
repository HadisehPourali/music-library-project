from django.shortcuts import render
from django.http import HttpResponse
from song import models


def artist(request):
    artist_list = models.Artist.objects.all()
    context = {'artist_list': artist_list}

    return render(request, 'artist.html', context)
