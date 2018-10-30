from django.shortcuts import render
from django.http import HttpResponse
from UMassApp.models import DiscussionPost

# Create your views here.
def test(request):
	return HttpResponse('Hello, World')

def discussionPosts(request):
	print("Being called")
	num_posts= DiscussionPost.objects.all().count()
	print(num_posts)
	context = {"num_posts": num_posts,
		}
	return HttpResponse(context)

# Render the HTML template index.html with the data in the context variable
	#return render(request, "events.html", context=context)