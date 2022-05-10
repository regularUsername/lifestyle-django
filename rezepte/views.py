from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.db.models.query import QuerySet
from django.db.models import Count, Exists, OuterRef
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from . import models


# class IndexView(generic.ListView):
#     model = models.Rezept
#     context_object_name = 'rezept_liste'
#     template_name = 'rezepte/index.html'


def rezept_favorites(user) -> QuerySet[models.Rezept]:
    user_favs = models.Favorite.objects\
        .filter(user_id=user.id, rezept=OuterRef('pk'))
    r = models.Rezept.objects\
        .annotate(Count("favorite"))\
        .annotate(user_fav=Exists(user_favs))

    return r

ITEMS_PER_PAGE = 4

def index(request: HttpRequest):

    r = rezept_favorites(request.user)

    kat_id = request.GET.get("kat")
    if kat_id and kat_id.isnumeric:
        kat_id = int(kat_id)
        r = r.filter(kategorien=kat_id)

    paginator = Paginator(r, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    rezepte_page = paginator.get_page(page_number)

    # TODO nur die anzeigen für die auch rezepte existieren
    kategorien = models.Kategorie.objects.all()
    return render(request, 'rezepte/index.html',
                  {'rezept_liste': rezepte_page,
                   'kategorien': kategorien,
                   'kat_id': kat_id,
                   'kat_param': f'&kat={kat_id}' if kat_id else ""})


@login_required
def detail_view(request: HttpRequest, pk: int):
    r = rezept_favorites(request.user).get(pk=pk)
    return render(request, 'rezepte/detail.html', {"rezept": r})


# TODO error checking etc.
@login_required
@require_http_methods(["POST"])
def favorite(request: HttpRequest):
    f, created = models.Favorite.objects.get_or_create(
        user=request.user,
        rezept_id=request.POST['rezept_id'])
    if not created:
        print(f"delting: {f}")
        models.Favorite.delete(f)
    else:
        print(f"created: {f}")
    return redirect(request.META.get('HTTP_REFERER'))
