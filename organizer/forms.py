from django import forms
from .models import Tag, Startup, NewsLink
from blog.models import Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
	# name = forms.CharField(max_length=65)
	# slug = forms.SlugField()

	class Meta:
		model = Tag
		fields = '__all__'

	# def save(self):
	# 	new_tag = Tag.objects.create(
	# 								  name=self.cleaned_data['name'],
	# 								  slug=self.cleaned_data['slug'])
	# 	return new_tag


	def clean_name(self):
		return self.cleaned_data['name'].lower()

	def clean_slug(self):
		new_slug = (self.cleaned_data['slug'].lower())

		if new_slug == 'create':
			raise ValidationError('Slug may not be "create " ')
		return new_slug

class StartupForm(forms.ModelForm):

	class Meta:
		model = Startup
		fields = '__all__'


	def clean_name(self):
		return self.cleaned_data['name'].lower()

	def clean_slug(self):
		new_slug = (self.cleaned_data['slug'].lower())

		if new_slug == 'create':
			raise ValidationError('Slug may not be "create " ')
		return new_slug	

	def clean_contact(self):
		return self.cleaned_data['contact'].lower()

	def clean_website(self):
		return self.cleaned_data['website'].lower()


# class SlugCleanMixin:
# 	""" Mixin class for slug clean method. """

# 	def clean_slug(self):
# 		new_slug = (self.cleaned_data['slug'].lower())

# 		if new_slug == 'create':
# 			raise ValidationError('Slug may not be "create " ')
# 		return new_slug


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

	def clean_slug(self):
		return self.cleaned_data['slug'].lower()


class NewsLinkForm(forms.ModelForm):

	class Meta:
		model = NewsLink
		fields = '__all__'

	def clean_title(self):
		return self.cleaned_data['title'].lower()



