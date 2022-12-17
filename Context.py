import MoveCircularStrategy
import IStrategy


class Context:

    strategy: IStrategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, x, y, rect):
        return self.strategy.execute(x, y, rect)
