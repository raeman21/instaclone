from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,ProfileForm,CommentForm
from .models import Image,Profile,User,Comments
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.order_by('-date')
    profile = Profile.objects.order_by('-last_update')
     
    return render(request,'index.html',{"images":images,"profile":profile})

@login_required(login_url='/accounts/login/')
def image(request,image_id):

    image = Image.objects.get(id = image_id)
    comments = Comments.get_comments_by_images(image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    is_liked = False
    if image.likes.filter(id = request.user.id).exists():
        is_liked = True
    
    return render(request,"image.html", {"image":image,"is_liked":is_liked,"total_likes":image.total_likes(),'comments':comments,'form':form})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster= current_user
            image.save()
        return redirect('home')
    else:
        form = ImageForm()

    return render(request,'new_image.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    #profile = Profile.objects.get(user_id=current_user.id)
    images = Image.objects.all().filter(poster_id=user.id)
    return render(request, 'profile.html',{"user":user, "current_user":request.user,"images":images})

@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    profile = Profile.objects.get(user=request.user.id)
    queryset = User.objects.get(username=username)
    profile_details = Profile.get_by_id(queryset.id)
    
    images = Image.get_profile_images(queryset.id)
    
    is_followed = False
    if profile.follows.filter(id=request.user.id).exists():
        is_followed = True

    return render(request, 'user_profile.html', { 'profile':profile, 'profile_details':profile_details, 'images':images,'is_followed':is_followed})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    # current_user = request.user
    # user = User.objects.get(id= current_user.id)
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            # profile = form.save(commit=False)
            # profile.user= request.user
            # profile.save()
        return redirect ('profile')
    else:
        form = ProfileForm( )
    
    return render(request,'update_profile.html',{"form":form})

@login_required (login_url='/accounts/register/')
def like_image(request):
    images = get_object_or_404(Image,id = request.POST.get('image_id') )
    is_liked = False
    if images.likes.filter(id = request.user.id).exists():
        images.likes.remove(request.user)
        is_liked = False
    else:
        images.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(images.get_absolute_url())

# @login_required (login_url='/accounts/register/')
# def follow_user(request):
#     profile = get_object_or_404(Profile,id = request.POST.get('profile_id'))
#     is_followed = False
#     if profile.follows.filter(id=request.user.id).exists():
#         profile.follows.remove(request.user)
#         is_followed = False
#     else:
#         profile.follows.add(request.user)
#         is_followed=True
#         return HttpResponseRedirect(profile.get_absolute_url())

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})

def follow_user(request):
    profile = get_object_or_404(Profile,id = request.POST.get('profile_id'))
    #user_profile = request.user.profile.id
    #data = {}
    is_followed = False
    if profile.follows.filter(id=request.user.profile.id).exists():
        profile.follows.remove(request.user)
        is_followed = False
        #data['message'] = "You are already following this user."
    else:
        profile.follows.add(request.user)
        is_followed= True
        #data['message'] = "You are now following {}".format(profile_to_follow)
    return HttpResponseRedirect(profile.get_absolute_url())

# def follow_user(request, profile_id):
#     profile_to_follow = get_object_or_404(Profile, pk=profile_id)
#     user_profile = request.user.profile.id
#     data = {}
#     if profile_to_follow.follows.filter(id=profile_id).exists():
#         data['message'] = "You are already following this user."
#     else:
#         profile_to_follow.follows.add(user_profile)
#         data['message'] = "You are now following {}".format(profile_to_follow)
#     return JsonResponse(data, safe=False)