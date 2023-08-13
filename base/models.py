from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #cascade - to delete the items created by the user whom deleted by admin, if set_null is chosen then the items created by the user will be there.
 #null = True is this field can be empty,Blank = True
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    #charfield is for title text field is for more content

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']