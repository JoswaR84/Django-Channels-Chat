# chat/views.py
from django.shortcuts import render
from .models import ChatMessage

def chat(request):
    messages = ChatMessage.objects.all()
    ctxt = {'messages': messages}
    return render(request, 'chat/chat.html', ctxt)
