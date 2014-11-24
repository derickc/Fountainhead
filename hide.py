import sublime
import sublime_plugin


class FoldBoneyard(sublime_plugin.EventListener):

    def on_load_async(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
            if sublime.load_settings('Fountainhead.sublime-settings').get('fold_boneyard', False):
                view.fold(view.find_by_selector('comment'))


class FoldSynopses(sublime_plugin.EventListener):

    def on_load(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
            if sublime.load_settings('Fountainhead.sublime-settings').get('fold_synopses', False):
                view.fold(view.find_by_selector('meta.diff'))


class FoldNotes(sublime_plugin.EventListener):

    def on_load(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
            if sublime.load_settings('Fountainhead.sublime-settings').get('fold_notes', False):
                view.fold(view.find_by_selector('variable.parameter'))


class HideBoneyardCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector('comment')):
                self.view.fold(self.view.find_by_selector('comment'))
                print('hide')
            else:
                ShowBoneyardCommand.run(self, edit)


class ShowBoneyardCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            for region in self.view.find_by_selector('comment'):
                self.view.unfold(region)


class HideSynopsesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector('meta.diff')):
                self.view.fold(self.view.find_by_selector('meta.diff'))
            else:
                ShowSynopsesCommand.run(self, edit)


class ShowSynopsesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            for region in self.view.find_by_selector('meta.diff'):
                self.view.unfold(region)


class HideNotesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector('variable.parameter')):
                self.view.fold(self.view.find_by_selector('variable.parameter'))
            else:
                ShowNotesCommand.run(self, edit)


class ShowNotesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            for region in self.view.find_by_selector('variable.parameter'):
                self.view.unfold(region)

# http://www.sublimetext.com/forum/viewtopic.php?f=3&t=4620
