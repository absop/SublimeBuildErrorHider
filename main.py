import sublime
import sublime_plugin


def plugin_loaded():
    from Default.exec import ExecCommand

    old_hide_phantoms = ExecCommand.hide_phantoms
    old_update_phantoms = ExecCommand.update_phantoms

    def new_hide_phantoms(self):
        for file, errs in self.errs_by_file.items():
            view = self.window.find_open_file(file)
            if view:
                view.settings().erase("error_phantom_visible")
        old_hide_phantoms(self)

    def new_update_phantoms(self):
        old_update_phantoms(self)
        for file, errs in self.errs_by_file.items():
            view = self.window.find_open_file(file)
            if view:
                view.settings().set("error_phantom_visible", True)

    ExecCommand.hide_phantoms = new_hide_phantoms
    ExecCommand.update_phantoms = new_update_phantoms


class HidePhantomListener(sublime_plugin.ViewEventListener):
    def on_query_context(self, key, operator, operand, match_all):
        if key == "error_phantom_visible":
            return self.view.settings().get('error_phantom_visible', False)
        return False
