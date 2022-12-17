import ICommand


class CommandUpRight(ICommand.ICommand):

    def execute(self):
        self.boy.up_right()
