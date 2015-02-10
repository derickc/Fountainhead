import sublime_plugin


class CapCurrentLineCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            self.view.run_command('run_macro_file', {"file": "Packages/Fountainhead/macros/CapCurrentLine.sublime-macro"})
