from django.shortcuts import render, get_object_or_404
from .models import Research, TeamMember, Service, News


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

    from .forms import ContactForm


    if request.method == "POST":

        form = ContactForm(request.POST)


        if form.is_valid():

            form.save()

            return render(
                request,
                "contact.html",
                {
                    "success": True
                }
            )


    else:

        form = ContactForm()


    return render(
        request,
        "contact.html",
        {
            "form": form
        }
    )
def news(request):

    articles = News.objects.filter(
        is_published=True
    ).order_by(
        "-published_date"
    )


    return render(
        request,
        "news.html",
        {
            "articles": articles
        }
    )

def team_detail(request, id):
    member = get_object_or_404(TeamMember, id=id)

    return render(
        request,
        "team_detail.html",
        {
            "member": member
        }
    )