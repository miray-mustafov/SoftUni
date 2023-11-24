from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    born = models.DateField(blank=False, null=False)
    position = models.CharField(max_length=7, default='default', choices=(
        ('default', 'default'),
        ('junior', 'junior'),
        ('mid', 'mid'),
        ('senior', 'senior'),
    ))
    department = models.ForeignKey(
        to=Departments,
        default=3,
        on_delete=models.CASCADE,
        null=False, blank=False)

    def __str__(self):
        return f'id:{self.pk} {self.name}'

    class Meta:
        ordering = ['id']


class EmployeeBasic(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    seniority_level = models.CharField(
        max_length=30,
        choices=(
            ('junior', 'junior'),
            ('regular', 'regular'),
            ('senior', 'senior'),
        )
    )


class Photo(models.Model):
    photo = models.ImageField(upload_to='pet_photos')

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"Photo: {self.photo.name.split('/')[-1]} ({self.pk})"
