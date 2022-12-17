import ICommand


class CommandDownRight(ICommand.ICommand):

    def execute(self):
        self.boy.down_right()
