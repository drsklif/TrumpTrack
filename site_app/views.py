
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from site_app.models import Request, PropertyType, ParcelSize
from site_app.forms import RequestForm, PropertyTypeForm


__author__ = 'ildyakov'


def index(request):
    if request.method == 'GET':
        requests = Request.objects.all()
        return render(request, 'site_app/index.html', {'requests': requests})
    return HttpResponse(status=405)


def create_request(request):
    if request.method == 'GET':
        c = {
            'form': RequestForm,
        }
        return render(request, 'site_app/create_request.html', c)

    elif request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                item = form.save()

            return redirect(reverse('view_request', kwargs={
                'request_id': item.pk
            }))
        else:
            c = {
                'form': form,
            }
            return render(request, 'site_app/create_request.html', c)
    return HttpResponse(status=405)


def view_request(request, request_id):
    if request.method == 'GET':

        item = Request.objects.filter(
            id=request_id
        ).first()

        if not item:
            raise Http404

        return render(request, 'site_app/view_request.html', {'item': item})
    return HttpResponse(status=405)
