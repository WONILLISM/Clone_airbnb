from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
from core import models as core_models

# from users import models as user_models
# from reviews import models as review_models


class AbstractItem(core_models.TimeStampModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]
        # ordering = ["name"]


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140, null=True)
    description = models.TextField(null=True)
    country = CountryField(null=True)
    city = models.CharField(max_length=80, null=True)
    price = models.IntegerField(null=True)
    guests = models.IntegerField(
        help_text="How many people will be staying?", null=True
    )
    address = models.CharField(max_length=140, null=True)
    beds = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    baths = models.IntegerField(null=True)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, default=""
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="room", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))
        return 0
