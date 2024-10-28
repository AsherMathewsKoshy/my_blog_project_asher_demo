from django.shortcuts import render
from .forms import CommentForm 
# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost




# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost






# Create a new blog post (for authenticated users)
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm  # Assuming you created a BlogPostForm in forms.py

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_create.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost  # Import your BlogPost model
from .forms import BlogPostForm  # Import your BlogPost form

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            blog_post = form.save(commit=False)  # Create the blog post instance without saving it yet
            blog_post.author = request.user  # Set the author to the logged-in user
            blog_post.save()  # Now save the blog post
            return redirect('blog:blog_list')  # Redirect to the blog list after creating
    else:
        form = BlogPostForm()  # Create an empty form for GET request

    return render(request, 'blog/blog_create.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import BlogPost  # assuming BlogPost model is defined

# blog/views.py
def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', id=id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comment_form': comment_form,
        'comments': post.comments.all()  # Get all comments for the post
    })

from .forms import UserRegistrationForm, ProfileForm

# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use your custom form if needed
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login or another page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()  # Create an empty form for GET request
    return render(request, 'blog/register.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the post author to the logged-in user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_create.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm  # Make sure to create this form

# blog/views.py
# blog/views.py

# blog/views.py

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm  # Assuming you have a form for the profile

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect to the user's profile after saving changes
            return redirect('blog:user_profile', user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'blog/edit_profile.html', {'form': form})




# blog/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .utils import send_notification_email  # Ensure this import is correct







# blog/views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'blog/user_management.html', {'users': users})
@staff_member_required
def post_management(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_management.html', {'posts': posts})
from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        'Test Email Subject',
        'This is a test email.',
        'ashermathewskoshy@gmail.com',
        ['masskolamass54@gmail.com'],  # Replace with an actual recipient
        fail_silently=False,
    )
    return HttpResponse('Test email sent!')

# blog/views.py
from .utils import send_notification_email

@login_required
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    
    send_notification_email(user, 'blocked')  # Notify user about being blocked
    
    messages.success(request, f'The user {user.username} has been blocked.')
    return redirect('user_management')


# blog/views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'blog/user_management.html', {'users': users})

@staff_member_required
def post_management(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_management.html', {'posts': posts})
@staff_member_required
def post_management(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_management.html', {'posts': posts})

# blog/views.py
from django.contrib.auth.models import User
from .utils import send_notification_email

@login_required
def block_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False  # Block the user
    user.save()

    # Send email notification
    subject = "Account Blocked"
    message = "Dear {}, your account has been blocked by the admin.".format(user.username)
    send_notification_email(user.email, subject, message)

    return redirect('admin_dashboard')  # Redirect to your admin dashboard

# blog/views.py
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)  # Check if the user is an admin
def admin_dashboard(request):
    users = User.objects.all()
    posts = BlogPost.objects.all()
    return render(request, 'blog/admin_dashboard.html', {'users': users, 'posts': posts})

from django.contrib import messages

@user_passes_test(lambda u: u.is_superuser)
def block_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()

    # Send email notification
    subject = "Account Blocked"
    message = f"Dear {user.username}, your account has been blocked by the admin."
    send_notification_email(user.email, subject, message)

    messages.success(request, f"{user.username} has been blocked.")
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = post.author  # Assuming Post has an author field
    post_title = post.title  # Get the title of the post
    post.delete()
    
    subject = "Post Deleted"
    context = {
        'username': user.username,
        'post_title': post_title,  # Include post title in the context
    }
    send_notification_email(subject, 'blog/emails/post_deleted.html', context, [user.email])
    
    return redirect('blog:post_management')

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import send_notification_email
from django.contrib import messages

@login_required
def unblock_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True  # Unblock the user
    user.save()

    send_notification_email(user, 'unblocked')  # Notify user about being unblocked

    messages.success(request, f'The user {user.username} has been unblocked.')
    return redirect('blog:user_management')  # Ensure the namespace is correct here



@user_passes_test(lambda u: u.is_superuser)
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    user_posts = BlogPost.objects.filter(author=user)
    return render(request, 'blog/user_detail.html', {'user': user, 'posts': user_posts})
@login_required
def profile(request):
    # Add logic to handle profile updates here if needed
    return render(request, 'blog/profile.html')

# blog/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def profile_view(request):
    # Render a template or return a response for the user profile
    return render(request, 'blog/user_profile.html', {'user': request.user}) # Create this template
# blog/views.py
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import BlogPost, Comment  # Assuming you have a Comment model

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})


def post_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        blog_post = get_object_or_404(BlogPost, id=post_id)
        Comment.objects.create(content=content, post=blog_post, author=request.user)
        return redirect('blog:blog_detail', post_id=post_id)
    return HttpResponse("Method not allowed", status=405)

# Example: Accessing profile data in a view
# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

def user_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch the user based on the user_id
    profile = get_object_or_404(Profile, user=user)  # Fetch the profile associated with the user

    return render(request, 'blog/user_profile.html', {'user': user, 'profile': profile})


# Restricting access based on blocked status
from django.http import HttpResponseForbidden

def some_view(request):
    if request.user.profile.blocked:
        return HttpResponseForbidden("Your account is blocked.")
    # Continue with the view's main logic if not blocked

# blog/views.py (example of login view handling)
from django.contrib.auth import login

def my_login_view(request):
    # Your login logic
    if request.method == 'POST':
        # Assuming form processing here
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:user_profile', user_id=user.id)  # Redirect to user's profile
    # Render login form...
# blog/utils.py

# blog/views.py
# blog/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .utils import send_notification_email

def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch user by ID
    user.is_active = False  # Change user status to inactive
    user.save()  # Save the changes to the database

    # Notify user via email
    send_notification_email(user, 'blocked')
    
    return redirect('blog:user_management')  # Redirect to user management page
# blog/utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# blog/utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_notification_email(user, action):
    subject = f'Account Notification: {action.capitalize()}'
    
    context = {
        'username': user.username,
        'action': action,
    }
    
    # Render the HTML message
    html_message = render_to_string('blog/emails/account_notification.html', context)

    # Send the email
    send_mail(
        subject,
        strip_tags(html_message),  # Fallback plain text message
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=html_message,  # This is the HTML message
    )

# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('blog:user_management')  # Redirect to your user management page after deletion
