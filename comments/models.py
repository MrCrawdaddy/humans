from django.db import models
from django.contrib.auth import models as auth_model
from documentaries.models import Documentary

class Comment(models.Model):
    user = models.ForeignKey(auth_model.User, on_delete=models.CASCADE)#required
    documentary = models.ForeignKey(Documentary, on_delete=models.CASCADE)#required
    date_submitted = models.DateTimeField()#required
    comment = models.TextField()#required
    appropriate = models.BooleanField(default=True)
    checked_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.comment)[0:20]

