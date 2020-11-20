from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required()
def home(requests):
    data = {'usuario': requests.user}
    return render(requests, 'core/index.html', context=data)
