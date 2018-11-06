
Team Members: Harsha Malireddy, Stephen Ulich, Conor Carmichael, Arjun Singh, Monmoy Mohsin 
Video Link: A link to your YouTube video regarding this submission. See below.

Overview:

Our application is a forum for UMASS students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll %, bar chart or pie chart. 

There are some differences in the layout of our webpages from our initial proposal shown in the proposal.md file:

Survey Results Pages: Instead of creating one page where all the survey questions and their answers are displayed, we will direct users to an individual webpage to display each survey's results. 
Discussion Posts Page: The discussion posts page is the same except it will not display comments until the specific post is selected. 
Create Survey Page: The form is the same except we choose to exclude the option for category tags. 
Create Discussion Page: The form is the same except we choose to exclude the option for category tags. 

Design Overview: 
A design overview of your data model as implemented in Django, the important URL routes, and the implemented UI views. Please provide enough detail to demonstrate your team’s understanding of the material.

Models.py: 

We have 5 models in our models.py file: UserAccount, DiscussionPost, CommentSection, SurveyPost, and Choice. 
The UserAccount model contains the first, last, and user_name elements with which each user will be identified by. 
The DiscussonPost model contains the elements title, disc_author, content
 and comment 

Urls.py: 

Views.py: 

Templates: 



Problems/Successes: 
A brief overview of the problems and successes your team encountered. This includes team communication problems/successes, what worked and what didn’t, implementation problems/successes, what worked and what didn’t, and what your team can do to improve collaboration and implementation for the next Project submission.



