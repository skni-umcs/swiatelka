from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib
import PyDMX

class LedManager(dbus.service.Object):

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='ay', out_signature='')
    def SendArray(self, dmx_values):
        dmx_device = PyDMX.PyDMX('/dev/ttyUSB0')
        dmx_values = dmx_values[::-1]
        dmx_values = [max(0, min(int(x), 255)) for x in dmx_values]
        for i in range(0, len(dmx_values), 3):
            print(f"{i + 1}: {dmx_values[i + 2]}")
            print(f"{i + 2}: {dmx_values[i + 1]}")
            print(f"{i + 3}: {dmx_values[i + 0]}")
            dmx_device.set_data(i + 1, dmx_values[i + 2])
            dmx_device.set_data(i + 2, dmx_values[i + 1])
            dmx_device.set_data(i + 3, dmx_values[i + 0])
        dmx_device.send()

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='s')
    def Test(self):
        return "Hello from LedManager!"

    @dbus.service.method("pl.umcs.skni.LedManager",
                         in_signature='', out_signature='')
    def Exit(self):
        mainloop.quit()

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    system_bus = dbus.SystemBus()
    name = dbus.service.BusName("pl.umcs.skni.LedManager", system_bus)
    object = LedManager(system_bus, '/pl/umcs/skni/LedManager')

    mainloop = GLib.MainLoop()
    print("Running LedManager")
    mainloop.run()
