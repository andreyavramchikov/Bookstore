from django import forms
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage


class FeedbackForm(forms.Form):
    email = forms.CharField(label=u'Email', max_length=50)
    topic = forms.CharField(label=u'Topic', max_length=200)
    response = forms.CharField(label=u'Response', max_length=500,
                               widget=forms.Textarea({'rows': 5, 'cols': 30}))

    def send_mail(self):


        context = {'fields': {}}
        for name, field in self.fields.iteritems():

            context['fields'][name] = self.cleaned_data.get(name, None)

        message = render_to_string('feedback/feedback_message.txt', context)



        subject = 'mail' + u'feedback'
        recepients = ('aldrson@gmail.com',)
        msg = EmailMessage('ls', message, 'aldrson@gmail.com', recepients, headers={})
        msg.send()
        # mail_managers(subject, message, fail_silently=False)