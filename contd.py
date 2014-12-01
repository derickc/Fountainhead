import sublime
import sublime_plugin
import re
# import threading
# import sys
try:
    from .sublime_helper import SublimeHelper
except (ImportError, ValueError):
    from sublime_helper import SublimeHelper
# sys.path.append(sublime.packages_path() + '/Fountainhead')
# import sublime_helper

# if int(sublime.version()) < 3000:
#     on_modified_async = sublime.on_modified

character1 = ''
character2 = ''


class Contd(sublime_plugin.EventListener):

    contd = " (CONT'D)"
    cursor_row = 0
    cursor_position1 = 0
    cursor_position2 = 0

    def on_activated(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('contd', False):
                self.cursor_row = view.rowcol(view.sel()[0].end())[0] - 1

    def modified_contd(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            self.cursor_position2 = view.rowcol(view.sel()[0].end())
            if sublime.load_settings('Fountainhead.sublime-settings').get('contd', False) and (self.cursor_position1 != self.cursor_position2):
                s = SublimeHelper()
                if s.cursor_scope(view) == 'text.fountain string entity.name.class ':
                    self.cursor_row = view.rowcol(view.sel()[0].end())[0] - 1
                    self.cursor_position1 = self.cursor_position2
                elif s.cursor_scope(view) == 'text.fountain entity.name.function ':
                    self.cursor_row = view.rowcol(view.sel()[0].end())[0]
                    self.cursor_position1 = self.cursor_position2
                elif s.cursor_scope(view) != 'text.fountain string entity.name.class ':
                            # print('cursor row ' + str(self.cursor_row))
                            scope_array = view.find_by_selector('text.fountain entity.name.function ')
                            row_array = []
                            for position in scope_array:
                                row_array.append(view.rowcol(sublime.Region.end(position))[0])
                            row_begin = 0
                            row_end = 0
                            for row in row_array:
                                if row <= self.cursor_row:
                                    row_begin = row
                                if row >= self.cursor_row and row_end == 0:
                                    row_end = row
                            if row_end == 0 or row_end <= self.cursor_row:
                                row = 0
                                text_point1 = 0
                                text_point2 = 1
                                while text_point1 != text_point2:
                                    text_point1 = view.text_point(row, 0)
                                    row += 1
                                    text_point2 = view.text_point(row, 0)
                                row_end = row
                            self.update_contd(view, row_begin, row_end)
                            self.cursor_position1 = self.cursor_position2

    def on_modified_async(self, view):
        if int(sublime.version()) >= 3000:
            self.modified_contd(view)

    def on_modified(self, view):
        if int(sublime.version()) < 3000:
            self.modified_contd(view)

    def remove_all_contd(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            row = 0
            text_point1 = -1
            text_point2 = 0
            line_beginning = 0
            line_end = 0
            scope = ''
            character = ''
            try:
                while text_point1 != text_point2:
                    text_point1 = view.text_point(row, 0)
                    line_beginning = text_point1
                    line_end = line_beginning + len(view.substr(view.line(text_point1)))
                    RemovecontdCommand.region = sublime.Region(line_end - len("(CONT'D)") - 1, line_end)
                    scope = view.scope_name(line_end - 1)
                    if scope == 'text.fountain string entity.name.class ':
                        character = view.substr(view.line(text_point1))
                        if re.search(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character) is not None:
                                view.run_command('removecontd')
                    row += 1
                    text_point2 = view.text_point(row, 0)
            except IndexError:
                pass

    def update_contd(self, view, row_begin=0, row_end=0):

        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            try:
                text_point1 = -1
                text_point2 = 0
                text_point3 = 1
                line_beginning = 0
                line_end = 0
                scope = ''
                character1 = ''
                character2 = ''
                if row_end != 0:
                    while text_point1 != text_point2 and text_point2 <= text_point3:
                        text_point1 = view.text_point(row_begin, 0)
                        text_point3 = view.text_point(row_end, 0)
                        line_beginning = text_point1
                        line_end = line_beginning + len(view.substr(view.line(text_point1)))
                        InsertcontdCommand.point = line_end
                        RemovecontdCommand.region = sublime.Region(line_end - len("(CONT'D)") - 1, line_end)
                        if line_beginning == line_end:
                            row_begin += 1
                        else:
                            scope = view.scope_name(line_end - 1)
                            if scope == 'text.fountain string entity.name.class ':
                                # get the entire line string
                                character2 = view.substr(view.line(text_point1))
                                # try to remove leading spaces
                                if character2[0] == ' ' or character2[0] == '\t':
                                    character2 = re.split(r"^\s*", character2)[1]
                                if re.search(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2) is not None and re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character1)[0] != re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2)[0]:
                                        view.run_command('removecontd')
                                # do not add (CONT'D) if already there
                                elif character2 == character1 and re.search(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2) is not None:
                                    pass
                                # add (CONT'D) to current matching character if previous character already has it
                                elif re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character1)[0] == character2:
                                    view.run_command('insertcontd')
                                elif character2 == character1:
                                    view.run_command('insertcontd')
                            character1 = character2
                            if scope == 'text.fountain entity.name.function ':
                                character1 = ''
                            row_begin += 1
                        text_point2 = view.text_point(row_begin, 0)
                elif row_end == 0:
                    while text_point1 != text_point2:
                        text_point1 = view.text_point(row_begin, 0)
                        line_beginning = text_point1
                        line_end = line_beginning + len(view.substr(view.line(text_point1)))
                        InsertcontdCommand.point = line_end
                        RemovecontdCommand.region = sublime.Region(line_end - len("(CONT'D)") - 1, line_end)
                        if line_beginning == line_end:
                            row_begin += 1
                        else:
                            scope = view.scope_name(line_end - 1)
                            if scope == 'text.fountain string entity.name.class ':
                                character2 = view.substr(view.line(text_point1))
                                # try to remove leading spaces
                                if character2[0] == ' ' or character2[0] == '\t':
                                    character2 = re.split(r"^\s*", character2)[1]
                                if re.search(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2) is not None and re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character1)[0] != re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2)[0]:
                                        view.run_command('removecontd')
                                # do not add (CONT'D) if already there
                                elif character2 == character1 and re.search(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character2) is not None:
                                    pass
                                # add (CONT'D) to current matching character if previous character already has it
                                elif re.split(r"\s+\([cC][oO][nN][tT]\'[dD]\)", character1)[0] == character2:
                                    view.run_command('insertcontd')
                                elif character2 == character1:
                                    view.run_command('insertcontd')
                            character1 = character2
                            if scope == 'text.fountain entity.name.function ':
                                character1 = ''
                            row_begin += 1
                        text_point2 = view.text_point(row_begin, 0)
            except IndexError:
                pass


class RemovecontdCommand(sublime_plugin.TextCommand):

    region = sublime.Region(0, 0)

    def run(self, edit):
        self.view.erase(edit, self.region)


class InsertcontdCommand(sublime_plugin.TextCommand):

    point = 0

    def run(self, edit):
        string = Contd.contd
        self.view.insert(edit, self.point, string)


class UpdateContdCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        update = Contd()
        update.update_contd(self.view)


class RemoveAllContdCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        remove = Contd()
        remove.remove_all_contd(self.view)
        Contd.cursor_position1 = self.view.rowcol(self.view.sel()[0].end())
