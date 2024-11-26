from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat more meat",
    "february": "Walk everyday",
    "march": "Eat more chicken",
    "april": "Learn Django"
}

def index(request):
    list_items=""
    months = list(monthly_challenges.keys()) 
    for month in months:
        redirect_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{redirect_path}\">{month}</a></li>"
    return HttpResponse(list_items)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Wrong Month")
    
    redirect = months[month]
    redirect_path = reverse("month-challenge", args=[redirect])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("Wrong Month")
