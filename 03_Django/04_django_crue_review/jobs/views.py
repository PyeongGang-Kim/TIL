from django.shortcuts import render
from .models import Job
from faker import Faker
from decouple import config
import requests
from IPython import embed



# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name') 
    person = Job.objects.filter(name=name).first()

    if person:
        past_job = person.past_job
    else:
        fake = Faker()
        past_job = fake.job()
        person = Job(name=name, past_job=past_job)
        person.save()

    # GIPHY
    #1. API키 가져오기
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1&'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')

    context = {'person': person, 'image': image}

    return render(request, 'jobs/past_life.html', context)
    # try:
    #     name = request.POST.get('name')
    #     job = Job.objects.get(name=name)
    #     #요청 url 세팅
        
    #     try:
    #         image = requets.get(url).json().
    #     except:
    #         image = None
    #     context = {
    #         'past_life': job.past_job,
    #         'name': name,
    #         'image': image,
    #     }
    #     embed()
    #     return render(request, 'jobs/past_life.html', context)
    # except:        
    #     fake = Faker()
    #     job = Job(name=name, past_job=fake.job())
    #     job.save()
    #     url = 'http://api.giphy.com/v1/gifs/search?api_key=' + GIPHY_API_KEY + '&q='+job.past_job+'&limit=1'
    #     try:
    #         image = requets.get(url).json().get('data')[0].get('images').get('original').get('url')
    #     except:
    #         image = None
        
    #     context = {
    #         'past_life': job.past_job,
    #         'name': name,
    #         'image': image,
    #     }
    #     return render(request, 'jobs/past_life.html', context)