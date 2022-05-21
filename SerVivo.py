class SerVivo():

    def __init__(self, est):
        self._energia = est

    def is_vivo(self):
        return self._energia > 0

    def die(self):
        self._energia = 0

    def get_energia(self):
        return self._energia

    def set_energia(self, x):
        self._energia = x