import sublime
import sublime_plugin

back_file_name = ''

class GoToFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global back_file_name
        selectionRegion = self.view.sel()[0]
        lineRegion = self.view.line(selectionRegion.begin())
        line = self.view.substr(lineRegion)

        startIndex = line.find("'")
        endIndex = line.find("'", startIndex + 1)

        file_name = line[startIndex + 1 : endIndex]
        
        if (file_name.find('.js') == -1) :
            file_name = file_name + '.js'

        window = self.view.window()

        window.open_file(file_name)
        back_file_name = self.view.file_name()
        print(current_file_name)

class BackToFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global back_file_name
        window = self.view.window()

        window.open_file(back_file_name)
        back_file_name = ''