from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
from .forms import ExtendedUserForm, ExtendedAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import NewsDetails, Comment, Games
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.detail import DetailView
from django.contrib.contenttypes.models import ContentType



@csrf_exempt
def register_request(response):
    if response.method == "POST":
        form = ExtendedUserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login/")
    else:
        form = ExtendedUserForm()

    return render(response, "register.html", {"form":form})

@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        form = ExtendedAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = ExtendedAuthenticationForm()
    return render(request = request,template_name = "login.html",context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")







def NewsList(request):
    object_list = NewsDetails.objects.filter(active=True).order_by('-created_on')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page',1)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
                # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
            # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request = request,template_name = "blog.html",context={"object_list":post_list})


def GameList(request):
    object_list = Games.objects.filter(Active=True).order_by('-created_on')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page',1)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
                # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
            # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request = request,template_name = "android.html",context={"object_list":post_list})





def NewsDetail(request,id):
    object = NewsDetails.objects.filter(pk=id)
    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(NewsDetails))
    if request.method == 'POST':
        comment_data = request.POST.dict()
        body = comment_data.get("comment")
        username = request.user.username
        email = request.user.email
        comment = Comment()
        comment.name = username
        comment.email = email
        comment.body =  body
        comment.content_type=ContentType.objects.get_for_model(NewsDetails)
        comment.save()
    return render(request = request,template_name = "pc_news_details.html",context={"object":object[0],"comments":comments})






def GameDetail(request,id):
    object = Games.objects.filter(pk=id)
    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(Games))
    if request.method == 'POST':
        comment_data = request.POST.dict()
        body = comment_data.get("comment")
        username = request.user.username
        email = request.user.email
        comment = Comment()
        comment.name = username
        comment.email = email
        comment.body =  body
        comment.content_type=ContentType.objects.get_for_model(Games)
        comment.save()
    return render(request = request,template_name = "pc_download.html",context={"object":object[0],"comments":comments})












class TextView(DetailView):
    template_name = 'pc_news_details.html'
    context_object_name = 'brand'

    def get(self, request, slug):
        # Grabs the Brand object that owns the given slug
        brand = NewsDetails.objects.filter(active=True).order_by('-created_on')

        # renders self.template_name with the given context and model object
        return render(request, self.template_name, self.context_object_name)
