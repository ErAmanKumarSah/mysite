from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question, Choice
from django.template import loader, context, RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

"""class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
	
		return Question.objects.order_by('-pub_date')[:5]
def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
	        'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))
	
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
				
def detail(request, question_id):
	#return HttpResponse("you're looking at question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question' : question})

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
		
	def results(request, quresponse = "g at the result of question %s."
		#return HttpResponse(response % question_id)
		#question= get_object_or_404(Question, pk=question_id)
		#return render(request,'polls/results.html', {'question': question})

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
    	selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError , Choice.DoesNotExist):
    	#Redisplay the question voting form.
    	return render(request, 'polls/detail.html', {
    		'question' : p,
    		'error_message': "you didn't select any choice.",
    	})
    else:
    	selected_choice.votes +=1
    	selected_choice.save()
    	# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        """
class IndexView(generic.ListView):
	#model = Aboutus
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
    	"""
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



