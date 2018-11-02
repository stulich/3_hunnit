from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from UMassApp.models import DiscussionPost, SurveyPost, UserAccount
from django.urls import reverse
from django.views import generic

# Create your views here.
def index(request):
	"""View function for home page of site."""
	# Generate counts of some of the main objects
	num_discposts = DiscussionPost.objects.all().count()
	num_surveyposts = SurveyPost.objects.all().count()

	print(num_surveyposts)
	# The 'all()' is implied by default.
	num_users = UserAccount.objects.count()

	context = {
	    "num_discposts": num_discposts,
	    "num_surveyposts": num_surveyposts,
	    "num_users": num_users,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, "index.html", context=context)


class SurveyPostsView(generic.ListView):
    model = SurveyPost

    template_name = "surveypost.html"

