from django.shortcuts import render, redirect
from .models import Post, PostImage


def posts_view(request):
    posts = Post.objects.all()
    return render(request, "accounts/allpost.html", {"allpost": posts})


def create_post_view(request):

    if request.method == "POST":
        title = request.POST.get("title_html")
        content = request.POST.get("content_html")

        post = Post.objects.create(
            title_coloum=title,
            content_coloum=content
        )

        images = request.FILES.getlist("images")

        for image in images:
            PostImage.objects.create(
                post=post,
                image=image
            )

        return redirect("allpost")

    return render(request, "accounts/create_post.html")