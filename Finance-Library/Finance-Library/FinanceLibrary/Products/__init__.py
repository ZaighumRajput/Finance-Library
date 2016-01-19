from abc import ABCMeta

class ProductInterface:
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

