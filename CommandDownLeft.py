import ICommand


class CommandDownLeft(ICommand.ICommand):

    def execute(self):
        self.boy.down_left()
