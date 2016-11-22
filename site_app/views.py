# -*- coding: utf-8 -*-

"""
Created on 16.11.2016

:author: Alexander Ildyakov
App views
"""

from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from api.models.tr import TransportationRequest
from site_app.forms import RequestForm

import logging

__author__ = 'ildyakov'

logger = logging.getLogger(__name__)


def index(request):
    if request.method == 'GET':
        requests = TransportationRequest.objects.all()
        return render(request, 'site_app/index.html', {'requests': requests})

    logger.log('/ wrong http method')
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

    logger.log('/create_request wrong http method')
    return HttpResponse(status=405)


def view_request(request, request_id):
    if request.method == 'GET':
        item = get_object_or_404(TransportationRequest, pk=request_id)
        return render(request, 'site_app/view_request.html', {'item': item})

    logger.log('/view_request wrong http method')
    return HttpResponse(status=405)
