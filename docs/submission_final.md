#Team 3_Hunnit
#Umass Forum
#Fall 2018

# Overview (perhaps add a little to top para about most recent changes?)
Our application is a forum for UMass students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll percentage, bar chart or pie chart. The aim is to provide more ways for UMass students to communicate, and to see how the community at large feels on certain topics. 

Our web app is particularly innovative in the way it can collect relevant data and present it in a clean and efficent way. Our web app is also much better at creating a sense of community when compared to other similar platforms like Reddit or Yahoo. The information shared on our platform will be made by Umass students for Umass students in a way that hasnt been done before. 


# Team Members
* Conor Carmichael
* Stephen Ulich
* Monmoy Mohsin
* Harsha Malireddy
* Arjun Singh
* Kyle Ewell


# Video Link
Video Link: 


# Design Overview
For this submission Django user accounts were created, allowing login/logout functionality simmilair to the examples done in class. The users were created in the init.py file. Since we already had a UserAccount model created which was linked to other datatypes we had to link the new users to the existing user accounts with a one to one mapping which included changing the model of userAccount to accept a user as a one to one field. 

For user interaction, we used Django forms to implement fields that users can use to create and update discussion posts. In our template, we checked to see whether a user is authenticated, is a superuser, or is neither of those. This allowed us to handle each case, by directing authorized users to the form, throwing a message to superusers to use the admin site, and throwing a message to log in for users.

In terms of functionality, we decided that users will not be allowed to modify survey posts because it could lead to dishonest data and would defeat the purpose of allowing surveys. We also decided to not allow users to delete posts because they could delete useful information in their posts or in the responses. Only admins will be allowed to delete posts if the content is deemed inappropriate.


# User Interface 

![HomePage IMG](docs/imgs/homepage.png "HomePage")
Pretty straightforward, that this is the main landing page when a user first logs in to the site

![Login IMG](docs/imgs/login.png "Login")
This is what the user will see when they attempt to login within the site

![Logout IMG](docs/imgs/logout.png "Logout")
This is what the user will see when they logout of the site

![discussionPage IMG](docs/imgs/discussionPage.png "Discussions")
This is the main discussions page that displays all the latest discussion posts. This particular UI is meant to filter by 'most recent' and all user posts would end up here, functionlaity will be added in future to be able to keep posts private or to specific users.

![surveyPage IMG](docs/imgs/surveyPage.png "Surveys")
Similar to the discussion page above, mainly meant to just present the surveys created by all users on the site. Also allows users to vote live on page and see results. 

![yourPosts IMG](docs/imgs/yourPosts.png "Your Posts")
Page that displays all personal contributions to the site.

![discussionForm IMG](docs/imgs/discussionForm.png "Discussion Form")
The page that holds the form to submit one of the discussions to be promoted to the front page


# Data Model: (HELP)
(A final up-to-date diagram of your data model including a brief description of each of the entities in your model and their relationships.)


# URL Routes/Mappings (HELP)
(A final up-to-date table of all the URL routes that your application supports and a short description of what those routes are used for. You should also indicate any authentication and permissions on those routes.)

|  Urls    |     Description                                                                                             |
|----------|:-----------------------------------------------------------------------------------------------------------:|
| “”                                              | This is the homepage of the website.                                 |                                        
|"surveyposts/"                                   | This page displays the list of survey posts.                         |                            
|"createsurvey/"                                  | This goes to a form to create a survey.                              |                               |"discussionposts/"                               | This page displays the list of discussion posts.                     |                            
|"surveyresults/".                                | This page displays the list of survey posts with the option of       |
|                                                    picking an nswer choice.                                            |                 
|"discussioncreation/"                            | This goes to a form to create a discussion.                          |       
|r'^surveyresults/(?P<pk>[0-9A-Fa-f-]+)'          | This displays the survey results of each individual survey post.     |       
|r'^discussionposts/(?P<pk>[0-9A-Fa-f-]+)'        | This displays each discussion post where it displays each discussion |
|                                                   post in detail where it gives you the option to edit the post.       |                
|"user/"                                          | This goes to each users homepage.                                    |                                       |r'^discussionposts/(?P<pk>[0-9A-Fa-f-]+)/update/ | This displays each discussion post form to edit the discussion post  |
|                                                   that was selected.  Users can only edit their posts.                 |
|"docUpload/"                                     | This displays the page to upload images.                             |
|"imageposts/"                                    | This displays the list of images uploaded.                           |
    

# Authentication/Authorization (HELP) 
(A final up-to-date description of how users are authenticated and any permissions for specific users (if any) that you used in your application. You should mention how they relate to which UI views are accessible.)

To check if users are authenticated we write the condition {% if user.is_authenticated %}. Doing this makes sure that the user is logged in. The line {% if user.username == object.disc_author.user_name  %} helps ensure that only the user can only edit the post they create. These lines of code are present in the template files createsurvey.html and discussiondetail.html. 

# Team Choice (HELP)
For our team choice component we decided to add functionality that would allow users to upload images and view images posted by others. For this team choice we added the Document model in models.py. This model consisted of a image field, a description, a time uploaded, and an author field. To allow images to be added we created a docUpload.html page which interacts with forms.py to update the Document data model. This included additions to forms.py, views.py, and urls.py. We created a list view for the images that shows the images, the descriptions and the authors. This is shown in imageposts.html which also required additions to urls.py. Finally we added to the base.html to make these upload pages and viewing pages for the images easily accessible. 

# Conclusion 

As a team we came from varying levels of experience but were able to come together and form a cohesive group with the ability to accomplish anything. Throughout the submissions we learned how to work together as a team to get all the various tasks done but also we began to become proficient in HTML, CSS and Django. As time went on it was almost effortless for us to delegate tasks to each other and get everything from the tricky UI to the troublesome user authentication done.

As a team we couldnt think of any one particular think that stood out to us as especially troubling other then a few things with User Authenitcation and generating user accounts. There was also a minor issue we ran into which was trying to link specific survey options to their respective survey post. We were able to resolve the issue, by figuring out how to add the parameter “related name = “choices”” in the survey_post foreign key element of the “Choice” model in the models.py file among other things. At times we left some of the work off a bit too long which left us sctrambling so in the future we certainly plan on being more proactive with the project and its due dates and to not expect things to magically get done. 

We would of liked to know more about CSS techniques and design strategies for making things look more appealing. Ofcourse there's more demand for functioonality and authenitcation but knowing how to create blocks of content and manipulating dimensions with inline style are important things to know too and could be covered in a class or two. Otherwise most things seemed useful to know as we went along with each submission. 

Other then a few issues with getting everybody hooked up on github, incidental or damaging github commits and the webservers we didnt really encounter any crazy technical errors. Everything more or less developed smoothly with everyones efforts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
