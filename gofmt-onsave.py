import sublime, sublime_plugin
from subprocess import call

class gofmt_onsave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        file = view.file_name()
        fileType = file[-3:]
        if (fileType == ".go"):
            call(["gofmt", "-w", file])
