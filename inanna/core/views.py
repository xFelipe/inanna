from django.views import View
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate


class Home(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        user = authenticate(username=form.data['username'],
                            password=form.data['password'])
        if not user:
            return render(request, 'login/login.html', {'form': LoginForm()})
        return render(request, 'login/login.html', {'form': form})
