from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from polls.models import Question,Choice
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.utils import timezone
# Create your views here.
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_text')[:5]
    
class DetailView(DetailView):
    model = Question
    template_name ='polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_text__lte=timezone.now())

class ResultView(DetailView):
    model = Question 
    template_name ='polls/results.html'

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question, 'error message': 'choice not selected'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    
