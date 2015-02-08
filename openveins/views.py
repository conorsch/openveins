from django.shortcuts import render_to_response
from openveins.models import Quote


def home(request):
    quotes = Quote.objects.all()
#    quotes = quotes[0:2]
    return render_to_response(
        'index.html',
        {'quotes': quotes},
    )
