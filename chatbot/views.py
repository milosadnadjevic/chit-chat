from django.shortcuts import render


# Create your views here.
def chtbot(request):
    return render(request, 'chatbot.html')
