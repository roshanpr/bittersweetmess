from django.shortcuts import render
from contact.forms import ContactForm
from django.views.generic import View
from django.contrib.messages import success

# Create your views here.

class ContactView(View):

	form_class = ContactForm
	template_name = 'contact/contact_form.html'

	def get(self, request):
		return render(request, self.template_name, {'form': self.form_class})


	def post(self, request):
		bound_form = self.form_class(request.POST)
		if bound_form.is_valid():
			mail_sent = bound_form.send_email()
			if mail_sent:
				success(request, 'Email sent successfully')
			return redirect('contact')
		return render(request, self.template_name, {'form': bound_form})
