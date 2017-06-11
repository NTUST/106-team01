from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question, Drink, Store

# Create your views here.
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

def about(request):
    return render(request, 'polls/about.html')

def drinkbar2(request):
    return render(request, 'polls/drinkbar2.html')

def drinkbarcolor(request):
    return render(request, 'polls/drinkbarcolor.html')

def find(request):
    return render(request, 'polls/find.html')

def information(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/information.html', {'question': question})

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
    
def tea(request):
    all_drinks = Drink.objects.all()
    cate=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
    ] 
    tea = ()
    store = ()
    for drink in all_drinks:
        if cate[6] in drink.category:
            tea += ((drink.drink_name,drink.store.store_name),)
    
    con = {
        'tea' : tea,
    }

    return render(request, 'polls/tea.html',con)
    
def multi(request):
    CATE_CHOICES=[
        '招牌','茶類','奶茶類','果茶類','特調茶類','抹茶類','嚼勁口感類','果汁類','水果類','奶,果昔類','鮮奶類','拿鐵類'  
    ]    

    all_drinks = Drink.objects.all()
    context = {
        'all_drinks': all_drinks,
        'cate': CATE_CHOICES
    }
    return render(request, 'polls/multiselect.html', context)

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
