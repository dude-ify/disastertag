from django.db import models

class Dtag(models.Model):
    barcode_id = models.PositiveIntegerField(default=1, unique=True)
    first_name = models.CharField(max_length=225, blank=True)
    last_name = models.CharField(max_length=225, blank=True)
    notes = models.TextField(blank=True)
    loc_lat = models.FloatField(blank=False)
    loc_lon = models.FloatField(blank=False)
    SEVERITY_CHOICES = (
            ('SR', 'Severe'),
            ('MO', 'Moderate'),
            ('MD', 'Mild'),
            )
    severity = models.CharField(
            max_length=2,
            choices=SEVERITY_CHOICES,
            default='SR',
            )

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable rep of the model instance"""
        return "{}".format(self.first_name)
