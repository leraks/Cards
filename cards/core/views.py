import string
from datetime import timedelta
import random
from django.shortcuts import render, redirect
from django.utils import timezone
from .def_views.randStr import randStr
from .models import Card
from django.core.exceptions import ObjectDoesNotExist
from .form import *


def search(request):
    if request.method == "POST":
        number = str(request.POST.get('Number'))
        cvc = request.POST.get('CVC')
        if (12 < len(number) < 20 and len(str(cvc)) == 3) and (number.isdigit() and cvc.isdigit()):
            try:
                find_card = Card.objects.filter(cvc=cvc).get(number_cart=number)
                orders = find_card.purchase_set.order_by("-id")[0:5]
                context = {'find_card': find_card, 'orders':orders}
                return render(request, 'core/card.html', context)
            except ObjectDoesNotExist:
                error = "Карта не найдена"
                context = {'error': error}
                return render(request, 'core/search.html', context)
        else:
            error = "Карта не найдена или заданна неверные данные в поля"
            context = {'error': error}
            return render(request, 'core/search.html', context)

    elif request.method == "GET":
        context = {}
        return render(request, 'core/search.html', context)


def create_card(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        set_numbers_card = set()
        date_add = timedelta(days=1)
        obj_card = Card.objects.all()

        if form.is_valid():
            while len(set_numbers_card) < form.cleaned_data['number_of_generated']:
                number = randStr(N=int(form.cleaned_data['number_of_digits_series']))
                if not obj_card.filter(number_cart=number):
                    set_numbers_card.add(number)

            if form.cleaned_data['choice_date_active_field'] == '1':
                date_add = timedelta(days=365)
            elif form.cleaned_data['choice_date_active_field'] == '2':
                date_add = timedelta(days=180)
            elif form.cleaned_data['choice_date_active_field'] == '3':
                date_add = timedelta(days=30)

            for i in set_numbers_card:
                card = Card.objects.create(
                    cvc=form.cleaned_data['cvc'],
                    number_cart=i,
                    date_stop=timezone.now() + date_add,
                    amount_cash=0,
                )

                card.save()

            return redirect('search')
    else:
        form = CreateForm()
    return render(request, 'core/create_card.html', {'form': form})
