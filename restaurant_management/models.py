from RestaurantLocation(models.Model):
    address = models.CharField(max_length = 252)
    city = models.CharField(max_length = 100)
    state  = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"
        