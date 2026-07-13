from django.contrib import admin
from .models import (
    Research,
    TeamMember,
    Service,
    ContactMessage,
    News,
    Project
)


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
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read"
    )

    list_filter = (
        "is_read",
        "created_at"
    )

    search_fields = (
        "name",
        "email",
        "subject"
    )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "published_date",
        "is_published"
    )

    list_filter = (
        "is_published",
        "published_date"
    )

    search_fields = (
        "title",
        "content"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "client",
        "location",
        "start_date",
        "end_date",
        "is_featured"
    )

    list_filter = (
        "is_featured",
        "location"
    )

    search_fields = (
        "title",
        "client"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }