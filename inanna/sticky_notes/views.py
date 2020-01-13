from django.shortcuts import render


# Create your views here.
def hello_notes(request):
    result = {'notes': [
        {
            'title': 'Primeiro lembrete',
            'content': 'Este é meu primeiro lembrete.'
        },
        {
            'title': 'Segundo lembrete',
            'content': 'Este é meu segundo lembrete.'
        },
        {
            'title': 'Terceiro lembrete',
            'content': 'Este é meu terceiro lembrete.'
        }
    ]}
    return render(request, 'notes/notes.html', result)

