from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges = {
    "january": "Eat more meat",
    "february": "Walk everyday",
    "march": "Eat more chicken",
    "april": "Learn Django"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Wrong Month")
    
    redirect = months[month]
    return HttpResponseRedirect("/challenges/" + redirect)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Wrong Month")
    return HttpResponse(challenge_text)