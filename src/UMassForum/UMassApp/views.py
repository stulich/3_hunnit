from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from UMassApp.models import DiscussionPost, SurveyPost, UserAccount, Choice, CommentSection
from UMassApp.forms import CreateDForm
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.core.exceptions import *

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
  
# Create your views here.  
def index(request): 
	"""View function for home page of site."""
	# Generate counts of some of the main objects
	num_discposts = DiscussionPost.objects.all().count()
	num_surveyposts = SurveyPost.objects.all().count()

	# The 'all()' is implied by default.
	num_users = UserAccount.objects.count() 

	context = { 
		"num_discposts": num_discposts,
		"num_surveyposts": num_surveyposts, 
		"num_users": num_users, 
	}  

	# Render the HTML template index.html with the data in the context variable
	return render(request, "index.html", context=context)
 
def createsurvey(request):
	num_surveyposts = SurveyPost.objects.all().count()
	context = {'num_surveyposts': num_surveyposts}
	return render(request, 'UmassApp/createsurvey.html', context)

def createDiscussion(request):
	return render(request, "discussionCreation.html")

def surveyPosts(request):
	posts = SurveyPost.objects.all()

	context = {
		'posts' : posts
	}
	return render(request, "surveypost.html", context=context)


def discussionPosts(request):
	dposts = DiscussionPost.objects.all()

	context = {
		'dposts': dposts
	}
	return render(request, "discussionposts.html", context=context)

  
class SurveyPostsView(generic.DetailView): 
	model = SurveyPost
	template_name = "surveydetails.html"

	def get_context_data(self, **kwargs):
		context = super(SurveyPostsView, self).get_context_data(**kwargs)
		context['choices'] = Choice.objects.all()
		# And so on for more models
		return context


class surveyResults(generic.ListView):
	context_object_name = 'survey_list'    
	template_name = 'UmassApp/surveyresults.html'
	queryset = UserAccount.objects.all()

	def get_context_data(self, **kwargs):
		context = super(surveyResults, self).get_context_data(**kwargs)
		context['surveyPosts'] = SurveyPost.objects.all()
		context['choices'] = Choice.objects.all()
		# And so on for more models
		return context

class discussionPosts(generic.ListView):
	context_object_name = 'discussion_list'
	template_name = 'discussionposts.html'
	queryset = UserAccount.objects.all()

	def get_context_data(self, **kwargs):
		context = super(discussionPosts, self).get_context_data(**kwargs)
		context['dposts'] = DiscussionPost.objects.all()
		return context

class discussionDetails(generic.DetailView):
	model = DiscussionPost
	template_name = "discussiondetail.html"

	def get_context_data(self, **kwargs):
		context = super(discussionDetails, self).get_context_data(**kwargs)
		context['comments'] = CommentSection.objects.all()
		return context

class createDiscussion(TemplateView):
	template_name = 'discussionCreation.html'

	def get(self, request):
		form = CreateDForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = CreateDForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.disc_author = request.user.UserAccount
			post.save()
#			DiscussionPost.disc_author = request.UserAccount
#			DiscussionPost.append(post)

			text = form.cleaned_data['title']
			text = form.cleaned_data['content']
		args = {'form': form, 'text': text}
		return redirect('/UMassApp/user/')

class UserGeneralView(generic.ListView):
	context_object_name = 'user_data'
	template_name = 'userindividual.html'
	queryset = UserAccount.objects.all()


	def get_context_data(self, **kwargs):
		context={}
		context['discposts']=(DiscussionPost.objects.filter(disc_author__in=(UserAccount.objects.filter(account=self.request.user))))
		context['surveyposts']=(SurveyPost.objects.filter(survey_author__in=(UserAccount.objects.filter(account=self.request.user))))
		return context

