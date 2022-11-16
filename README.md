# Traffic_Lights_Electrical_Engineering
A project to construct a functional traffic lights system for Advanced Electrical Engineering course

## How to Run
First, make sure that all necessary Python modules are installed. 

Then, to initiate the traffic light simulation system, run as follows:
```
python3.7 traffic_light_simulator.py
```
This should prompt an user input on the terminal where you can input the pedestrian or car traffic. 

In order to run the arduino control function via pyserial, first create an Arduino script after you have modeled the traffic light system via components like LEDs. In this script, you should trigger all of the output signals through the serial port input by using the following structure:
```
yourVar = Serial.read();

if (yourVar = LG) { // LG = light traffic road green
    digitalWrite(yourPin1, HIGH);
}
if (yourVar = HG) { // HG = heavy traffic road green
    digitalWrite(yourPin2, HIGH);
} 
...
```
Once you have finished your arduino script, set up the Serial Port accordingly in the python script by changing the variable: *PORT* to the port that is connected to your Arduino board.

Finally, run the following command: 
```
python3.7 traffic_light_arduino.py
```
As with the simulator, this will prompt an user input on the terminal. 

*Note: if using a different version of Python, some threading function syntex may need to be changed. Please visit the official threading Python documentation for more information: https://docs.python.org/3.10/library/threading.html*
## Project Description
By using Thread module from threading and time module to simulate a virtual environment for asynchronous function calls, I was able to successfully achieve concurrent task calls and implement a looped program that models a traffic light system at an intersection where three variables exist: pedestrians, cars on road 1, and cars on road 2. 

The premise of this challenge lies in having a default condition of road 1 taking priority, hence being named "Heavy Road," and adjusting the traffic light system in a logical, systematic way to allow pedestrians and cars in road 2, the "Light Road," to cross/pass the street accordingly without disrupting traffic. 

I allot a buffer time that allows for cars in the heavy road to finish passing for a certain duration before allowing either the pedestrians or cars on the other road from passing. In addition, I designate an asynchronous internal cooldown (ICD) metric to check and prevent repeated inputs in either pedestrians or cars on road 2 from completely paralyzing the traffic in road 1 indefinitely. 

