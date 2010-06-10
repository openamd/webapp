from django.db import models

# May want to add information to a faction later, hence a separate model for it.
class Faction(models.Model):  
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

# This data is going to come from the Cassandra DB. But for now, I'm putting it 
# here so it's somewhere hackable.
class UserSTUB(models.Model): 
	name = models.CharField(max_length=100)
	faction = models.ForeignKey(Faction)
	def __unicode__(self):
		return "%s (%s)" % (self.name, self.faction.name)

# This data is going to exclusively come from the Cassandra DB.
class UserDataSTUB(models.Model):
	user = models.ForeignKey(UserSTUB)
	x = models.IntegerField()
	y = models.IntegerField()
	# sometimes, zone information is all we need, a chance to speed up processing
	zone = models.IntegerField() 
	# 8-bit bitfield, indicating which buttons were pressed with the badge was
	# scanned
	buttons = models.IntegerField() 
	when = models.DateTimeField()
	def __unicode__(self):
		return "%s (%s, %s) [%s] %s => %s" % (self.user.name, self.x, self.y, self.zone, self.when, self.buttons)

# In a way, hotspots are almost like virtual attendees. They will exist on the 
# conference floor without having a physical embodiment.
class Hotspot(models.Model):
	name = models.CharField(max_length=50)
	x = models.IntegerField()
	y = models.IntegerField()
	# hotspots cover an area, rather than being a single point
	radius = models.IntegerField() 
	zone = models.IntegerField()
	buttons = models.IntegerField()
	def __unicode__(self):
		return self.name
		
	#INPUT: user -> a UserSTUB instance to check for standing in the hotspot
	#OUTPUT: true if the user is standing in range of the hotspot and has the 
	#	hotspot's button pattern depressed. False otherwise.
	def userIsInside(self, user):
		return False
		
	#INPUT: user -> a UserSTUB instance to check for having the hotspot's button
	#	pattern depressed
	#OUTPUT: true if the user is pressing the button pattern, false otherwise
	def userIsPressingButton(self, user):
		return False

# Flags are a representation of actions that the user can take, things they can
# pick up, general status indicators.
class Flag(models.Model):
	name = models.CharField(max_length=50)
	# The text that will be emailed to the user when they pick up the flag
	content = models.CharField(max_length=5000)
	# The number of raffle ticket points that picking up the flag will confer
	points = models.IntegerField()
	# The first time the flag is capable of being picked up (used to lock certain
	# features of the games until a certain time has been reached)
	minDate = models.DateTimeField()
	# The area the user has to be in to pick up the flag
	hotspot = models.ForeignKey(Hotspot)
	# The faction the user has to be in to pick up the flag
	faction = models.ForeignKey(Faction)
	# The minimum number of other faction members that need to be with the user
	# in order for all users to pick up the flag
	minFactionCount = models.IntegerField()
	# Indicates that the flag is not visible until the user has obtained it
	isHidden = models.BooleanField()
	# Indicates that the flag is never visible to the user, it's used only for
	# internal processing.
	isInternal = models.BooleanField()
	def __unicode__(self):
		return self.name + ": " + self.content
		
	# INPUT: user -> a UserSTUB instance to check for receiving a certain flag
	# OUTPUT: false if the user does not match the requirements for the flag
	#	or if the user already has the flag, true otherwise.
	def isMatch(self, user):
		#TODO: figure out how to determine the following two bools
		userHasFlag = False
		userMeetsRequirements = False
		return not userHasFlag and userMeetsRequirements

# Some flags will have prerequisites of other flags before they can be picked up
class FlagPrereq(models.Model):
	flag = models.OneToOneField(Flag, related_name="Flag_Parent")
	prereqs = models.ManyToManyField(Flag, related_name="Flag_Requirements")

# A record of when a user has picked up a specific flag
class FlagCapture(models.Model):
	flag = models.ForeignKey(Flag)
	user = models.ForeignKey(UserSTUB)
	when = models.DateTimeField()
	def __unicode__(self):
		return self.user + ":" + self.flag + ":" + self.when