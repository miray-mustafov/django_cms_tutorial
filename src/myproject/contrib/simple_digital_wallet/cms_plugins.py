from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import SimpleDigitalWalletPlugin


@plugin_pool.register_plugin
class SimpleDigitalWalletPluginPublisher(CMSPluginBase):
    model = SimpleDigitalWalletPlugin
    name = "Simple Digital Wallet Plugin"
    render_template = "simple_digital_wallet/simple_digital_wallet.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
