from django.shortcuts import render
from IPython import embed
from .models import users

# Create your views here.
def index(request):
    embed()
    return render(request, 'dbcrud.html')