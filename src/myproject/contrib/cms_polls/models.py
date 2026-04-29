from django.db import models
from cms.models import CMSPlugin


class CmsPollPlugin(CMSPlugin):
    question = models.CharField(max_length=255)
    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.question

# class CmsPollSepChoicesPlugin(CMSPlugin):
#     question = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.question
#
#
# class Choice(CMSPlugin):  # todo: or models.Model ?
#     poll = models.ForeignKey(CmsPollPlugin, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=255)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
