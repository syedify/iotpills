from django.shortcuts import render
from django.http import HttpResponse
import pandas
import json
from .models import Greeting

def printitems(dictObj, indent=0):
    p=[]
    p.append('<ul>\n')
    for k,v in dictObj.iteritems():
        if isinstance(v, dict):
            p.append('<li>'+ str(k).upper()+ ': ')
            p.append(printitems(v))
            p.append('</li>')
        else:
            p.append('<li>'+ str(k).upper()+ ': '+ str(v)+ '</li>')
    p.append('</ul>\n')
    return '\n'.join(p)

# Create your views here.
def index(request):
	#return render(request, "index.html")
	return (HttpResponse("HELLO"))

def portal(request):
	json_data = json.load(open("dummy.json"))
	# df = pandas.DataFrame(data).T
	# df.fillna("-", inplace=True)
	s = printitems(json_data,"")
	# json_str = json.dumps(json_data)
	#close("static/dummy.json")
	return HttpResponse(s)

def stuff(request):
    return render(request, "index.html")

def data(request):
	input = request.input


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

