I contributed to several aspects of this project. The first one being that I implemented the login/logout functionality for users created in init.py. While noticing that we would somehow have to have our userAccounts be tied with a one to one relationship to the django users.

I made the one to one mappings of users created to our existing userAccount data model so that they shared the same information and posts were tied to a user. 

Finally I added a page that allows users to see all of the posts they made themselves that required the user to be logged in. Which involved creating the view in views.py as well as the html.
