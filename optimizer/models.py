from django.db import models

class FarmData(models.Model):
    farmer_name = models.CharField(max_length=100)
    total_budget = models.FloatField()
    crop_options = models.TextField(help_text="Comma-separated crop names")
    transport_costs = models.TextField(help_text="CSV formatted transport cost matrix")
    constraints = models.TextField(help_text="CSV formatted constraints")

    def __str__(self):
        return self.farmer_name
