# blog/forms.py
from django import forms
from .models import BlogPost  # Make sure BlogPost exists in models.py
from django.contrib.auth.models import User
from .models import Profile
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','image']
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'contact_number']

# blog/forms.py
from django import forms
from .models import Profile  # Assuming you have a Profile model
from .models import BlogPost, Comment
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'contact_number']  # Add any other fields you want
# blog/forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
