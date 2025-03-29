Building and deploying a Django API

Learning Objectives
By the end of this project, you will be able to:

Set Up a Django Project and Implement User Authentication:

Create a new Django project and app.
Configure Django REST Framework and implement a robust user authentication system.
Implement Posts and Comments Functionality:

Develop features that allow users to create, view, update, and delete posts and comments.
Implement User Follows and Feed Functionality:

Add features for users to follow other users and view a feed of posts from followed users.
Implement Notifications and Likes Functionality:

Enable users to like posts and receive notifications for various interactions within the platform.
Deploy the Django REST API to Production:

Prepare and deploy the Django REST API to a production environment, ensuring it is secure and scalable.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)