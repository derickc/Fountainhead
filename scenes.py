import sublime
import sublime_plugin
import re
import os
# import sys
# import platform
# from .sublime_helper import *
try:
    from .sublime_helper import SublimeHelper
except (ImportError, ValueError):
    from sublime_helper import SublimeHelper

cursor_scope = SublimeHelper.cursor_scope
line_scope = SublimeHelper.line_scope
line_string = SublimeHelper.line_string

user = ''
# user_os = platform.system()


class Scenes(sublime_plugin.EventListener):

    scene_headings = []
    scene = ''
    major_scenes = []
    current_scene = ''
    previous_line = 0
    current_line = 0
    filename = ''

    def modified_scene(self, view):
        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('scenes', True):
                if self.scene_headings == []:
                    self.on_activated(view)
                view.set_status('SceneList',
                                '')
                if view.rowcol(view.sel()[0].end())[0] != self.current_line:
                    self.previous_line = self.current_line
                    self.current_line = view.rowcol(view.sel()[0].end())[0]
                    if view.scope_name(view.text_point(self.previous_line + 1, 0) - 2) == 'text.fountain entity.name.function ':
                        self.current_scene = view.substr(view.line(view.text_point(self.previous_line, 0)))
                        scene = self.current_scene
                        if scene[0] == ' ' or scene[0] == '\t':
                            scene = re.split(r'^\s*', scene)[1]
                        if scene not in self.scene_headings:
                            self.scene_headings.append(scene)
                            # if user_os == 'Windows':
                            #     print("Sorry, not supported at this time.")
                            # elif user_os == 'Darwin':
                            if scene.lower() not in self.major_scenes:
                                self.major_scenes.append(scene.lower())
                                self.major_scenes = sorted(self.major_scenes)
                                # proc_env = os.environ.copy()
                                # encoding = sys.getfilesystemencoding()
                                # for k, v in proc_env.items():
                                #     proc_env[k] = os.path.expandvars(v).encode(encoding)
                                # user = (proc_env['HOME']).decode(encoding='UTF-8')
                                # completions = open(user + '/Library/Application Support/Sublime Text 3/Packages/Fountainhead/Scenes.sublime-completions', 'w')
                                # packages_directory = sublime.packages_path()
                                # completions_file = packages_directory + '/Fountainhead/Scenes.sublime-completions'
                                # Create Fountainhead directory if it doesn't exist
                                packages_directory = sublime.packages_path() + '/User/Fountainhead/'
                                if not os.path.exists(packages_directory):
                                    os.mkdir(packages_directory)
                                completions_file = packages_directory + 'Scenes.sublime-completions'
                                completions = open(completions_file, 'w')
                                completions.write('{\n\t\t"scope": "text.fountain - comment - string - entity.other.attribute-name - entity.other.inherited-class - foreground - meta.diff - entity.name.tag - entity.name.class - variable.parameter",\n\n\t\t"completions":\n\t\t[')
                                length = len(self.major_scenes)
                                scene_counter = 0
                                for scene in self.major_scenes:
                                    if scene_counter < length - 1:
                                        completions.write('"%s",' % scene)
                                        scene_counter += 1
                                    else:
                                        completions.write('"%s"' % scene)
                                completions.write(']\n}')
                                completions.close()
                            # Clear out scene list message
                            view.set_status('SceneList',
                                            '')

    def on_modified_async(self, view):
        if int(sublime.version()) >= 3000:
            self.modified_scene(view)

    def on_modified(self, view):
        if int(sublime.version()) < 3000:
            self.modified_scene(view)

    def on_activated(self, view):

        if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
            if sublime.load_settings('Fountainhead.sublime-settings').get('scenes', True):
                if self.filename == view.file_name() and len(self.scene_headings) > 0:
                    pass
                else:
                    view.set_status('SceneList',
                                    'FINDING SCENES...')
                    self.scene_headings = []
                    self.major_scenes = []
                    counter = 0
                    self.filename = view.file_name()
                    try:
                        while counter >= 0:
                            scene = view.substr(view.find_by_selector('text.fountain entity.name.function ')[counter])
                            heading = scene
                            if heading[0] == ' ' or heading[0] == '\t':
                                heading = (re.split(r'^\s*', heading))[1]
                            if heading not in self.scene_headings:
                                if heading[0] != '#':
                                    self.scene_headings.append(heading)
                            counter += 1
                    except IndexError:
                        pass
                    # if user_os == 'Windows':
                    #     print("Sorry, not supported at this time.")
                    # elif user_os == 'Darwin':
                    for scene in self.scene_headings:
                        self.major_scenes.append(scene.lower())
                    self.major_scenes = sorted(self.major_scenes)
                    # proc_env = os.environ.copy()
                    # encoding = sys.getfilesystemencoding()
                    # for k, v in proc_env.items():
                    #     proc_env[k] = os.path.expandvars(v).encode(encoding)
                    # user = (proc_env['HOME']).decode(encoding='UTF-8')

                    # completions = open(user + '/Library/Application Support/Sublime Text 3/Packages/Fountainhead/Scenes.sublime-completions', 'w')
                    # packages_directory = sublime.packages_path()
                    # completions_file = packages_directory + '/Fountainhead/Scenes.sublime-completions'
                    # Create Fountainhead directory if it doesn't exist
                    packages_directory = sublime.packages_path() + '/User/Fountainhead/'
                    if not os.path.exists(packages_directory):
                        os.mkdir(packages_directory)
                    completions_file = packages_directory + 'Scenes.sublime-completions'
                    completions = open(completions_file, 'w')
                    completions.write('{\n\t\t"scope": "text.fountain - comment - string - entity.other.attribute-name - entity.other.inherited-class - foreground - meta.diff - entity.name.tag - entity.name.class - variable.parameter",\n\n\t\t"completions":\n\t\t[')

                    length = len(self.major_scenes)
                    scene_counter = 0
                    for scene in self.major_scenes:
                        if scene_counter < length - 1:
                            completions.write('"%s",' % scene)
                            scene_counter += 1
                        else:
                            completions.write('"%s"' % scene)
                    completions.write(']\n}')
                    completions.close()
                    # Print confirmation message
                    view.set_status('SceneList',
                                    'SCENES FOUND!')
                    ShowScenesCommand.unsorted_scenes = self.scene_headings


class UpdateSceneListCommand(sublime_plugin.TextCommand):

    scene_headings = []
    filename = ''

    def run(self, edit):
        self.scene_headings = []
        s = Scenes()
        s.on_activated(self.view)


class ShowScenesCommand(sublime_plugin.TextCommand):

    scene = ''
    unsorted_scenes = []
    sorted_scenes = []

    def run(self, edit):
        if sublime.load_settings('Fountainhead.sublime-settings').get('scenes', True) and int(sublime.version()) >= 3000:
            self.sorted_scenes = sorted(self.unsorted_scenes)
            self.view.show_popup_menu(self.sorted_scenes, self.on_done)

            self.view.run_command('insert', {"characters": self.scene})

    def on_done(self, index):
        if index == -1:
            self.scene = ''
        else:
            self.scene = self.sorted_scenes[index]
