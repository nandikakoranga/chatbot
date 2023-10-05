from django.shortcuts import render
from django.http import JsonResponse
import openai


# Create your views here.
openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
         model="text-davinci-003",
         prompt=message,
         temperature=0.71,
         max_tokens=256,
         n=1,
         frequency_penalty=0,
         presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
