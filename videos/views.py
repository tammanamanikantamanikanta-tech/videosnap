# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect
from .models import Video

# Display all videos
def video_view(request):
    videos = Video.objects.all()
    return render(request, "accounts/allvideo.html", {"allvideos": videos})

def create_video_view(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        video_file = request.FILES.get("video")

        if title and video_file:
            # Create the video
            Video.objects.create(
                title=title,
                description=description,
                video=video_file,
                uploader=request.user if request.user.is_authenticated else None
            )
            return redirect("allvideos")

    return render(request, "accounts/create_video.html")
