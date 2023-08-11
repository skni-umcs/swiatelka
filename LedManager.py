from datetime import datetime
from gi.repository import GLib
from systemd import journal

import dbus
import dbus.service
import dbus.mainloop.glib
import PyDMX

class LedManager(dbus.service.Object):
    def __init__(self, bus, path):
        self.array = [0, 0, 0]
        self.time = None
        self.ready = False
        dbus.service.Object.__init__(self, bus, path)

    def loop(self):
        if datetime.now().replace(microsecond=0) == self.time and self.ready:
            self.DisplayArray(self.array, False)
            self.ready = False
        return True

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='ay', out_signature='')
    def SetArray(self, array):
        self.array = array

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='ay')
    def GetArray(self):
        return self.array

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='s', out_signature='')
    def SetTime(self, time):
        self.time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
        self.ready = True

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='s')
    def GetTime(self):
        return self.time.strftime("%d/%m/%Y %H:%M:%S")

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='ayb', out_signature='')
    def DisplayArray(self, dmx_values, debug):
        dmx_values = dmx_values[::-1]
        dmx_values = [max(0, min(int(x), 255)) for x in dmx_values]
        if debug:
            for i in range(0, len(dmx_values), 3):
                journal.send(f"{i + 1}: {dmx_values[i + 2]}")
                journal.send(f"{i + 2}: {dmx_values[i + 1]}")
                journal.send(f"{i + 3}: {dmx_values[i + 0]}")
            return

        try:
            dmx_device = PyDMX.PyDMX('/dev/ttyUSB0')
            for i in range(0, len(dmx_values), 3):
                dmx_device.set_data(i + 1, dmx_values[i + 2])
                dmx_device.set_data(i + 2, dmx_values[i + 1])
                dmx_device.set_data(i + 3, dmx_values[i + 0])
            dmx_device.send()
        except Exception as err:
            journal.send(f"Exception: {err}")

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='s')
    def Test(self):
        journal.send("Hello from LedManager!")
        return "Hello from LedManager!"

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='')
    def Exit(self):
        journal.send("Exiting LedManager")
        mainloop.quit()

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    system_bus = dbus.SystemBus()
    name = dbus.service.BusName("pl.umcs.skni.LedManager", system_bus)
    object = LedManager(system_bus, '/pl/umcs/skni/LedManager')

    mainloop = GLib.MainLoop()
    journal.send("Running LedManager")
    GLib.idle_add(object.loop)
    mainloop.run()
