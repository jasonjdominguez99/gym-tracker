from django.db import models
import uuid

class User(models.Model):
    sexes = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Non-binary')
    ]

    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=127)
    sex = models.CharField(max_length=1, choices=sexes)

    def __str__(self):
        return self.first_name + self.last_name
