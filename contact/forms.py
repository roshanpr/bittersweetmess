from django import forms
from django.core.mail import BadHeaderError, mail_managers
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):

	email = forms.EmailField(initial='youremail@domain.com')
	text = forms.CharField(widget=forms.Textarea)

	FEEDBACK = 'F'
	CORRECTION = 'C'
	SUPPORT = 'S'

	REASON_CHOICES = (
						(FEEDBACK, 'Feedback'),
						(CORRECTION, 'Correction'),
						(SUPPORT, 'Support'),
					)
	reason = forms.ChoiceField(choices=REASON_CHOICES, initial=FEEDBACK)

	def send_email(self):
		email = self.cleaned_data.get('email')
		text = self.cleaned_data.get('text')
		reason = self.cleaned_data.get('reason')

		reason_dict = dict(self.REASON_CHOICES)
		full_reason = reason_dict.get('reason')

		body = 'Message From: {}\n\n {}\n'.format(email, text)

		try:
			mail_managers(full_reason, body)
		except BadHeaderError:
			self.add_error(
							None, ValidationError(
													'Could Not Send Email\n'
													'Extra headers not allowed', code='badheader'))
			return False
		else:
			return True


