from django.db import models

# Create your models here.
class Alert_history(models.Model):
    date = models.CharField(max_length=30)
    alert_rating = models.FloatField()
    alert_g_spread = models.FloatField()
    alert_bm_spread = models.FloatField()
    alert_ai = models.FloatField()
    alert = models.FloatField()
    total = models.FloatField()
    region= models.FloatField()
    content = models.TextField()
    create_at = models.DateTimeField()

    #이건 뭘까낭?
    def __str__(self):
        return f'[{self.pk}]{self.title}'