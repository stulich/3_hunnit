
Team Members: Harsha Malireddy, Stephen Ulich, Conor Carmichael, Arjun Singh, Monmoy Mohsin, Kyle Ewell
Video Link: A link to your YouTube video regarding this submission. See below.

Overview:

Our application is a forum for UMASS students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll %, bar chart or pie chart. 

There are some differences in the layout of our webpages from our initial proposal shown in the proposal.md file:

Survey Results Pages: Instead of creating one page where all the survey questions and their answers are displayed, we will direct users to an individual webpage to display each survey's results. 
Discussion Posts Page: The discussion posts page is the same except it will not display comments until the specific post is selected. 
Create Survey Page: The form is the same except we choose to exclude the option for category tags. 
Create Discussion Page: The form is the same except we choose to exclude the option for category tags. 
 
Design Overview: A design overview of your data model as implemented in Django, the important URL routes, and the implemented UI views. Please provide enough detail to demonstrate your team’s understanding of the material.
Models.py: 

We have 5 models in our models.py file: UserAccount, DiscussionPost, CommentSection, SurveyPost, and Choice. 
The UserAccount model identifies different users, the DiscussionPost and SurveyPost models contain elements related to a discussion post and survey post respectively. The comment section model is associated with the comments contained under the discussion posts. The choice model is associated with the MC options that the user can pick when answering a survey post. 

Urls.py: Whenever a user visits a url, this file will recognize it and dictate what the webpage will display based on the method invoked in the views.py file. This method is listed as the second parameter in the path method of this file. . 

Views.py: This file contains methods that refers to the appropriate html template file each is associated with, and returns the webpage created in the html file. 

Templates: The templates files create the webpages of our site. We have 2 templates for the discussion creation and discussion posts and another 2 templates for survey creation and survey posts. We have an additional 2 templates titled surveydetails.html and discussiondetails.html. These templates extend the base.html file that give the overall structure to the site.  

Problems/Successes: A brief overview of the problems and successes your team encountered. This includes team communication problems/successes, what worked and what didn’t, implementation problems/successes, what worked and what didn’t, and what your team can do to improve collaboration and implementation for the next Project submission.

We had no problems at all; we’re perfect.
One of the first issues we had was an issue with our database that did not allow us to connect choices to a survey. We also had an issue with waiting til the last second because we’re lazy. 





