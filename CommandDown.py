import ICommand


class CommandDown(ICommand.ICommand):

    def execute(self):
        self.boy.down()


