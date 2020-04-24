from django.db import models

# Create your models here.
def content_file_name(instance, filename):
	# return '/'.join(['content', instance.user.username, filename])
	return 'files/text/%s.png' % ( instance.name)

class message(models.Model):
	name 				= models.CharField(primary_key = True,max_length=100)
	note 				= models.TextField(null = True,blank = True)
	im 					= models.ImageField(upload_to=content_file_name,null = True,blank = True)
	created_date		= models.DateTimeField(auto_now_add=True)
	modified_date		= models.DateTimeField(blank=True, null=True,auto_now=True)

	def __str__(self):
		return ('%s' % (self.name))
