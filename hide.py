# import sublime
import sublime_plugin
try:
    from . import scopes
except (ImportError, ValueError):
    import scopes

fountain_scope = scopes.fountain_scope
action_scope = scopes.action_scope
boneyard_scope = scopes.boneyard_scope
dialogue_scope = scopes.dialogue_scope
lyrics_scope = scopes.lyrics_scope
character_scope = scopes.character_scope
parenthetical_scope = scopes.parenthetical_scope
note_scope = scopes.note_scope
scene_scope = scopes.scene_scope
character_list_scope = scopes.character_list_scope
section_scope = scopes.section_scope
synopses_scope = scopes.synopses_scope
pagebreak_scope = scopes.pagebreak_scope
title_page_scope = scopes.title_page_scope
center_scope = scopes.center_scope
transition_scope = scopes.transition_scope


class FoldBoneyard(sublime_plugin.EventListener):

    def on_load_async(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
        # if 'Fountainhead.tmLanguage' in view.settings().get('syntax'):
            # if sublime.load_settings('Fountainhead.sublime-settings').get('fold_boneyard', False):
            if view.settings().get('fold_boneyard', False):
                # view.fold(view.find_by_selector('comment'))
                view.fold(view.find_by_selector(boneyard_scope))


class FoldSynopses(sublime_plugin.EventListener):

    def on_load(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
        # if 'Fountainhead.tmLanguage' in view.settings().get('syntax'):
            # if sublime.load_settings('Fountainhead.sublime-settings').get('fold_synopses', False):
            if view.settings().get('fold_synopses', False):
                # view.fold(view.find_by_selector('meta.diff'))
                view.fold(view.find_by_selector(synopses_scope))


class FoldNotes(sublime_plugin.EventListener):

    def on_load(self, view):
        if (view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage'):
        # if 'Fountainhead.tmLanguage' in view.settings().get('syntax'):
            # if sublime.load_settings('Fountainhead.sublime-settings').get('fold_notes', False):
            if view.settings().get('fold_notes', False):
                # view.fold(view.find_by_selector('variable.parameter'))
                view.fold(view.find_by_selector(note_scope))


class HideBoneyardCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector(boneyard_scope)):
                self.view.fold(self.view.find_by_selector(boneyard_scope))
            else:
                for region in self.view.find_by_selector(boneyard_scope):
                    self.view.unfold(region)


class HideSynopsesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector(synopses_scope)):
                self.view.fold(self.view.find_by_selector(synopses_scope))
            else:
                for region in self.view.find_by_selector(synopses_scope):
                    self.view.unfold(region)


class HideNotesCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            if self.view.fold(self.view.find_by_selector(note_scope)):
                self.view.fold(self.view.find_by_selector(note_scope))
            else:
                for region in self.view.find_by_selector(note_scope):
                    self.view.unfold(region)

# http://www.sublimetext.com/forum/viewtopic.php?f=3&t=4620
