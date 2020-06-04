actor Switch():
    config:
        #config
    states:
        state on: "/on"
    actions:


actor Light(switch):
    config:
        #config
    states:
        state illuminated: "/active"
    actions:
        trigger switch.on:
            illuminated = switch.on

instantiate kitchen_switch: Switch "//data/sensor/switch[location='Kitchen']"


bind kitchen_switch(params*)










kitchen_switch = Switch: "//data/sensor/switch[location='Kitchen']"
kitchen_light = Light: "//data/devices/light[location='Kitchen']"



Light "//data/devices/light[location='Kitchen']"

kitchen_light.bind(kitchen_switch)




kitchen_switch = Switch()
kitchen_light = Light(kitchen_switch)

kitchen_switch("//data/sensor/switch[location='Kitchen']")
kitchen_light.bind("//data/devices/light[location='Kitchen']")