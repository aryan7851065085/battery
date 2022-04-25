import psutil
battery = psutil.sensors_battery()
percent = str(battery.percent)
plugged = battery.power_plugged
plugged = "Plugged In" if plugged else "Not Plugged In"
print(f'Battery : {percent}% Device Is {plugged}')