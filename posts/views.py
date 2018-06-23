from django.shortcuts import render, redirect
from .models import Post
from django import forms


# Defining the Form class for using Django Form
class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    desc = forms.CharField(label="Description", max_length=1000)


# Create your views here.
# Show the list of the posts
def index(request):
    # get all the data, ordered by -timestamp is to show the newest one at the top
    posts_objs = Post.objects.all().order_by("-timestamp")
                                            # returning the posts_objs and the front-end could use it as posts.
    return render(request, "index.html", {"posts": posts_objs})


# Create a post
def create_post(request):
    # when clicking the button, the method is get. Showing the page at this time.
    if request.method == "GET":
        return render(request, "create_post.html")
    # when submitting the form, the method is post. Getting the data at this time and to store it.
    else:
        form = PostForm(request.POST)

        # validate the input
        if form.is_valid():
            # input is correct, store the data.
            post = Post(title=form.cleaned_data["title"], desc=form.cleaned_data["desc"])
            post.save()
            return redirect('/')
        # if sth wrong, return with the error and the data that user has input.
        else:
            return render(request, "create_post.html", {"form": form})


# Show the post details.
def post_detail(request, post_id):
    # using regular expression will get a string, parse it to int.
    post_id = int(post_id)
    # query for the post
    post = Post.objects.get(id=post_id)

    # return it about its details.
    return render(request, "post_detail.html", {"post": post})


# Edit a post
def edit_post(request, post_id):
    # using regular expression will get a string, parse it to int.
    post_id = int(post_id)

    # query for the post
    post = Post.objects.get(id=post_id)

    # when clicking the button, the method is get. Showing the page at this time with the post infos.
    if request.method == "GET":
        return render(request, "edit_post.html", {"post": post})
    # when submitting the form, the method is post. Getting the data at this time and to update it.
    else:
        form = PostForm(request.POST)

        # validate the input
        if form.is_valid():
            # input is correct, store the data.
            Post.objects.filter(id=post_id).update(title=form.cleaned_data['title'], desc=form.cleaned_data['desc'])
            return redirect('/')
        else:
            # if sth wrong, return with the error and the data that user has input.
            return render(request, "edit_post.html", {"form": form})

