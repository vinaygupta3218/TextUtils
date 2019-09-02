from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext= request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    spaceremover= request.POST.get('spaceremover','off')
    lowercase = request.POST.get('lowercase', 'off')

    if removepunc =="on":

        punctuations = '''!()-[]{};-=;,.'`<>!:'"/?@$%^&*_'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(lowercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Change to Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed=analyzed + char
        params = {'purpose':'Removed New Lines','analyzed_text':analyzed}
        djtext = analyzed

    if(spaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
          if not(djtext[index] ==" " and djtext[index+1] ==" "):
              analyzed=analyzed+char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}


    if(removepunc !="on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
