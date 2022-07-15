#!/usr/bin/env python


from inputs import devices, get_gamepad
for device in devices:
    print(devices.gamepads)
while 1:
    [event] = get_gamepad()
    print(event.ev_type, event.code, event.state)
    print(type(event.code), type(event.ev_type), type(event.state))
    print(inp.buttons)