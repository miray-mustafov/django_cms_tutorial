from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import CmsPollPlugin
from django.utils.translation import gettext as _

"""
The plugin class is responsible for providing django CMS with the necessary information to render your plugin.
"""


@plugin_pool.register_plugin
class CmsPollPluginPublisher(CMSPluginBase):
    model = CmsPollPlugin
    name = _("CMS Poll Plugin")
    render_template = "cms_polls/cms_polls.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
