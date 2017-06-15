from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question, Drink, Store
from multiselectfield import MultiSelectField
from django.db.models import Avg
from operator import itemgetter
import random



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/home.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    q = Question.objects.get(id=question_id)
    question = q.choice_set.all().order_by('-votes')
    return render(request, 'polls/results.html', {'question': question, 'q':q})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def about(request):
    return render(request, 'polls/about.html')

def find(request):
    CATE_CHOICES=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
    ] 
    
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

    teas = list(tea)
    chews = list(chew)
    juices = list(juice)
    lattes = list(milk_latte)
    random.shuffle(teas)
    random.shuffle(chews)
    random.shuffle(juices)
    random.shuffle(lattes)
    context = {
        'hot' : hot,
        'tea' : teas,
        'matcha': matcha,
        'chew': chews,
        'juice': juices,
        'milk_latte': lattes,
        'all_drinks': all_drinks,
        'cate': CATE_CHOICES
    }
    return render(request, 'polls/find.html',context)

def brand(request):
    all_drinks = Drink.objects.all()
    stores = Store.objects.all()
    price = {}
    
    a = Drink.objects.filter(store__store_name = '十杯').aggregate(average_price=Avg('price'))
    b = Drink.objects.filter(store__store_name = '珍煮丹').aggregate(average_price=Avg('price'))
    c = Drink.objects.filter(store__store_name = '陳三鼎').aggregate(average_price=Avg('price'))
    d = Drink.objects.filter(store__store_name = 'SOMA').aggregate(average_price=Avg('price'))
    e = Drink.objects.filter(store__store_name = '九品川').aggregate(average_price=Avg('price'))
    f = Drink.objects.filter(store__store_name = 'Bobii Frutii').aggregate(average_price=Avg('price'))
    g = Drink.objects.filter(store__store_name = '波囍').aggregate(average_price=Avg('price'))
    h = Drink.objects.filter(store__store_name = '花甜果室').aggregate(average_price=Avg('price'))
 
    con = {
        'store' : stores,
        'price': price,
        'a': round(a['average_price']),
        'b': round(b['average_price']),
        'c': round(c['average_price']),
        'd': round(d['average_price']),
        'e': round(e['average_price']),
        'f': round(f['average_price']),
        'g': round(g['average_price']),
        'h': round(h['average_price']),
    }
    
    return render(request, 'polls/brandbrowse.html',con)


def rankboard(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    store = question.choice_set.all()
    choice =  Choice.objects.filter(question_id=3)
    vote = []
    for i in choice:
        vote.append(i.votes)

    ch = ()
    for choice in question.choice_set.all():
        ch += ((choice.choice_text,choice.votes),)

    ch = sorted(ch, key=lambda tup: tup[1],reverse=True)
    chs =list(ch)
    con ={
        'choices': chs,
        'question': question,
        'store':store,
        'vote':vote,
    }
    return render(request, 'polls/rankboard.html', con)


def store1(request):
    return render(request, 'polls/store1.html')

def store2(request):
    return render(request, 'polls/store2.html')

def store3(request):
    return render(request, 'polls/store3.html')

def store4(request):
    return render(request, 'polls/store4.html')

def store5(request):
    return render(request, 'polls/store5.html')

def store6(request):
    return render(request, 'polls/store6.html')

def store7(request):
    return render(request, 'polls/store7.html')

def store8(request):
    return render(request, 'polls/store8.html')

def store9(request):
    return render(request, 'polls/store9.html')

def store10(request):
    return render(request, 'polls/store10.html')
