from django.shortcuts import render
from .models import Research, TeamMember, Service



def home(request):
    return render(request, "home.html")


def about(request):

    from .models import TeamMember

    team = TeamMember.objects.all()

    context = {
        "team": team
    }

    return render(
        request,
        "about.html",
        context
    )


def services(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(
        request,
        "services.html",
        context
    )


def research(request):

    researches = Research.objects.all().order_by(
        "-publication_date"
    )

    context = {
        "researches": researches
    }

    return render(
        request,
        "research.html",
        context
    )


def contact(request):
    return render(request, "contact.html")