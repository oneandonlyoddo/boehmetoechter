from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from auszeichnungen.models import AuszeichnungsPlugin as AuszeichnungsPluginModel
from auszeichnungen.models import Veranstalter
from django.utils.translation import ugettext as _




class AwardsPlugin(CMSPluginBase):
    #model = AuszeichnungsPluginModel
    name = "Auszeichnungen"
    render_template = "auszeichnungen/plugin.html"

    def render(self, context, instance, placeholder):
    	awards = Veranstalter.objects.order_by('-jahr')
    	context.update({'awards':awards})
        return context

plugin_pool.register_plugin(AwardsPlugin)