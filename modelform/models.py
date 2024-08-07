from django.db import models


# Create your models here.
class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(
        help_text="Enter project name", verbose_name="Project Name", max_length=100
    )
    assigned_to = models.CharField(
        verbose_name="Assigned To", max_length=100, help_text="Enter name"
    )
    priority = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Meta:
    verbose_name = "Project"
    verbose_name_plural = "Projects"
