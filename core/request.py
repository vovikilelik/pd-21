class Request:
    source = None
    destination = None
    cargo = None

    def __init__(self, source=None, destination=None, cargo=None):
        self.source = source
        self.destination = destination
        self.cargo = cargo
