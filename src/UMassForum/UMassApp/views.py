from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from UMassApp.models import DiscussionPost, SurveyPost
from django.urls import reverse
from django.views import generic

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

class SurveyPostsView(generic.ListView):
	template_name = 'UMassApp/surveypost.html'
	context_object_name = 'postlist'

	def get_queryset(self):
		return SurveyPost.objects.all()

class SPDetailsView(generic.DetailView):
	model = SurveyPost
	template_name = 'UMassApp/spdetails.html'

def vote(request, surveypost_id):
	post = get_object_or_404(SurveyPost, pk=surveypost_id)
	selected_choice = option.get(pk=request.POST['option'])
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('results', args=(post.id,)))

class ResultsView(generic.DetailView):
	model = SurveyPost
	template_name = 'UMassApp/results.html'

# Render the HTML template index.html with the data in the context variable
	#return render(request, "events.html", context=context)
