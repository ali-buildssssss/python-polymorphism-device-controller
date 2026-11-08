# python-polymorphism-device-controller

Device Controller (Python Polymorphism Demo)

A small command-line project that shows polymorphism in Python. A car, a mobile and a speaker are completely different classes, but they all respond to the same start() and stop() commands. One simple menu can control all of them.

What it does
Starts all devices with one menu choice
Stops all devices with one menu choice
Keeps running until you choose to quit
Handles wrong input (like text or decimals) without crashing
The main idea: polymorphism

Each class has its own version of start() and stop():

python
car1.start()      # car is starting
mobile1.start()   # mobile is starting
speaker1.start()  # speaker is starting

The helper functions start_devices(device) and stop_devices(device) don't care what kind of device they get. They just call device.start() or device.stop() and each object does its own thing. This style is called duck typing: if it has a start() method, it can be used as a device.

Because of this, adding a new device (a TV, a fan, a laptop) only needs a new class with start() and stop(). The rest of the code stays the same.

OOP concepts used
Concept	Where it shows up
Classes & objects	car, mobile, speaker
Polymorphism	Same method names, different behavior per class
Duck typing	Helper functions work with any object that has start() / stop()
Loops over objects	A devices list is looped through to control everything
Error handling	try/except around the menu input
How to run
Make sure Python 3 is installed.
Save the code as main.py.
Run it:
bash
python main.py
Menu options
1 -> start devices
2 -> stop devices
3 -> quit
Example output
enter your choices: 1
start devices
car is starting
mobile is starting
speaker is starting
Ideas for improvement
Add more devices (TV, fan, laptop)
Let the user start or stop one specific device instead of all of them
Track each device's state (on/off) so a device that is already running can't be started again
Use a parent class or abstract base class (Device) to force every device to have start() and stop()
Fix the input handling so a wrong entry shows the menu again (see below)

# Author

M.Ali Ibrahim
Author

Your Name
