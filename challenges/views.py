from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat more meat",
    "february": "Walk everyday",
    "march": "Eat more chicken",
    "april": "Learn Django",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys()) 
    return render(request, "challenges/index.html",{
        "months":months
    })

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
            "month_name": month
        })
    except:
        raise Http404()
