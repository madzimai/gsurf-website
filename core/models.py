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