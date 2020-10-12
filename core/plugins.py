# dictionary to store default plugins short - long name mapping
default_plugins_list = {
    "DummySampler": 'kg.apc.jmeter.samplers.DummySampler',
    'UDP': 'kg.apc.jmeter.samplers.UDPSampler',
    'SeleniumWebDriver': 'com.googlecode.jmeter.plugins.webdriver.sampler.WebDriverSampler',
    'Visualizer': 'kg.apc.jmeter.vizualizers.CorrectedResultCollector'
}


def get_plugin_full_name(plugin):
    """
    Returns the plugin full name based on plugin name/type
    :param plugin: short name of plugin
    :return: string long name of plugin
    """
    plugin_name = default_plugins_list.get(plugin, None)
    return plugin_name
