import ICommand


class CommandDraw(ICommand.ICommand):

    def execute(self):
        self.boy.draw()
