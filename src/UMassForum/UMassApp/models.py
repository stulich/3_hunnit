from django.db import models


class User(models.Model):
    """Model representing a user."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this user across whole platform",
    )

    # A character field for the first name.
    first_name = models.CharField(max_length=20)

    # A character field for the last name.
    last_name = models.CharField(max_length=20)

    # A charecter field for the username
    user_name = models.CharField(max_length=20)
 

    class Meta:
        ordering = ["user_name"]

    def get_absolute_url(self):
        """Returns the url to access a particular user"""
        return reverse("user-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.user_name}"

class Discussion_Post:
    """Model representing a user."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this post",
    )

    title = models.CharField(max_length=25)

    disc_author = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)

    content=models.CharField(max_length=400)

    class Meta:
       ordering = ["title"]

    def get_absolute_url(self):
        """Returns the url to access a particular user"""
        return reverse("title", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.title}"




