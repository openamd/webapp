from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from timezones.fields import TimeZoneField

class Profile(models.Model): 
    
    user = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    name = models.CharField(_('name'), max_length=50, null=True, blank=True)
    about = models.TextField(_('about'), null=True, blank=True)
    location = models.CharField(_('location'), max_length=40, null=True, blank=True)
    website = models.URLField(_('website'), null=True, blank=True, verify_exists=False)
    twitter = models.CharField(_('twitter username'), max_length=50, null=True, blank=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)

    age = models.IntegerField( null=True, blank=True)

    """this is ugly it came from this ugly script

	interests = ["New Tech","Activism","Radio","Lockpicking","Crypto","Privacy","Ethics","Telephones","Social Engineering",
		     "Hackerspaces","Hardware Hacking", "Nostalgia", "Communities", "Science", "Government", "Network Security",
		     "Malicious Software", "Pen Testing", "Web", "Niche Hacks", "Media"]

	for i in interests:
		var = i.replace(" ","")
		print "    " + str(var) + " = models.BooleanField(_('" + i + "'), max_length=50, null=True, blank=True)"
    """

    NewTech = models.BooleanField(_('New Tech'), max_length=50, null=True, blank=True)
    Activism = models.BooleanField(_('Activism'), max_length=50, null=True, blank=True)
    Radio = models.BooleanField(_('Radio'), max_length=50, null=True, blank=True)
    Lockpicking = models.BooleanField(_('Lockpicking'), max_length=50, null=True, blank=True)
    Crypto = models.BooleanField(_('Crypto'), max_length=50, null=True, blank=True)
    Privacy = models.BooleanField(_('Privacy'), max_length=50, null=True, blank=True)
    Ethics = models.BooleanField(_('Ethics'), max_length=50, null=True, blank=True)
    Telephones = models.BooleanField(_('Telephones'), max_length=50, null=True, blank=True)
    SocialEngineering = models.BooleanField(_('Social Engineering'), max_length=50, null=True, blank=True)
    Hackerspaces = models.BooleanField(_('Hackerspaces'), max_length=50, null=True, blank=True)
    HardwareHacking = models.BooleanField(_('Hardware Hacking'), max_length=50, null=True, blank=True)
    Nostalgia = models.BooleanField(_('Nostalgia'), max_length=50, null=True, blank=True)
    Communities = models.BooleanField(_('Communities'), max_length=50, null=True, blank=True)
    Science = models.BooleanField(_('Science'), max_length=50, null=True, blank=True)
    Government = models.BooleanField(_('Government'), max_length=50, null=True, blank=True)
    NetworkSecurity = models.BooleanField(_('Network Security'), max_length=50, null=True, blank=True)
    MaliciousSoftware = models.BooleanField(_('Malicious Software'), max_length=50, null=True, blank=True)
    PenTesting = models.BooleanField(_('Pen Testing'), max_length=50, null=True, blank=True)
    Web = models.BooleanField(_('Web'), max_length=50, null=True, blank=True)
    NicheHacks = models.BooleanField(_('Niche Hacks'), max_length=50, null=True, blank=True)
    Media = models.BooleanField(_('Media'), max_length=50, null=True, blank=True)

    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return ('profile_detail', None, {'username': self.user.username})
    get_absolute_url = models.permalink(get_absolute_url)
    
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return
    profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
