from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from . import models



def index(request: HttpRequest):
    v = models.Video.objects.all()
    v = list(v)*20
    paginator = Paginator(v, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'videos/index.html', {'page_obj': page})


def detail_view(request: HttpRequest, pk: int):
    return render(request, 'videos/detail.html',
                  {'video': models.Video.objects.get(pk=pk)})
