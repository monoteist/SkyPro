from django.db import models

from users.models import User


class Education(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='educations'
    )
    title = models.CharField('Title', max_length=150)

    def __str__(self) -> str:
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='experiences'
    )
    title = models.CharField('Title', max_length=150)

    def __str__(self) -> str:
        return self.title


class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='portfolio'
    )
    title = models.CharField('Title', max_length=150)

    def __str__(self) -> str:
        return self.title
