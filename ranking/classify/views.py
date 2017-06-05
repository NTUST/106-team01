from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from polls.models import Drink, Store
# Create your views here.
CATE_CHOICES=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
] 
def multi2(request):
    all_drinks = Drink.objects.all()
    context = {
        'all_drinks': all_drinks,
        'cate': CATE_CHOICES
    }
    return render(request, 'classify/multi.html', context)

def tea(request):
    all_drinks = Drink.objects.all()
    cate=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
    ] 
    tea = ()
    store = ()
    for drink in all_drinks:
        if cate[1] in drink.category or cate[2] in drink.category or cate[3] in drink.category or cate[4] in drink.category:
            tea += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'tea' : tea,
        'cate': cate
    }

    return render(request, 'classify/tea.html',con)