# coding=utf-8
from __future__ import absolute_import
import subprocess

import octoprint.plugin

class Access_controlPlugin(octoprint.plugin.SettingsPlugin,
                           octoprint.plugin.AssetPlugin,
                           octoprint.plugin.TemplatePlugin,
                           octoprint.plugin.StartupPlugin):
    def on_startup(self):
        self.global_set(['accessControl','enabled'], 'true')
        self.global_set(['server','firstRun'], 'true')
        s = subprocess.call(['/home/pi/oprint/bin/pip', 'uninstall', '-y', 'access_control'])
        subprocess.call(['sudo', 'reboot'])


__plugin_name__ = "Access_control Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Access_controlPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
	}
