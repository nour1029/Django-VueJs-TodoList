from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Todo(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    done = models.BooleanField(_("Done"), default=False)

    
    def __str__(self):
        return self.title