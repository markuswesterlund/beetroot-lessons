channels = ["SVT1", "SVT2", "TV4", "Kanal 5", "TV6", "ZTV"]


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.active_channel = 0

    def first_channel(self):
        self.active_channel = 0
        return self.channels[self.active_channel]

    def last_channel(self):
        self.active_channel = -1
        return self.channels[self.active_channel]

    def turn_channel(self, N):
        if N > len(self.channels):
            raise ValueError("Unknown channel")
        self.active_channel = N - 1
        return self.channels[self.active_channel]

    def next_channel(self):
        if self.active_channel == len(self.channels) - 1:
            self.active_channel = 0
        else:
            self.active_channel += 1

        return self.channels[self.active_channel]

    def previous_channel(self):
        if self.active_channel == 0:
            self.active_channel = len(self.channels) - 1
        else:
            self.active_channel -= 1
        return self.channels[self.active_channel]

    def current_channel(self):
        return self.channels[self.active_channel]

    def is_exist(self, channel):
        if (isinstance(channel, int) and 1 < channel < len(self.channels) + 1) or channel in self.channels:
            return "YES"
        else:
            return "NO"


controller = TVController(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(3))
print(controller.next_channel())
print(controller.current_channel())
print(controller.previous_channel())
