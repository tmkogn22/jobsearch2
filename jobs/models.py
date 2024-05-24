from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    objects = models.Manager()


class Vacancy(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    objects = models.Manager()


class Resume(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    skills = models.TextField()
    criminal_record = models.CharField(max_length=3)
    experience = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_user_permissions',
        related_query_name='customuser_user_permission'
        )
    ROLE_CHOICES = [
            ('appliciant', 'Соискатель'),
            ('company', 'Компания')
        ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
