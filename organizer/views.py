from django.shortcuts import render
from django.http.response import (HttpResponse, Http404)
from django.views.generic import View
from .models import Tag, Startup, NewsLink
from django.template import loader, Context
from django.shortcuts import get_object_or_404, redirect
from .forms import TagForm, StartupForm, NewsLinkForm
from django.core.paginator import Paginator


# def create_tag(request):

	# tag_form = TagForm()
	# if tag_form.is_bound:
		# if tag_form.is_valid():
			

# 	return render(request, 'organizer/create_tag_form.html', {'tag_form': TagForm()})

class TagCreate(View):
	form_class = TagForm
	template_name = 'organizer/create_tag_form.html'

	def get(self, request):
		return render(request, self.template_name, {'form': self.form_class()})

	def post(self, request):
		
		bound_form = self.form_class(request.POST)
		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)
		else:
			return render(request, self.template_name, {'form': bound_form})

class TagUpdate(View):
	form_class = TagForm
	template_name = 'organizer/update_tag_form.html'
	model = Tag

	def get(self, request, slug):
		tag = get_object_or_404(Tag, slug__iexact=slug)
		context = {'form': self.form_class(instance=tag), 'tag': tag}
		return render(request, self.template_name, context)

	def post(self, request, slug):
		tag = get_object_or_404(Tag, slug__iexact=slug)
		bound_form = self.form_class(request.POST, instance=tag)
		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)
		else:
			context = {'form': bound_form, 'tag': tag}
			return render(request, self.template_name, context)



def tag_create(request):

	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			new_tag = form.save()
			return redirect(new_tag)
	else:
		form = TagForm()
		

	return render(request, 'organizer/create_tag_form.html', {'form': form})

def tag_list(request):
	# def get(self, request):

		# tags = Tag.objects.values_list('name', flat=True)
		# tags = Tag.objects.all()

		# result = ", ".join(tag.name for tag in tags)

		# template = loader.get_template('organizer/tag_list.html')
		# context = Context({'tag_list': Tag.objects.all()})
		# output = template.render(context)

		# return HttpResponse(output)

		return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

# Create your views here.

def tag_detail(request, slug):

	print(Tag.objects.values_list('slug', flat=True))
	# try:
	# 	tag = Tag.objects.get(slug__iexact=slug)
	# except Tag.DoesNotExist:
	# 	raise Http404

	tag = get_object_or_404(Tag, slug__iexact=slug)	

	return render(request, 'organizer/tag_detail.html', {'tag':tag})
	
	# template = loader.get_template('organizer/tag_detail.html')
	# context = Context({'tag': tag})
	# output = template.render(context)
	# return HttpResponse(output)

class StartupCreate(View):
	
	form_class = StartupForm
	template_name = 'organizer/create_startup_form.html'

	def get(self, request):
		return render(request, self.template_name, {'form': self.form_class()})

	def post(self, request):
		bound_form = StartupForm(request.POST)
		if bound_form.is_valid():
			new_startup = bound_form.save()
			return redirect(new_startup)
		else:
			return render(request, self.template_name, {'form': bound_form})

class StartupList(View):
	
	paginate_by = 2
	template_name = 'organizer/startup_list.html'

	def get(self, request):
		startups = Startup.objects.all()
		paginator = Paginator(startups, self.paginate_by)
		page = paginator.page(1)
		context = {'startup_list': page, 'paginator': paginator, 'is_paginated': page.has_other_pages()}
		return render(request, self.template_name, context)



def startup_detail(request, slug):
	startup = get_object_or_404(Startup, slug__iexact=slug)
	return render(request, 'organizer/startup_detail.html', {'startup': startup})

class NewsLinkCreate(View):
	form_class =  NewsLinkForm
	template_name = 'organizer/create_newslink_form.html'

	def get(self, request):
		return render(request, self.template_name, {'form': self.form_class})

	def post(self, request):
		bound_form = NewsLinkForm(request.POST)
		if bound_form.is_valid():
			new_news_link = bound_form.save()
			return redirect(new_news_link)
		else:
			return render(request, self.template_name, {'form': bound_form})


class NewsLinkUpdate(View):
	form_class = NewsLinkForm
	template_name = 'organizer/update_newslink_form.html'

	def get(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		context = {'form': self.form_class(instance=newslink), 'newslink': newslink}
		return render(request, self.template_name, context)

	def post(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		bound_form = self.form_class(request.POST, instance=newslink)
		if bound_form.is_valid():
			new_news_link = bound_form.save()
			return redirect(new_news_link)
		else:
			context = {'form': bound_form, 'newslink': newslink}
			return render(request, self.template_name, context)

class NewsLinkDelete(View):
	def get(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		return reverse(request, 'organizer/delete_newslink_form.html', {'newslink': newslink})

	def post(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		startup = newslink.startup
		newslink.delete()
		return redirect(startup)

class StartupUpdate(View):
	form_class = StartupForm
	template_name = 'organizer/update_startup_form.html'

	def get(self, request, slug):
		startup = get_object_or_404(Startup, slug__iexact=slug)
		context = {'form': self.form_class(instance=startup), 'startup': startup}
		return render(request, self.template_name, context)

	def post(self, request, slug):
		startup = get_object_or_404(Startup, slug__iexact=slug)
		bound_form = self.form_class(request.POST, instance=startup)
		if bound_form.is_valid():
			new_startup = bound_form.save()
			return redirect(new_startup)
		else:
			context = {'form': bound_form, 'startup': startup}
			return render(request, self.template_name, context)



















