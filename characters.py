import sublime
import sublime_plugin
import re
# import os
# import sys
# import platform
# from .sublime_helper import *
try:
    from .sublime_helper import SublimeHelper
except (ImportError, ValueError):
    from sublime_helper import SublimeHelper


# class SublimeHelper(sublime_plugin.EventListener):

#     def cursor_scope(self, view, offset=1):
#         '''
#         Gives the scope based on cursor position.
#         '''
#         return view.scope_name(view.sel()[0].end() - offset)

#     def line_scope(self, view, offset=1):
#         '''
#         Gives the scope for a given line based on cursor position.  Defaults to the previous line.
#         '''
#         return view.scope_name(view.text_point(view.rowcol(view.sel()[0].end())[0] - offset, 0))

#     def line_string(self, view, offset=1):
#         '''
#         Gives the string of text for a given line.  Defaults to the previous line.
#         '''
#         return view.substr(view.line(view.text_point(view.rowcol(view.sel()[0].end())[0] - offset, 0)))

#     def scope_list(self, view, scope='text.fountain '):
#         '''
#         Gives a list of all strings for a given scope.
#         '''
#         regions = []
#         scopes = []
#         regions = view.find_by_selector(scope)
#         for region in regions:
#             scopes.append(view.substr(region))
#         return scopes

# cursor_scope = SublimeHelper.cursor_scope
# line_scope = SublimeHelper.line_scope
# line_string = SublimeHelper.line_string

user = ''
# user_os = platform.system()


class Characters(sublime_plugin.EventListener):

    characters = []
    person = ''
    lower_characters = []
    camel_characters = []
    current_character = ''
    previous_line = 0
    current_line = 0
    filename = ''

    def modified_character(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('characters', True):
                if self.characters == []:
                    self.on_activated(view)
                view.set_status('CharacterList', '')
                if view.rowcol(view.sel()[0].end())[0] != self.current_line:
                    self.previous_line = self.current_line
                    self.current_line = view.rowcol(view.sel()[0].end())[0]
                    if view.scope_name(view.text_point(self.previous_line, 0)) == 'text.fountain string entity.name.class ':
                        # get character name from line
                        s = SublimeHelper()
                        self.current_character = view.substr(view.line(view.text_point(self.previous_line, 0)))
                        character = s.line_string(view)
                        name = self.current_character.split(' (O.S.)')[0]
                        name = name.split(' (V.O.)')[0]
                        name = name.split(' (OS)')[0]
                        name = name.split(' (VO)')[0]
                        name = name.split(" (CONT'D)")[0]
                        if name[0] == ' ' or name[0] == '\t':
                            name = re.split(r'^\s*', name)[1]
                        if name not in self.characters:
                            self.characters.append(name)
                            packages_directory = sublime.packages_path()
                            completions_file = packages_directory + '/Fountainhead/Characters.sublime-completions'
                            # if user_os == 'Windows':
                                # print("Sorry, not supported at this time.")
                            # elif user_os == 'Darwin':
                            if name[0] != '@':
                                if name.lower() not in self.lower_characters:
                                    self.lower_characters.append(name.lower())
                                    self.lower_characters = sorted(self.lower_characters)
                                    # proc_env = os.environ.copy()
                                    # encoding = sys.getfilesystemencoding()
                                    # for k, v in proc_env.items():
                                        # proc_env[k] = os.path.expandvars(v).encode(encoding)
                                    # user = (proc_env['HOME']).decode(encoding='UTF-8')
                                    # completions = open(user + '/Library/Application Support/Sublime Text 3/Packages/Fountainhead/Characters.sublime-completions', 'w')
                                    completions = open(completions_file, 'w')
                                    completions.write('{\n\t\t"scope": "text.fountain - comment - string - entity.other.attribute-name - entity.other.inherited-class - foreground - meta.diff - entity.name.function - entity.name.tag - entity.name.class - variable.parameter",\n\n\t\t"completions":\n\t\t[')
                                    length = len(self.lower_characters)
                                    character_counter = 0
                                    for character in self.lower_characters:
                                        if character_counter < length - 1:
                                            completions.write('"%s",' % character)
                                            character_counter += 1
                                        else:
                                            completions.write('"%s"' % character)
                                    completions.write(']\n}')
                                    completions.close()
                            elif name[0] == '@':
                                if name not in self.lower_characters:
                                    self.lower_characters.append(name)
                                    self.lower_characters = sorted(self.lower_characters)
                                    # proc_env = os.environ.copy()
                                    # encoding = sys.getfilesystemencoding()
                                    # for k, v in proc_env.items():
                                    #     proc_env[k] = os.path.expandvars(v).encode(encoding)
                                    # user = (proc_env['HOME']).decode(encoding='UTF-8')
                                    # completions = open(user + '/Library/Application Support/Sublime Text 3/Packages/Fountainhead/Characters.sublime-completions', 'w')
                                    completions = open(completions_file, 'w')
                                    completions.write('{\n\t\t"scope": "text.fountain - comment - string - entity.other.attribute-name - entity.other.inherited-class - foreground - meta.diff - entity.name.function - entity.name.tag - entity.name.class - variable.parameter",\n\n\t\t"completions":\n\t\t[')
                                    length = len(self.lower_characters)
                                    character_counter = 0
                                    for character in self.lower_characters:
                                        if character_counter < length - 1:
                                            completions.write('"%s",' % character)
                                            character_counter += 1
                                        else:
                                            completions.write('"%s"' % character)
                                    completions.write(']\n}')
                                    completions.close()
                            # Clear out character list message
                            view.set_status('CharacterList',
                                            '')

    def on_modified_async(self, view):
        if int(sublime.version()) >= 3000:
            self.modified_character(view)

    def on_modified(self, view):
        if int(sublime.version()) < 3000:
            self.modified_character(view)

    def on_activated(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('characters', True):
                if self.filename == view.file_name() and len(self.characters) > 0:
                    pass
                    # print(view.file_name())
                else:
                    view.set_status('CharacterList',
                                    'FINDING CHARACTERS...')
                    self.characters = []
                    self.lower_characters = []
                    counter = 0
                    self.filename = view.file_name()
                    try:
                        while counter >= 0:
                            character = view.substr(view.find_by_selector(
                                'text.fountain string entity.name.class ')[counter])
                            name = character.split(' (O.S.)')[0]
                            name = name.split(' (V.O.)')[0]
                            name = name.split(' (OS)')[0]
                            name = name.split(' (VO)')[0]
                            name = name.split(" (CONT'D)")[0]
                            if name[0] == ' ' or name[0] == '\t':
                                name = (re.split(r'^\s*', name))[1]
                            if name not in self.characters:
                                self.characters.append(name)
                            counter += 1
                    except IndexError:
                        pass
                    # if user_os == 'Windows':
                    #     print("Sorry, not supported at this time.")
                    # elif user_os == 'Darwin':
                    for character in self.characters:
                        if character[0] != '@':
                            self.lower_characters.append(character.lower())
                        if character[0] == '@':
                            self.lower_characters.append(character)
                    self.lower_characters = sorted(self.lower_characters)
                    # proc_env = os.environ.copy()
                    # encoding = sys.getfilesystemencoding()
                    # for k, v in proc_env.items():
                    #     proc_env[k] = os.path.expandvars(v).encode(encoding)
                    # user = (proc_env['HOME']).decode(encoding='UTF-8')
                    # completions = open(user + '/Library/Application Support/Sublime Text 3/Packages/Fountainhead/Characters.sublime-completions', 'w')
                    packages_directory = sublime.packages_path()
                    completions_file = packages_directory + '/Fountainhead/Characters.sublime-completions'
                    completions = open(completions_file, 'w')
                    completions.write('{\n\t\t"scope": "text.fountain - comment - string - entity.other.attribute-name - entity.other.inherited-class - foreground - meta.diff - entity.name.function - entity.name.tag - entity.name.class - variable.parameter",\n\n\t\t"completions":\n\t\t[')
                    length = len(self.lower_characters)
                    character_counter = 0
                    for character in self.lower_characters:
                        if character_counter < length - 1:
                            completions.write('"%s",' % character)
                            character_counter += 1
                        else:
                            completions.write('"%s"' % character)
                    completions.write(']\n}')
                    completions.close()
                    # Print confirmation message
                    view.set_status('CharacterList',
                                    'CHARACTERS FOUND!')

                    ShowCharactersCommand.unsorted_characters = self.characters


class UpdateCharacterListCommand(sublime_plugin.TextCommand):

    characters = []
    filename = ''

    def run(self, edit):
        self.characters = []
        c = Characters()
        c.on_activated(self.view)


class ShowCharactersCommand(sublime_plugin.TextCommand):

    person = ''
    unsorted_characters = []
    sorted_characters = []

    def run(self, edit):
        if sublime.load_settings('Fountainhead.sublime-settings').get('characters', True) and int(sublime.version()) >= 3000:
            self.sorted_characters = sorted(self.unsorted_characters)
            self.view.show_popup_menu(self.sorted_characters, self.on_done)

            self.view.run_command('insert', {"characters": self.person})

    def on_done(self, index):
        if index == -1:
            self.person = ''
        else:
            self.person = self.sorted_characters[index]
