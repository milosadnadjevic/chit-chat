from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_apikey = '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'
openai.api_key = openai_apikey

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop='None',
        temperature=0.7,
    )
    
    answer = response.choices[0].text.strip()
    return answer

# Create your views here.
def chtbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
