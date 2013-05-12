# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from feedback.forms import FeedbackForm


def show_feedback_form(request, template_name="feedback/feedback_form.html"):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.send_mail()
            url = reverse('catalog_home')
            return HttpResponseRedirect(url)
    else:
        form = FeedbackForm()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
