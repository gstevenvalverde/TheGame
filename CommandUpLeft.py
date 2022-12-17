import ICommand


class CommandUpLeft(ICommand.ICommand):

    def execute(self):
        self.boy.up_left()
