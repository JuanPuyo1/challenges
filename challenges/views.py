from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This workds!"
    elif month == "february":
        challenge_text = "Walk More"
    else:
        HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)