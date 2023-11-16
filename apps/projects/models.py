from django.db import models

# Create your models here.


class Project(models.Model):
    naming = models.CharField(max_length=35)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='project_preview_image/')


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_image/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
