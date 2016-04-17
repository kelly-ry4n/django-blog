from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import markdown

# Create your models here.

class Post(models.Model):
    
    ''' This model represents a single blog post.

    Do no write to the html field directly, it is rendered by
    parsing markdown in the body field

    '''

    created = models.DateTimeField(blank=True)
    published = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    modified = models.DateTimeField(blank=True)

    html = models.TextField(blank=True, null=True, editable=False)

    title = models.TextField(unique=True)
    body = models.TextField()

    slug = models.CharField(max_length=63, blank=True)
    tags = models.ManyToManyField('blog.Tag')


    def _compute_slug(self):

        if len(self.title) > 63:
            slug = self.title.replace(' ', '-')
        else:
            slug = self.title[:63].replace(' ', '-')

        return slug


    def save(self, *args, **kwargs):

        # If this is a new object, assign created time on save
        if not self.pk:
            self.created = timezone.now()

        self.modified = timezone.now()
        self.slug = self._compute_slug()

        html = markdown.markdown(self.body, output_format='html5')
        self.html = html


        if self.is_published and self.published is None:
            self.published = timezone.now() 

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):

        tags = self.tags.all()

        tags_str = ', '.join([str(tag) for tag in tags])

        return "{} - [{}]".format(self.title, tags_str)

    def get_absolute_url(self):

        return '/posts/{}/{}'.format(self.pk, self.slug)




class Tag(models.Model):

    name = models.CharField(max_length=127, unique=True)

    def __unicode__(self):

        return self.name
