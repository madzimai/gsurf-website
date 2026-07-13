from django.db import models


class Research(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    publication_date = models.DateField()

    report = models.FileField(
        upload_to="research_reports/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title


class TeamMember(models.Model):

    name = models.CharField(
        max_length=100
    )

    position = models.CharField(
        max_length=100
    )

    biography = models.TextField()

    photo = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Service(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title
class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        max_length=200,
        blank=True
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name + " - " + self.subject
class News(models.Model):

    title = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )

    content = models.TextField()

    published_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_published = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    client = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    summary = models.TextField()

    featured_image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title