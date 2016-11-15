from django.db import models
import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length = 65, unique=True)
	slug = models.SlugField(unique = True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('organizer_tag_detail', kwargs={'slug':self.slug})

	def get_update_url(self):
		return reverse('organizer_update_tag', kwargs={'slug': self.slug})


class Startup(models.Model):
	name = models.CharField(max_length = 65, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	# founded_date = models.DateField(verbose_name='Date Published', null=True, blank=True)
	contact = models.EmailField()
	website = models.URLField()
	tags = models.ManyToManyField(Tag)

	class Meta:
		ordering = ['name']
		# get_latest_by = 'founded_date'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('organizer_start_up_detail', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('organizer_start_up_update', kwargs={'slug': self.slug})

class NewsLink(models.Model):
	title = models.CharField(max_length = 65)
	pub_date = models.DateField()
	link = models.URLField()
	startup = models.ForeignKey(Startup)

	def __str__(self):
		return "{}:{}".format(self.title, self.startup)

	def get_absolute_url(self):
		return self.startup.get_absolute_url()

	def get_update_url(self):
		return reverse('organizer_update_newslink', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('organizer_delete_newslink', kwargs={'pk': self.pk})

