from django.db import models
from organizer.models import Tag, Startup
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 65, unique=True)
	slug = models.SlugField(help_text='Label for URL Configuration', unique_for_month='pub_date')
	text = models.TextField()
	pub_date = models.DateField('date published', auto_now_add=True)

	tags = models.ManyToManyField(Tag, related_name='blog_post')
	startups = models.ManyToManyField(Startup, related_name='blog_post')

	class Meta:
		ordering = ['-pub_date', 'title']

	def __str__(self):
		return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

	def get_absolute_url(self):
		return reverse('blog_post_detail', kwargs={'year': self.pub_date.year,
													'month': self.pub_date.month,
													'slug': self.slug})

	def get_update_url(self):
		return reverse('blog_post_update', kwargs={'year': self.pub_date.year,
													'month': self.pub_date.month,
													'slug': self.slug})

	def get_delete_url(self):
		return reverse('blog_post_delete', kwargs={'year': self.pub_date.year,
													'month': self.pub_date.month,
													'slug': self.slug})