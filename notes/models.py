from django.db import models

from markdownx.models import MarkdownxField

class Note(models.Model):

	class Maturity(models.IntegerChoices):
		SEEDLINE = 1
		SAPLING = 2
		MATURE = 3
		DECLINE = 4

	class Importance(models.IntegerChoices):
		NOT_AT_ALL_IMPORTANT = 1
		LOW_IMPORTANCE = 2
		NEUTRAL = 3
		VERY_IMPORTANT = 4
		EXTREMELY_IMPORTANT = 5

	class Likelihood(models.IntegerChoices):
		IMPOSSIBLE = 1
		REMOTE = 2
		HIGHLY_UNLIKELY = 3
		UNLIKELY = 4
		POSSIBLE = 5
		LIKELY = 6
		HIGHLY_LIKELY = 7
		CERTAIN = 8

	title = models.CharField(unique=True, max_length=255)
	slug = models.SlugField(unique=True, max_length=255)

	body = MarkdownxField()

	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	lifespan = models.DurationField()

	maturity = models.IntegerField(choices=Maturity.choices, default=1)
	importance = models.IntegerField(choices=Importance.choices)
	likelihood = models.IntegerField(choices=Likelihood.choices)

	def __str__(self):
		return self.title


class NoteLink(models.Model):

	note = models.ForeignKey('Note', on_delete=models.CASCADE)

	url = models.URLField(max_length=255)
