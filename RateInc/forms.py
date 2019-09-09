from django import forms
from .models import Profile, Project,Review

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','userinterface','content','functionality']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','bio']

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['project','judge']
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']   