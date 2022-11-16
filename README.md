# Traffic_Lights_Electrical_Engineering
A project to construct a functional traffic lights system for Advanced Electrical Engineering course

## How to Run
To initiate the traffic light system, run as follows:
```
python3.7 traffic_light_simulator.py
```
This should prompt an user input on the terminal where you can input the pedestrian or car traffic. 

*Note: if using a different version of Python, some threading function syntex may need to be changed. Please visit the official threading Python documentation for more information: https://docs.python.org/3.10/library/threading.html*
## Project Description
By using Thread module from threading and time module to simulate a virtual environment for asynchronous function calls, I was able to successfully achieve concurrent task calls and implement a looped program that models a traffic light system at an intersection where three variables exist: pedestrians, cars on road 1, and cars on road 2. 

The premise of this challenge lies in having a default condition of road 1 taking priority, hence being named "Heavy Road," and adjusting the traffic light system in a logical, systematic way to allow pedestrians and cars in road 2, the "Light Road," to cross/pass the street accordingly without disrupting traffic. 

I allot a buffer time that allows for cars in the heavy road to finish passing for a certain duration before allowing either the pedestrians or cars on the other road from passing. In addition, I designate an asynchronous internal cooldown (ICD) metric to check and prevent repeated inputs in either pedestrians or cars on road 2 from completely paralyzing the traffic in road 1 indefinitely. 

