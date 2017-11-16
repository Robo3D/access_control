# coding=utf-8
from __future__ import absolute_import
import subprocess

import octoprint.plugin

class Access_controlPlugin(octoprint.plugin.SettingsPlugin,
                           octoprint.plugin.AssetPlugin,
                           octoprint.plugin.TemplatePlugin,
                           octoprint.plugin.StartupPlugin):
    def on_settings_initialized(self):
        try:
            self._logger.info("###### Starting Access Control ##########")
            self._logger.info( "accessControl: enabled: {}".format(
                self._settings.global_get(['accessControl','enabled'])
                )
            )
            self._settings.global_set(['accessControl','enabled'], True)
            self._logger.info( "accessControl: enabled: {}".format(
                self._settings.global_get(['accessControl','enabled'])
                )
            )
            self._settings.global_set(['server','firstRun'], True)
            self._settings.save()
            s = subprocess.call(['/home/pi/oprint/bin/pip', 'uninstall', '-y', 'access_control'])
            subprocess.call(['sudo', 'reboot'])
        except Exception as e:
            self._logger.exception('###########Error !!!Access Control ####')



__plugin_name__ = "Access_control Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Access_controlPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
	}
