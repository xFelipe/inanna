from django.shortcuts import render
from .models import StickyNotes


# Create your views here.
def hello_notes(request):
    notes = StickyNotes.objects.all()
    result = {'notes': notes}
    return render(request, 'notes/notes.html', result)
