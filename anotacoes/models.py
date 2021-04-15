from django.db import models

class Anotacao(models.Model):
    id = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return f"Anotação ({self.id})"