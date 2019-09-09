from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.core.validators import URLValidator
from tinymce.models import HTMLField
from statistics import mean
# Create your models here.

class Profile(models.Model):
    profile = models.OneToOneField(User,on_delete=models.CASCADE, null = True)
    photo = models.ImageField(upload_to = 'profile/',default='fbfba5feddcfae6c24fa528c7749eafc.jpg' ,blank = True)
    bio = models.TextField(max_length=500)

    def __str__(self):
     return self.profile.username
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

 # project class
class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField(max_length=1000)
    link=models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)   
    userinterface=models.PositiveIntegerField(choices=list(zip(range(1,11),range(1, 11))), default=0)
    functionality = models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    content=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)

    def __str__(self):
     return self.title

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        project = cls.objects.get(id=project_id)
        return project

    @classmethod
    def search_by_title(cls,search_term):
        projects_title = cls.objects.filter(title__icontains=search_term)
        return projects_title

class Review(models.Model):
    '''
    '''
    design=models.IntegerField(blank=True,default=0)
    userinterface=models.IntegerField(blank=True,default=0)
    functionality=models.IntegerField(blank=True,default=0)
    content=models.IntegerField(blank=True,default=0)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    judge=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    average_review = models.IntegerField(blank=True, default=0)

    def save_review(self):
        self.save()
    def __str__(self):
        return f'{self.project.title}:Review-{self.design}-{self.userinterface}-{self.functionality}-{self.content}-{self.project.id}'    
    @classmethod
    def get_all_reviews(cls,project_id):
        design=round(mean(cls.objects.filter(project_id=project_id).values_list('design',flat=True)))
        userinterface=round(mean(cls.objects.filter(project_id=project_id).values_list('userinterface',flat=True)))
        functionality=round(mean(cls.objects.filter(project_id=project_id).values_list('functionality',flat=True)))
        content=round(mean(cls.objects.filter(project_id=project_id).values_list('content',flat=True)))
        average_review=(design+userinterface+functionality+content)/4

        return  {
            'design':design,
            'userinterface':userinterface,
            'functionality':functionality,
            'content':content,
            'average_review':average_review
        }