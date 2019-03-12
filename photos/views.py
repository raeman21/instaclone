from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def home(request):
    images = Image.get_all_images()
    
    return render(request, 'all-photos/home.html', {'images':images})

# @login_required(login_url='/accounts/login/')
# def new_pic(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.editor = current_user
#             article.save()
#         return redirect('NewsToday')

#     else:
#         form = NewArticleForm()
#     return render(request, 'new_pic.html', {"form": form})