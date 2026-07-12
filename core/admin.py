from django.contrib import admin
from .models import Research, TeamMember, Service


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "publication_date",
        "created_at"
    )

    search_fields = (
        "title",
        "description"
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "position",
        "created_at"
    )

    search_fields = (
        "name",
        "position"
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_at"
    )

    search_fields = (
        "title",
        "description"
    )