from django.shortcuts import render


def create_note(request):
    name = request.POST['name']
    content = request.POST['content']

