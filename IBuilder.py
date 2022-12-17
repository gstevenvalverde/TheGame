from abc import ABC, abstractmethod


class IBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_position(self, x, y):
        pass

    @abstractmethod
    def set_image(self, dir_images):
        pass

    @abstractmethod
    def set_screen(self, screen):
        pass
