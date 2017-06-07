# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from polls.models import Drink, Store
from multiselectfield import MultiSelectField
from django.db.models import Avg


# Create your views here.
CATE_CHOICES=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
] 




def multi2(request):
    all_drinks = Drink.objects.all()
    hot = ()
    tea = ()
    matcha = ()
    chew= ()
    juice = ()
    milk_latte = ()
    for drink in all_drinks:
        if CATE_CHOICES[0] in drink.category:
            hot += ((drink.drink_name,drink.store.store_name),)
        elif (CATE_CHOICES[1] in drink.category or CATE_CHOICES[2] in drink.category or
        CATE_CHOICES[3] in drink.category or CATE_CHOICES[4] in drink.category):
            tea += ((drink.drink_name,drink.store.store_name),)
        elif CATE_CHOICES[5] in drink.category:
            matcha += ((drink.drink_name,drink.store.store_name),)
        elif CATE_CHOICES[6] in drink.category:
            chew += ((drink.drink_name,drink.store.store_name),)
        elif CATE_CHOICES[7] in drink.category or CATE_CHOICES[8] in drink.category or CATE_CHOICES[9] in drink.category:
            juice += ((drink.drink_name,drink.store.store_name),)
        elif CATE_CHOICES[10] in drink.category or CATE_CHOICES[11] in drink.category:
            milk_latte += ((drink.drink_name,drink.store.store_name),) 
    context = {
        'hot' : hot,
        'tea' : tea,
        'matcha': matcha,
        'chew': chew,
        'juice': juice,
        'milk_latte': milk_latte,
        'all_drinks': all_drinks,
        'cate': CATE_CHOICES
    }
    return render(request, 'classify/multi.html', context)

def tea(request):
    all_drinks = Drink.objects.all()

    tea = ()
    for drink in all_drinks:
        if (CATE_CHOICES[1] in drink.category or CATE_CHOICES[2] in drink.category or
        CATE_CHOICES[3] in drink.category or CATE_CHOICES[4] in drink.category):
            tea += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'tea' : tea,
        'cate': CATE_CHOICES
    }

    return render(request, 'classify/tea.html',con)


def hot(request):
    all_drinks = Drink.objects.all()

    hot = ()
    for drink in all_drinks:
        if CATE_CHOICES[0] in drink.category:
            hot += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'hot' : hot,
        'cate': CATE_CHOICES
    }

    return render(request, 'classify/hot.html',con)

def chew(request):
    all_drinks = Drink.objects.all()

    chew = ()
    for drink in all_drinks:
        if CATE_CHOICES[6] in drink.category:
            chew += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'chew' : chew,
        'cate': CATE_CHOICES
    }

    return render(request, 'classify/chew.html',con)

def milk(request):
    all_drinks = Drink.objects.all()

    chew = ()
    for drink in all_drinks:
        if CATE_CHOICES[6] in drink.category:
            chew += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'chew' : chew,
        'cate': CATE_CHOICES
    }

    return render(request, 'classify/chew.html',con)

def avg_price(request):
    all_drinks = Drink.objects.all()
    stores = Store.objects.all()
    price = {}
    
    a = Drink.objects.filter(store__store_name = '十杯').aggregate(average_price=Avg('price'))
    b = Drink.objects.filter(store__store_name = '珍煮丹').aggregate(average_price=Avg('price'))
 
    con = {
        'store' : stores,
        'price': price,
        'a': round(a['average_price']),
        'b': b['average_price'],
    }
    
    return render(request, 'classify/price.html',con)



