from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class PollsApphook(CMSApp):
    """
    app_name: this optional attribute gives the system a unique way to refer to the apphook.
        It is used the create a reverse mapping for the URL’s namespace.

    name: is a human-readable name, and will be displayed to the user in the Advanced settings
        of the CMS pages attaching to this apphook.

    get_urls(): method is what actually hooks the application in, returning a list of URL
        configurations that will be made active wherever the apphook is used - in this case, it
        will either use the urls.py from polls, or declare its own list of URL patterns.
    """

    app_name = "polls"
    name = "Polls Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["myproject.contrib.polls.urls", ]  # !


"""
# Alternatively, you can also specify the URL patterns directly, for instance:

from django.urls import path
from ..polls import views


@apphook_pool.register
class PollsApphook(CMSApp):
    app_name = "polls"
    name = "Polls Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
            path("<int:pk>/vote/", views.vote, name="vote"),
            path("<int:pk>/", views.DetailView.as_view(), name="detail"),
            path("", views.IndexView.as_view(), name="index"),
        ]
"""
