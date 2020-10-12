from core import config as setup


class PluginFactory:
    def __init__(self):
        # dictionary to store default plugins short - long name mapping
        self.default_plugins = {
            "DummySampler": 'kg.apc.jmeter.samplers.DummySampler',
            'UDP': 'kg.apc.jmeter.samplers.UDPSampler',
            'SeleniumWebDriver': 'com.googlecode.jmeter.plugins.webdriver.sampler.WebDriverSampler',
            'Visualizer': 'kg.apc.jmeter.vizualizers.CorrectedResultCollector'
        }
        self.plugins = self.default_plugins
        self.plugins_list = setup.config['JMeter']['Plugins']['Default']
        self.custom_plugins = setup.config['JMeter']['Plugins']['Custom']

    def load_custom_plugin_mappings(self):
        """
        Adds custom plugin mappings to default plugins dict
        """
        self.update_plugin_list()
        if self.custom_plugins:
            self.plugins.update(self.custom_plugins)

    def update_plugin_list(self):
        """
        Generates a list of all plugin names (default + custom)
        """
        custom_plugin_list = []
        if self.custom_plugins:
            custom_plugin_list = [*self.custom_plugins]

        self.plugins_list = list(set(self.plugins_list + custom_plugin_list))

    def get_plugin_full_name(self, plugin):
        """
        Returns the plugin full name based on plugin name/type
        :param plugin: short name of plugin
        :return: string long name of plugin
        """
        # updated_plugin_list = load_custom_plugin_mappings(default_plugins_list)
        plugin_name = self.plugins.get(plugin, None)
        return plugin_name
