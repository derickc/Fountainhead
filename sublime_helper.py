import sublime
import sublime_plugin


class SublimeHelper(sublime_plugin.EventListener):

    def cursor_scope(self, view, offset=1):
        '''
        Gives the scope based on cursor position.
        '''
        return view.scope_name(view.sel()[0].end() - offset)

    def line_scope(self, view, offset=1):
        '''
        Gives the scope for a given line based on cursor position.  Defaults to the previous line.
        '''
        return view.scope_name(view.text_point(view.rowcol(view.sel()[0].end())[0] - offset, 0))

    def line_string(self, view, offset=1):
        '''
        Gives the string of text for a given line.  Defaults to the previous line.
        '''
        return view.substr(view.line(view.text_point(view.rowcol(view.sel()[0].end())[0] - offset, 0)))

    def scope_list(self, view, scope='text.fountain '):
        '''
        Gives a list of all strings for a given scope.
        '''
        regions = []
        scopes = []
        regions = view.find_by_selector(scope)
        for region in regions:
            scopes.append(view.substr(region))
        return scopes
