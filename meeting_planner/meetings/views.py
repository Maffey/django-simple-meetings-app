from django.shortcuts import render, get_object_or_404, redirect
from .forms import MeetingForm
from .models import Meeting
from .models import Room


def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/rooms.html",
                  {"rooms": Room.objects.all})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
