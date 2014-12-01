# import sublime
import sublime_plugin


class AutoScrollCommand(sublime_plugin.EventListener):
    pagesWritten = 0

    def on_activated(self, view):
        # if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
        if 'Fountainhead.tmLanguage' in view.settings().get('syntax'):
            # if sublime.load_settings('Fountainhead.sublime-settings').get('auto_scroll', True):
            if view.settings().get('auto_scroll', True):
                view.set_status('AutoScrollCommand',
                                'Pages written: %d' % self.pagesWritten)

    def on_modified(self, view):
        # if view.settings().get('syntax') == 'Packages/Fountainhead/Fountainhead.tmLanguage':
        if 'Fountainhead.tmLanguage' in view.settings().get('syntax'):
            # if sublime.load_settings('Fountainhead.sublime-settings').get('auto_scroll', True):
            if view.settings().get('auto_scroll', True):
                self.currentY = view.text_to_layout(view.sel()[0].begin())[1]
                self.viewportY = view.viewport_position()[1]
                self.viewportHeight = view.viewport_extent()[1]
                self.lineHeight = view.line_height()
                self.pageLines = ((self.currentY - self.viewportY) /
                                  self.lineHeight)
                self.rowCounter = 1
                self.stopCounter = 0
                # sets how many rows to look for a previous element (a row can be many lines)
                self.rowCounterLimit = 8
                # sets the threshold on how many lines to look for a previous element
                self.lineAmount = 8
                # sets how many lines to scroll up if scrolling to the previous element is too much
                self.scrollAmount = 6

                if (self.currentY >= (self.viewportY + self.viewportHeight -
                                     (1.9 * self.lineHeight))):
                    self.rowCounter = 1
                    while (self.rowCounter <= self.rowCounterLimit and
                            self.stopCounter == 0):
                        self.currentRow = (view.rowcol(view.sel()[0].begin()))[0]
                        self.scope = view.scope_name(view.text_point((self.currentRow - self.rowCounter - 1), 0))
                        # Needed?
                        # if (self.scope == 'text.fountain keyword entity.other.attribute-name '):
                        #     self.rowCounter += 1
                        # Needed?
                        # elif (self.scope == 'text.fountain keyword '):
                        #     self.rowCounter += 1
                        if (self.scope == 'text.fountain ') and (view.text_point((self.currentRow - self.rowCounter), 0) == view.text_point((self.currentRow - self.rowCounter - 1), 1)):
                            self.rowCounter += 1
                        # Scene Heading
                        elif (self.scope == 'text.fountain entity.name.function '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Character Name
                        elif (self.scope == 'text.fountain string entity.name.class '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Action
                        elif (self.scope == 'text.fountain foreground '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Notes
                        elif (self.scope == 'text.fountain variable.parameter '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Synopses
                        elif (self.scope == 'text.fountain meta.diff '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                # view.run_command('scroll_lines', {"amount": -(self.pageLines - (self.rowCounter + 0.5)) })
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        elif (self.scope == 'text.fountain '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Section
                        elif (self.scope == 'text.fountain entity.name.filename '):
                            self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                            if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                                view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                            else:
                                view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                                self.pagesWritten += 1
                                view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                                self.stopCounter = 1
                                self.rowCounter = 1
                        # Boneyard
                        # elif (self.scope == 'text.fountain comment '):
                        #     self.newY = view.text_to_layout((view.text_point((self.currentRow - self.rowCounter - 1), 0)))[1]
                        #     if (((self.currentY - self.newY) / self.lineHeight) > self.lineAmount):
                        #         view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                        #         self.pagesWritten += 1
                        #         view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                        #         self.stopCounter = 1
                        #         self.rowCounter = 1
                        #     else:
                        #         view.run_command('scroll_lines', {"amount": -(((self.newY - self.viewportY) / self.lineHeight) - (0.5))})
                        #         self.pagesWritten += 1
                        #         view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                        #         self.stopCounter = 1
                        #         self.rowCounter = 1
                        else:
                            self.rowCounter += 1

                    while ((self.rowCounter > self.rowCounterLimit) and self.stopCounter == 0):
                        view.run_command('scroll_lines', {"amount": -(self.pageLines - self.scrollAmount)})
                        self.pagesWritten += 1
                        view.set_status('AutoScrollCommand', 'Pages written: %d' % self.pagesWritten)
                        self.stopCounter = 1
