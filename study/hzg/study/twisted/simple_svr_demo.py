# -*- coding: utf-8 -*-
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class Echo(Protocol):
    def __init__(self):
        self.sentence = ''
    def dataReceived(self, data):
        self.sentence += data
        while '\n' in self.sentence:
            idx = self.sentence.find('\n')
            self.transport.write(self.sentence[:idx + 1])
            self.sentence = self.sentence[idx + 1:]

factory = Factory()
factory.protocol = Echo
reactor.listenTCP(8888, factory)
reactor.run()
