# Overview
Our application is a forum for UMass students that allows users to create discussion posts and survey posts. Users can create discussion posts by entering a title and the content of the discussion. Users can create survey posts by entering a question and giving multiple choice options for others to choose from. The authors of survey posts can also select how they want the results to be displayed: a poll percentage, bar chart or pie chart. The aim is to provide more ways for UMass students to communicate, and to see how the community at large feels on certain topics. 

There are no differences to our application other than adding the functionality needed for this submission.

# Team Members

* Conor Carmichael
* Stephen Ulich
* Monmoy Mohsin
* Harsha Malireddy
* Arjun Singh
* Kyle Ewell

# Video Link
Video Link: https://youtu.be/Sc3QC6qiIOk

# Design Overview
For user interaction, we used Django forms to implement fields that users can use to create and update discussion posts. In our template, we checked to see whether a user is authenticated, is a superuser, or is neither of those. This allowed us to handle each case, by directing authorized users to the form, throwing a message to superusers to use the admin site, and throwing a message to log in for users.

In terms of functionality, we decided that users will not be allowed to modify survey posts because it could lead to dishonest data and would defeat the purpose of allowing surveys. We also decided to not allow users to delete posts because they could delete useful information in their posts or in the responses. Only admins will be allowed to delete posts if the content is deemed inappropriate.

# Problems/Successes

We didn't have any problems working together. We all did our parts to the best of our abilities and helped each other when needed. We ran into a problem when we tried to update the survey posts because it might need a thorough change to our data model and how we coded the posts. We will work on it so that it is done for the final submission. Our discussion post form has full functionality and works like. One big success for this submission was that we all were able to do our parts and didn't have any merge issues. Another big success is how are application has turned out. It works well, we manage to handle adding the functionality needed for this assignment, and fixed a lot of bugs that popped up and made our app crash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
