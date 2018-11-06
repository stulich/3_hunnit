from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from UMassApp.models import DiscussionPost, SurveyPost, UserAccount, Choice
from django.urls import reverse
from django.views import generic
  
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


# # class SurveyPostsView(generic.ListView):
# def surveyResults(request): #surveyResults(request,surveypost_id):
# 	all_surveyposts = SurveyPost.objects.all()

# 	context = {
# 		'all_surveyposts': all_surveyposts, 
# 		# "surveypost_id": surveypost_id,  
# 	}   
# 	# return HttpResponse("<h4>test: " + str(surveypost_id) + "</h4>")
# 	return render(request, 'UmassApp/surveyresults.html', context) 

def discussionPosts(request):
	dposts = DiscussionPost.objects.all()

	context = {
		'dposts': dposts
	}
	return render(request, "discussionposts.html", context=context)
# def getLinkedOptions(post):
# 	choices = Choice.objects.all()
# 	ret_vals = []
# 	for i in choices:	
# 		if i.survey_post == post.title:
# 			ret_vals.append(i)
# 	return ret_vals
  
class SurveyPostsView(generic.DetailView): 
	model = SurveyPost
	template_name = "surveydetails.html"

	# def book_detail_view(request, primary_key):
	# 	print(primary_key)
	# 	try:
	# 		post = SurveyPost.objects.get(id=primary_key)
	# 	except SurveyPost.DoesNotExist:
	# 		raise Http404('Post does not exist')
		
	# 	return render(request, 'surveydetails.html', context={'post': post})
	def get_context_data(self, **kwargs):
		context = super(SurveyPostsView, self).get_context_data(**kwargs)
		context['choices'] = Choice.objects.all()
		# And so on for more models
		return context


class surveyResults(generic.ListView):
	context_object_name = 'survey_list'    
	template_name = 'UMassApp/surveyresults.html'
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
		return context





