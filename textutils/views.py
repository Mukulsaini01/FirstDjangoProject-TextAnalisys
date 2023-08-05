# Created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

def analize(request):

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    captalize = request.POST.get('captalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    

    if removepunc == "on":
        panchuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""
        for char in djtext:
            if char not in panchuations:
                analized = analized + char
                
        params = {'purpose':'Remove Panchuations' , 'analized_text':analized}
        djtext = analized
        # return render(request, 'analize.html', params)


    
    if captalize == "on":
        analized = ""
        for char in djtext:
            analized = analized + char.upper()
                
        params = {'purpose':'Captalize Text' , 'analized_text':analized}
        djtext = analized
        # return render(request, 'analize.html', params)


    if newlineremover == "on":
        analized = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analized = analized + char
                
        params = {'purpose':'Remove newline' , 'analized_text':analized}
        djtext = analized
        # return render(request, 'analize.html', params)
    


    if spaceremover == "on":
        analized = ""
        for index,char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analized = analized + char
                
        params = {'purpose':'Remove Extra Space' , 'analized_text':analized}
        djtext = analized
        # return render(request, 'analize.html', params)
    


    if charcounter == "on":
        analized = 0
        for char in djtext:
            analized = analized + 1
                
        params = {'purpose':'Character Counter' , 'analized_text':analized}
        djtext = analized
        
       


    # else:
    #     return HttpResponse("Error")
    return render(request, 'analize.html', params)