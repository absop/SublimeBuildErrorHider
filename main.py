import sublime
import sublime_plugin


def plugin_loaded():
    from Default.exec import ExecCommand

    exec_hide_phantoms = ExecCommand.hide_phantoms
    exec_update_phantoms = ExecCommand.update_phantoms

    def hide_phantoms(self):
        for file, errs in self.errs_by_file.items():
            view = self.window.find_open_file(file)
            if view:
                view.settings().erase("error_phantom_visible")
        exec_hide_phantoms(self)

    def update_phantoms(self):
        exec_update_phantoms(self)
        for file, errs in self.errs_by_file.items():
            view = self.window.find_open_file(file)
            if view:
                view.settings().set("error_phantom_visible", True)

    ExecCommand.hide_phantoms = hide_phantoms
    ExecCommand.update_phantoms = update_phantoms


class HidePhantomListener(sublime_plugin.ViewEventListener):
    def on_query_context(self, key, operator, operand, match_all):
        return self.view.settings().get('error_phantom_visible', False)
