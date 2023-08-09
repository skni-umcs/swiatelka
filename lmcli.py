import dbus

if __name__ == '__main__':
    system_bus = dbus.SystemBus()

    dbus_object = system_bus.get_object("pl.umcs.skni.LedManager", "/pl/umcs/skni/LedManager")

    led_manager = dbus.Interface(dbus_object, "pl.umcs.skni.LedManager")

    reply = led_manager.Test()
    
    print("reply:", reply)
