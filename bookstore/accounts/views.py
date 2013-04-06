from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = reverse('catalog_home')
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    page_title = 'User Registration'

    return render_to_response(template_name, locals(),
                          context_instance=RequestContext(request))
