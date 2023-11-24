from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=20, unique=True)
    nonrequired = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    born = models.DateField(blank=False, null=False)
    position = models.CharField(max_length=7, default='default', choices=(
        ('default', 'default'),
        ('junior', 'junior'),
        ('senior', 'senior'),
        ('devops', 'devops'),
    ))
    department = models.ForeignKey(
        to=Departments,
        default=3,
        on_delete=models.CASCADE,
        null=False, blank=False)

    def __str__(self):
        return f'id:{self.pk} {self.name}'
