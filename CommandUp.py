import ICommand


class CommandUp(ICommand.ICommand):

    def execute(self):
        self.boy.up()
