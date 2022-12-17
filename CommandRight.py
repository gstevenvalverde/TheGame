import ICommand


class CommandRight(ICommand.ICommand):

    def execute(self):
        self.boy.right()
