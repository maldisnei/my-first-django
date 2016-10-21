from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
class Post(models.Model):
	
	auth=models.ForeignKey('auth.User',related_name='auth')
	title=models.CharField(max_length=200)
	texto = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	slug=models.SlugField(blank=True,max_length=200,unique=True)


	def __str__(self):
		return self.title

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('blog.views.detail',kwargs={'slug':self.slug})
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)


class Comment(models.Model):
	poste = models.ForeignKey('blog.Post',related_name='comments')
	
	testo = models.TextField()
	author = models.CharField(max_length=200)
	approved_comment = models.BooleanField(default=False)
	created_date= models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.testo
	

	def approved(self):
		self.approved_comment=True
		self.save()


class Sobre_mim(models.Model):
	autho= models.ForeignKey('auth.User',related_name='blog_sobre_mim')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	
	def  __str__(self):
		return self.text

# SIGNAILS
from django.db.models import signals
from django.template.defaultfilters import slugify

def artigo_pre_save(signal,instance,sender, **kwargs):
	if not instance.slug:
		slug = slugify(instance.title)
		novo_slug = slug
		contador = 0

		while Post.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
			contador += 1
			novo_slug = '%s-%d'%(slug,contador)

		instance.slug = novo_slug
signals.pre_save.connect(artigo_pre_save, sender=Post)

