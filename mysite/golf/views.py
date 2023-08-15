from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseRedirect

# Create your views here.


def accept(request):
    if request.method == 'POST':
        course = request.POST.get('course', '')
        score = request.POST.get('score', '')
        fairways = request.POST.get('fairways', '')
        putts = request.POST.get('putts', '')
        greens = request.POST.get('greens', '')
        pars = request.POST.get('pars', '')
        birdies = request.POST.get('birdies', '')
        summary = request.POST.get('summary', '')
        profile = Profile(course=course, score=score, fairways=fairways, putts=putts, greens=greens, pars=pars,
                          birdies=birdies, summary=summary)
        profile.save()
        return HttpResponseRedirect('/')
    else:
        golf_round = Profile.objects.all()

    return render(request, 'golf/accept.html', {'golf_round': golf_round})


def clear(request):
    Profile.objects.all().delete()
    return render(request, 'golf/accept.html')

