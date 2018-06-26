# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Training
from django import forms


class TrainingListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('name', 'name asc'),
        ('-name', 'name desc'),
        ('trainer', 'trainer'),
        ('data', 'data'),
        ('id', 'id')
    ), required=False)
    search = forms.CharField(required=False)


def training_list(request):
    trainings = Training.objects.all()
    form = TrainingListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            trainings = trainings.order_by(data['sort'])
        if data['search']:
            trainings = trainings.filter(name=data['search'])

    context = {
        'trainings': trainings,
        'trainings_form': form
    }
    return render(request, 'training_list.html', context)


def training_detail(request, pk):
    context = {
        'training': get_object_or_404(Training,id=pk)
    }
    return render(request, 'training_detail.html', context)
