import ICommand


class Play:
    commands = []

    def set_command(self, command: ICommand):
        self.commands.append(command)
        command.execute()
