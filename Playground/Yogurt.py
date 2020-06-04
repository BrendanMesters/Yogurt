actor switch(dblink):
    config:
        #config
    states:
        state on: "/on"
    actions:
        trigger foobar:


actor light(dblink, switch):
    config:
        #config
    states:
        illuminated: "/active"
    actions:
        trigger switch.on:
            illuminated = switch.on


kitchen_light = light("//data/devices/light[location='Kitchen']")
kitchen_switch = switch("//data/sensor/switch[location='Kitchen']")


kitchen_light.input(switch = kitchen_switch)