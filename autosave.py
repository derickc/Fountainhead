import sublime
import sublime_plugin


class AutomaticSaveCommand(sublime_plugin.EventListener):

    clicks = 0

    def on_modified(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('auto_save', True):
                self.clicksTrigger = sublime.load_settings('Fountainhead.sublime-settings').get('auto_save_count', 42)
                self.clicks += 1
                if self.clicks >= self.clicksTrigger:
                    self.clicks = 0
                    view.run_command('save')
