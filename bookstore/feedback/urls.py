from django.conf.urls.defaults import *

urlpatterns = patterns('bookstore.feedback.views',
    (r'^feedback_form/$', 'show_feedback_form' , {'template_name': 'feedback/feedback_form.html'}, 'feedback_form'),
)
