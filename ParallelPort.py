import parallel


class ParallelPort():
    def __init__(self, port):
        self.parport = parallel.Parallel(port)

    def setPin(self, pin, state):
        if pin == 1:
            self.parport.setDataStrobe(state)
        elif 2 <= pin <= 9:
            if state:
                mask = 2**(pin-2)
                self.parport.setData(self.parport.getData() | mask)
            else:
                mask = 255-2**(pin-2)
                self.parport.setData(self.parport.getData() & mask)
        elif pin == 14:
            self.parport.setAutoFeed(state)
        elif pin == 16:
            self.parport.setInitOut(state)
        elif pin == 17:
            self.parport.setSelect(state)
        else:
            raise ValueError("Pin {0} can't be set!".format(pin))

    def getPin(self, pin):
        if pin == 10:
            return int(self.parport.getInAcknowledge())
        elif pin == 11:
            return int(self.parport.getInBusy())
        elif pin == 12:
            return int(self.parport.getInPaperOut())
        elif pin == 13:
            return int(self.parport.getInSelected())
        elif pin == 15:
            return int(self.parport.getInError())
        elif 2 <= pin <= 9:
            data = '{0:08b}'.format(self.parport.getData())
            return int(data[1-pin])
        else:
            raise ValueError("Pin {0} can't be read!".format(pin))
