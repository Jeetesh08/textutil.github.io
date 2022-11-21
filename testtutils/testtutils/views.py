from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    mytext = request.POST.get('text','0')
    removepunc = request.POST.get('removepunc','off')
    alphabate = request.POST.get('charcount','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')

    if removepunc == "on":

        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in mytext:

            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed Punctuations', 'analyzed_text': analyzed}
        mytext = analyzed
        # return render(request, 'analyze.html', params)

    if alphabate == "on":


        i = 0
        for char in mytext:
            i = i + 1


        params = {'purpose': 'Total char count', 'analyzed_text': i}
        mytext = i
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in mytext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        mytext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremove=="on"):
        analyzed = ""
        for char in mytext:
            if char != "\n" and char != "\r":

                analyzed = analyzed+char

        params = {'purpose': 'Removed Newline' , 'analyzed_text': analyzed}
        mytext = analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(mytext) :
            if mytext[index] == " " and mytext[index+1]==" ":
                pass
            else:

                analyzed = analyzed + char
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        mytext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc!="on" and alphabate!="on" and fullcaps != "on" and newlineremove != "on" and spaceremove != "on"):
        return HttpResponse("Error 404")




    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')











