from django.db import models

# Add the markdown field
from markdownx.models import MarkdownxField

# Add slugify to create pretty urls
from django.template.defaultfilters import slugify

# Add reverse for paths
from django.urls import reverse

# Import regexp for finding backlinks
import re

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
	slug = models.SlugField(unique=True, blank=True, max_length=255)

	body = MarkdownxField()

	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	lifespan = models.DurationField()

	maturity = models.IntegerField(choices=Maturity.choices, default=1)
	importance = models.IntegerField(choices=Importance.choices)
	likelihood = models.IntegerField(choices=Likelihood.choices)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("note_detail", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):

		# Add slug to note
		self.slug = slugify(self.title).replace("-", "_")

		#
		# Find backlinks
		#

		# First check if the note is new or not and delete any previous links from the database
		if self.id is not None:
			NoteLink.objects.filter(source = self).delete()

		# Create an empty list to hold references
		link_list = list()

		# Look for wiki-style internal links
		links = re.findall("\[\[.*?\]\]", self.body)

		# Parse internal links
		for link in links:

			# Extract the reference and search for matching notes
			link = link[2:-2].lower().replace(" ", "_")

			# Deduplicate references
			if link not in link_list:
				link_list.append(link)

		# Look for standard markdown links
		links = re.findall("\[.*?\]\(\/.*?[#\)]", self.body)

		# Parse internal links
		for link in links:

			# Extract the reference and search for matching notes
			link = link[link.find("/")+1:-1].lower().replace(" ", "_")

			# Deduplicate references
			if link not in link_list:
				link_list.append(link)

		# Validate and add links to model
		for link in link_list:

			reference_note = Note.objects.filter(slug = link)

			# Check if any notes match and save
			if len(reference_note) > 0:
				notelink = NoteLink(source = self, reference = reference_note[0])
				notelink.save()

		return super().save(*args, **kwargs)


class NoteLink(models.Model):

	source = models.ForeignKey('Note', related_name="source", on_delete=models.CASCADE, null=True)
	reference = models.ForeignKey('Note', related_name="reference", on_delete=models.CASCADE, null=True)
