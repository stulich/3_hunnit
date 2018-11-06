# Overview
Our application is a forum for UMass students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll percentage, bar chart or pie chart. The aim is to provide more ways for UMass students to communicate, and to see how the community at large feels on certain topics. 

There are some differences in the layout of our webpages from our initial proposal shown in the proposal.md file. For one, we originally intended to display comments on each discussion post, directly beneath the content of the post. We opted to change that, and have each discussion post be linked to a focused page on each post. There, users can view comments on the post and add their own comments. When creating discussions and surveys, we also opted to remove the option to categorically tag posts for sorting for the time being. It is something we could put back in later, but for now have avoided. Lastly, with our survey results display we have made a few changes. Similar to how we will have users drill down to see the details of a discussion page, we will have users vote on a post, then be brought to a designated view of that survey’s results. This will allow us to provide a more detailed view of the results, without cluttering the survey listings.


# Team Members

* Conor Carmichael
* Stephen Ulich
* Monmoy Mohsin
* Harsha Malireddy
* Arjun Singh
* Kyle Ewell

# Video Link

 
# Design Overview

We have 5 models in our models.py file: UserAccount, DiscussionPost, CommentSection, SurveyPost, and Choice. 
The UserAccount model identifies different users which contains a username, a first name, and a last name. The DiscussionPost contains information regarding a post, including the title, the author (a UserAccount object), the content of the post, and a reference to a comment section. The comment is tied to the discussion post, many comments can link to one discussion post and each content contains a user, and text.
The SurveyPost model contains a title, a UserAccount, a question, and the options that can be voted for. The options are found in the Choice model and are a different data model where many different instances of Choice can link to one survey post. Each instance of a Choice contains the actual option and the number of votes that the option has received. 
 
We have set up our urls such that we have base routes to view surveys and discussion posts, then base routes to create surveys and discussions. Then, from the survey and discussion urls, there are dynamic urls for viewing the details of specific discussions and surveys. For each of the urls, there are respective functions/classes depending on the need of the page. For static pages, functions can deliver the content to the browser sufficiently, where as for pages using more dynamic, database driven views, a class is needed to deliver the proper information to the user. For discussion posts and survey posts, we have list views that enable us to deliver the SurveyPost Objects back to the user, and when you click on links from these post, you can see a more detailed view of them (with results for surveys, or comments for the discussion posts).

In our views file, we have classes and functions that serve specific urls. We have classes that are able to serve our Surveys, Discussions, and respective detail views. These classes allow us to specify the data necessary for the page, a queryset, and the template html page associated with it. Then, we can write a function for retrieving the data, in get_context_data(). This is useful, because we do not need to get the survey results, when were just showing the survey and allowing the users to vote, and we don’t need to retrieve the comments on all posts when displaying our discussion posts page. This is good for efficiency, as we don’t retrieve data we do not need. For our pages not relying on data, we do not need to specify a class, and can just reference a function in the urls page. For example, in our creating a discussion page, we have a function that just calls the django built in function, render, and provide it a html template.

# Problems/Successes

We didn’t have problems in collaboration. We worked through any difficulties in coding the site by talking with one another. One issue we ran into, was trying to link specific survey options to their respective survey post. We were able to resolve the issue, by having a few of the team members approach the issue. One of our group members was able to figure out how to solve this issue by adding the parameter “related name = “choices”” in the survey_post foreign key element of the “Choice” model in the models.py file. By doing this we were able to add the inner for loop line and its display statement: {% for choice in  post.choices.all %} {{choice.option}}<br>. Another issue, we encountered, was trying to create a specific page, for the detailed view of surveys/discussions. We were able to solve that by implementing a regular expression based url mapping, which uses the id’s of the post to make unique urls. To improve collaboration for the next project we will make sure to start our discussions earlier in the working period for project 3 so that we are less stressed about getting things done before the deadline. 


# Youtube video
https://www.youtube.com/watch?v=yjFtHXPX5tQ&feature=youtu.be

