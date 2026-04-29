from django.db import models
from cms.models import CMSPlugin


class CmsPollPlugin(CMSPlugin):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Choice(CMSPlugin):
    poll = models.ForeignKey(CmsPollPlugin, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
