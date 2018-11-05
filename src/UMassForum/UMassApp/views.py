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

def surveyPosts(request):
	posts = SurveyPost.objects.all()

	context = {
		'posts' : posts
	}
	return render(request, "surveypost.html", context=context)


# class SurveyPostsView(generic.ListView):
def surveyResults(request): #surveyResults(request,surveypost_id):
	all_surveyposts = SurveyPost.objects.all()

	context = {
		'all_surveyposts': all_surveyposts, 
		# "surveypost_id": surveypost_id,  
	}   
	# return HttpResponse("<h4>test: " + str(surveypost_id) + "</h4>")
	return render(request, 'UmassApp/surveyresults.html', context) 

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
  
class SurveyPostsView(generic.ListView): 
    model = SurveyPost
 
    template_name = "surveypost.html"
