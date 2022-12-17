import ICommand


class CommandUpdate(ICommand.ICommand):

    def execute(self):
        self.boy.update()
