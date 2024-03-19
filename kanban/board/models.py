from django.db import models
from django.conf import settings

class ticket(models.Model):
    ticket_title=models.CharField(max_length=300)
    ticket_description=models.CharField(max_length=300)
    ticket_user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ticket_title