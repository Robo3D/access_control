/*
 * View model for access_control
 *
 * Author: victor
 * License: AGPLv3
 */
$(function() {
    function Access_controlViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        Access_controlViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_access_control, #tab_plugin_access_control, ...
        [ /* ... */ ]
    ]);
});
