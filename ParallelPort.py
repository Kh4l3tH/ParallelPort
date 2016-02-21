from lib import parallel


class ParallelPort():
    def __init__(self, port):
        self.pport = parallel.Parallel(port)

    def setPin(self, pin, state):
        if pin == 1:
            self.pport.setDataStrobe(state)
        elif 2 <= pin <= 9:
            if state:
                mask = 2**(pin-2)
                self.pport.setData(self.pport.getData() | mask)
            else:
                mask = 255-2**(pin-2)
                self.pport.setData(self.pport.getData() & mask)
        elif pin == 14:
            self.pport.setAutoFeed(state)
        elif pin == 16:
            self.pport.setInitOut(state)
        elif pin == 17:
            self.pport.setSelect(state)
        else:
            raise ValueError('Pin {0} kann nicht gesetzt werden!'.format(pin))

    def getPin(self, pin):
        if pin == 10:
            return int(self.pport.getInAcknowledge())
        elif pin == 11:
            return int(self.pport.getInBusy())
        elif pin == 12:
            return int(self.pport.getInPaperOut())
        elif pin == 13:
            return int(self.pport.getInSelected())
        elif pin == 15:
            return int(self.pport.getInError())
        elif 2 <= pin <= 9:
            data = '{0:08b}'.format(self.pport.getData())
            return int(data[1-pin])
        else:
            raise ValueError('Pin {0} kann nicht gelesen werden!'.format(pin))
