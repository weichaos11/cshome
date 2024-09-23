from mkdocs.plugins import BasePlugin
import markdown

class MultilineTablePlugin(BasePlugin):
    def on_config(self, config):
        config['markdown_extensions'] = config.get('markdown_extensions', []) + ['stylesheets/multiline_table_plugin.MultilineTableExtension']
        return config
