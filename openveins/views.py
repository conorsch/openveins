from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from openveins.models import Quote
from openveins.forms import QuoteForm
from django.views.generic import CreateView
from braces.views import LoginRequiredMixin
from vanilla import UpdateView
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


def about(request, template='index.html', extra_context=None, **kwargs):
    context = {
        'quotes': Quote.objects.all().order_by('post_date')[:1],
    }
    return home(request, template, extra_context=context, **kwargs)


class QuoteUpdateView(UpdateView):
    model = Quote
    template_name = "quote_form.html"


class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = "quote_form.html"

    def get_form_class(self):
        return QuoteForm

    def get_success_url(self):
        return reverse_lazy('home')
