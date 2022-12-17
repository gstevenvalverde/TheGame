import ICommand


class CommandLeft(ICommand.ICommand):

    def execute(self):
        self.boy.left()
