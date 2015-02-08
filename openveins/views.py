from django.shortcuts import render_to_response
from django.template import RequestContext
from openveins.models import Quote
from endless_pagination.decorators import page_template


@page_template('quote_iteration.html')
def home(
        request,
        template='index.html',
        extra_context=None):
    context = {
        'quotes': Quote.objects.all(),
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))

def home_orig(request):
    quotes = Quote.objects.all()
#    quotes = quotes[0:2]
    return render_to_response(
        'index.html',
        {'quotes': quotes},
    )
