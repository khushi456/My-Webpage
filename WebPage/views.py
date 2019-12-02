#I have created this file - khushi

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'index.html')

def analyze(request):
	djtext = request.POST.get('text','default')
	print(djtext)
	removepunc = request.POST.get('removepunc',"off")
	uppercase = request.POST.get('uppercase','off')
	lowercase = request.POST.get('lowercase','off')
	newlineremover = request.POST.get('newlineremover','off')
	if removepunc == "on":
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ""

		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char

		params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
		djtext=analyzed
		
	if uppercase=='on':
		analyzed =""
		for char in djtext:
			analyzed += char.upper()

		params = {'purpose':'uppercase', 'analyzed_text': analyzed}
		djtext=analyzed
		
	if lowercase=='on':
		analyzed =""
		for char in djtext:
			analyzed += char.lower()

		params = {'purpose':'lowercase', 'analyzed_text': analyzed}
		djtext=analyzed

	if newlineremover == "on":
		analyzed = ""
		for char in djtext:
			if char != "\n" and char!="\r":
				analyzed = analyzed + char
			else:
				print("no")
		
		params = {'purpose':'lowercase', 'analyzed_text': analyzed}
		djtext=analyzed

	if(removepunc != "on" and uppercase != "on" and lowercase != "on" and newlineremover!='on'):
		return HttpResponse("ERROR!")

	return render(request,'analyze.html',params)

def ex1(request):
	s = '''<h1>Navigation bar</h1><br>
		<a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-11"> Code with harry bhai</a><br>
		<a href="https://www.youtube.com/watch?v=2Qn2uHpl3Pk">Youtube</a><br>
		<a href="https://www.codechef.com/certification/data-structures-and-algorithms/prepare#foundation">Codechef </a>
		'''
	return HttpResponse(s)

