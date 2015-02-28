from django.contrib import admin

from base.models import UserProfile, Advertisement, Interest, JobOffer, Rating


class UserProfilePageAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'username', 'firstname', 'last_name', 'email', 'city',
                     'points', 'last_login', 'date_joined', 'picture', 'get_interests',)


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'user', 'lesson', 'date', 'type_of_meeting', 'duration', 'active', 'get_interest')


class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)


class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('id' , 'get_user', 'get_add_id', 'accepted',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'get_offer_id', 'get_author', 'rate', 'comment',)

admin.site.register(UserProfile, UserProfilePageAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(JobOffer, JobOfferAdmin)
admin.site.register(Rating, RatingAdmin)


# Register your models here.
