from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Question,Choice,Questionmaths,Choicemaths
from django.core.serializers import json, serialize
from django.http import JsonResponse
#from django.utils.datastructures import MultiValueDictKeyError



def index(request):
    request.session['gender'] = None
    request.session['vocab']=0
    request.session['maths']=0
    request.session['lives']=2
    request.session['levelvocab']=False
    request.session['levelmaths']=False
    print request.session['gender']
    return render(request,'birds/index.html',{'resp':''})

#def welname(request):
   #return HttpResponse("Hello, world. You're at the birds index.")
 #   return render(request,'birds/welname.html')
def progress(request):
	return render(request,'birds/progress.html')

def wel(request):
	print request.POST.get('name')
	name = request.POST.get('name')
	if(request.method == "POST"):
	    request.session['gender'] = name
#	if 'gender' not in request.session:	
	if(request.session['gender'] == None or request.session['gender']==""):
	    print "now at wel.html"
	    return render(request,'birds/index.html',{'resp':'Please select a character.'})
	else:
	    print "here at welcome.html"
        #prevocab=request.session['vocab']
        #request.session['vocab']=0
	    #request.session['gramm']=0;
	    return render(request,'birds/welcome.html',    )
	
def vocab(request):
	if(request.session['gender'] == None):
	    return render(request,'birds/index.html',{'resp':'Please select a character.'})
	else:    
	    return render(request,'birds/vocab.html')

	
#	return render(request,'birds/questions.html')
# Create your views here.

def detail(request, question_id):
    if(request.session['gender'] == None):
	    return render(request,'birds/index.html',{'resp':'Please select a character.'})
    else:    
        qid=int(question_id)
        if(qid > 2):
            request.session['levelvocab']=True
        else:
            request.session['levelvocab']=False
        print request.session['levelvocab']
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'birds/detail.html', {'question': question})

def vote(request, question_id):
	if(request.session['gender'] == None):
	    return render(request,'birds/index.html',{'resp':'Please select a character.'})
	else: 	
	    question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.GET['choice'])
    	except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
            print "key error"
            return JsonResponse({'resp':'KeyError','error_message': "You didn't select a choice."})
        else:
            if(selected_choice.ans):
	    		request.session['vocab']=request.session['vocab']+1
	    		print request.session['vocab']
        		return JsonResponse({'resp':'true','life':request.session['lives']})
            else:
            	request.session['lives']=request.session['lives']-1
            	print request.session['lives']
            	if (request.session['lives'] == 0):
            	    request.session['vocab']=0
            	    request.session['lives']=2
                    c=question.choice_set.get(ans=True)
                    return JsonResponse({'resp':'false','life':request.session['lives'],'ans':c.choice_text})
                else:
                    return JsonResponse({'resp':'wrong answer','life':request.session['lives']})

def maths(request):
    if(request.session['gender'] == None):
        return render(request,'birds/index.html',{'resp':'Please select a character.'})
    else:    
        return render(request,'birds/mathematics.html')


def detailmaths(request, question_id):
    if(request.session['gender'] == None):
        return render(request,'birds/index.html',{'resp':'Please select a character.'})
    else:    
        qid=int(question_id)
        if(qid > 2):
            print ">2 level is "
            request.session['levelmaths']=True
        else:
            print "<2 level is "
            request.session['levelmaths']=False
        print request.session['levelmaths']
        question = get_object_or_404(Questionmaths, pk=question_id)
        return render(request, 'birds/detailmaths.html', {'question': question})

def votemaths(request, question_id):
    if(request.session['gender'] == None):
        return render(request,'birds/index.html',{'resp':'Please select a character.'})
    else:   
        question = get_object_or_404(Questionmaths, pk=question_id)
        try:
            selected_choice = question.choicemaths_set.get(pk=request.GET['choice'])
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
            print "key error"
            return JsonResponse({'resp':'KeyError','error_message': "You didn't select a choice."})
        else:
            if(selected_choice.ans):
                request.session['maths']=request.session['maths']+1
                print "marks in maths is:"
                print request.session['maths']
                return JsonResponse({'resp':'true','life':request.session['lives']})
            else:
                request.session['lives']=request.session['lives']-1
                print request.session['lives']
                if (request.session['lives'] == 0):
                    request.session['maths']=0
                    request.session['lives']=2
                    print question.choicemaths_set.get(ans=True)
                    c=question.choicemaths_set.get(ans=True)
                    return JsonResponse({'resp':'false','life':request.session['lives'],'ans':c.choice_text})
                else:
                    return JsonResponse({'resp':'wrong answer','life':request.session['lives']})




       #selected_choice.save()
        #return render(request,'birds/results.html', {'choice':selected_choice,}) 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
       # return HttpResponseRedirect(reverse('birds:results', args=(1)))

'''
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    q=Question.objects.get('pk=1')[:2]
    template = loader.get_template('polls/questions.html')
    context = {
        'question': q,
    }
    return HttpResponse(template.render(context, request))
'''