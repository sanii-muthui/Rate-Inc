from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile,Review
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ProfileForm,NewReviewForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from .serializer import ProfileSerializer
from rest_framework import status

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'landing.html',{'projects':projects})

def project(request,project_id):
    project = Project.objects.get(id = project_id)
    reviews=Review.get_all_reviews(project_id)
    project.design=reviews['design']
    project.userinterface=reviews['userinterface']
    project.functionality=reviews['functionality']
    project.content=reviews['content']
    project.average_review=reviews['average_review']
    project.save()
    current_user=request.user
    if request.method=='POST':
        form=NewReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.judge=current_user
            review.project=project
            
            review.save()
            messages.success(request,f'Review Submitted')
            return redirect('project-detail',project_id)
    else:
        form=NewReviewForm()  
    return render(request,'project.html',{'form':form,'project':project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('indexPage')

    else:
        form = ProjectForm()
    return render(request, 'new_post.html', {"form": form})

def profile(request):
    current_user = request.user
    projects = Project.objects.filter(profile=current_user).all()
    profile = Profile.objects.filter(profile=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(profile=current_user)

    return render(request, 'profile/profile.html',{'projects':projects,'profile':profile})
@login_required
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance = request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('Profile')
    else:
        form = ProfileForm(instance = request.user.profile)
    return render(request,'profile/edit_profile.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'project_details.html', {'project':project})

class ProjectList(APIView):
   def get(self,request,format=None):
       all_projects=Project.objects.all()
       serializers=ProjectSerializer(all_projects,many=True)
       return Response(serializers.data)


class ProfileList(APIView):
   def get(self,request,format=None):
       all_profiles=Profile.objects.all()
       serializers=ProfileSerializer(all_profiles,many=True)
       return Response(serializers.data)



