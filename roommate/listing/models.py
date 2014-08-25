from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode

# PURPOSE CHOICES
NEED = 1
HAVE = 2
PURPOSE_CHOICES = (
    (NEED, 'Need a Room'),
    (HAVE, 'Have a Room'),
)

# GENDER CHOICES
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Others'),
)

# DWELLING CHOICES
BUNGALOW = 1
APARTMENT = 2
HOUSE = 3
DWELLING_CHOICES = (
    (BUNGALOW, 'Bungalow'),
    (APARTMENT, 'Apartment'),
    (HOUSE, 'House'),
)

# ROOM TYPES
SINGLE = 1
DOUBLE = 2
TRIPLE = 3
ROOM_SHARE = 4
ROOM_TYPES = (
    (SINGLE, 'Single Room'),
    (DOUBLE, 'Double Room'),
    (TRIPLE, 'Triple Room'),
    (ROOM_SHARE, 'Room share'),
)

# DIET CHOICES
PURE_VEG = 1
EGGETERIAN = 2
NON_VEG = 3
DIET_CHOICES = (
    (PURE_VEG, 'Pure Veg'),
    (EGGETERIAN, 'Eggeterian'),
    (NON_VEG, 'Non Veg'),
)

# LOOKING CRITERIA
MALE = 1
FEMALE = 2
COUPLE = 3
GROUP = 4
CRITERIA_TYPES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (COUPLE, 'Couple'),
    (GROUP, 'Group'),
)

# OCCUPATION CHOICES
STUDENT = 1
PROFESSIONAL = 2
RETIRED = 3
OTHERS = 4
OCCUPATION_CHOICES = (
    (STUDENT, 'Student'),
    (PROFESSIONAL, 'Professional'),
    (RETIRED, 'Retired'),
    (OTHERS, 'Others'),
)


class Country(models.Model):
    code = models.CharField(max_length=2, db_index=True)
    languages = models.CharField(max_length=250, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "countries"

    @property
    def parent(self):
        return None

    def __unicode__(self):
        return force_unicode(self.name)


class Region(models.Model):
    name_std = models.CharField(max_length=200, db_index=True, verbose_name="State")
    code = models.CharField(max_length=200, db_index=True)

    @property
    def parent(self):
        return self.country

    def full_code(self):
        return ".".join([self.parent.code, self.code])


class City(models.Model):
    name_std = models.CharField(max_length=200, db_index=True, verbose_name="City")
    region = models.ForeignKey(Region, null=True, blank=True)

    class Meta:
        verbose_name_plural = "cities"

    @property
    def parent(self):
        return self.region


class UserProfile(User):
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    occupation = models.SmallIntegerField(choices=OCCUPATION_CHOICES)
    age = models.SmallIntegerField()
    avatar = models.ImageField()
    city = models.ForeignKey(City)
    area = models.CharField(max_length=200, db_index=True, verbose_name='Area')
    purpose = models.SmallIntegerField(choices=PURPOSE_CHOICES)
    contact_number = models.IntegerField(max_length=20)
    email = models.EmailField()
    smokes = models.BooleanField()
    drinks = models.BooleanField()
    diet = models.SmallIntegerField(choices=DIET_CHOICES)
    about_me = models.CharField(max_length=200, db_index=True, verbose_name='About Me')


class UserProfileHave(UserProfile):
    user_profile = models.OneToOneField(UserProfile)

    # Details about the property
    total_rent = models.IntegerField()
    rent_per_head = models.IntegerField()
    available_from = models.DateTimeField()
    minimum_stay = models.SmallIntegerField()
    dwelling_type = models.SmallIntegerField(choices=DWELLING_CHOICES)
    current_tenants = models.IntegerField()
    max_tenants = models.IntegerField()
    bedrooms = models.SmallIntegerField()
    bedrooms_available = models.SmallIntegerField()
    bathrooms = models.SmallIntegerField()
    room_type = models.SmallIntegerField(choices=ROOM_TYPES)

    # Room amenities
    furnished = models.BooleanField()
    television = models.BooleanField()
    air_condition = models.BooleanField()
    internet = models.BooleanField()
    parking = models.BooleanField()
    gym = models.BooleanField()
    swimming_pool = models.BooleanField()
    elevator = models.BooleanField()


class UserProfileNeed(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    budget = models.IntegerField()
    criteria = models.SmallIntegerField(choices=CRITERIA_TYPES)









