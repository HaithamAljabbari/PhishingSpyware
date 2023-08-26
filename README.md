<h1>Introduction</h1>

We are Team Apollo from Future Engineers of WRO2023, Future Engineers is a category where we create a working autonomnous vehicle with open-source hardware such as electromechanical components or controllers. 

Autonomous robots are advanced intelligent machines that can perform tasks and operate in an environment independently without human assistance. They also elminate dangerous jobs for humans becausse they are capable of working in hazardous environments. They can handle lifting heavy loads, toxic substances and repetitive tasks. This has helped companies to prevent many accidents, also saving time and money. Some examples of autonmous robots include autonomous cleaning robots like Roomba, medical delivery robots, and other robots that move freely around a physical space without being physically guided by humans.

<h2>Engineering materials</h2>
The EV3 Medium motor is the first motor that the robots can use to drive its attachments. So far, we have been moving only the wheels of our robots. With the help of the medium motor. The Medium Motor runs at 240-250 rpm , with a running torque of 8 Ncm and a stall torque of 12 Ncm (faster, but less powerful)

![EV3](https://user-images.githubusercontent.com/101916087/236661666-030f9d6b-68d3-44a4-8af5-b1633461205e.jpeg)



Our servomotor is a rotary actuator or linear actuator that allows for precise control of angular or linear position, velocity and acceleration. It consists of a suitable motor coupled to a sensor for positon feedback.

![SERVO](https://user-images.githubusercontent.com/101916087/235341557-77cccdea-9d87-4324-8b55-59c7aa7b43cf.jpeg)

Raspberry Pi 4 is a small single-board computer that runs on ARM64 Linux OS which is based on debian distrobution.
It is responsible for processing all input data from the sensory camera and acts accordingly to it. It has 4GB ram, a 4-pole stereo audio and composite video port and for the camera, it uses Camera Module 3 which comes with 12 IMX708 Quad Bayer sensor and features a High Dynamic Range Mode, making it a very high quality Camera Module. 

![PI4](https://user-images.githubusercontent.com/101916087/235341511-94ac211c-986b-4d27-8e97-62f3fcb628b0.jpeg)

The Pi camera is a portable light weight camera that supports ٍRaspberry Pi. It communicates with Pi using the MIPI camera serial interface protocol. It is normally used in image processing, machine learning or in surveillance projects. Its' still resolution is up to 5 Megapixels and its' video modes are 1080p30, 720p60 and 640 x 480p60/90.

![PiCam](https://user-images.githubusercontent.com/101916087/235341629-eaca2838-3ec3-4641-97b5-8107403502fa.jpeg)

This L298D Based Motor Driver Module is a high-power motor driver perfect for driving DC Motors and Stepper Motors. It is used to get EV3 running for the wheels to move. This module consists of an l298 motor driver IC, a 78MO5 5V regulator, Driver current of 2A, a maxium power of 25W, Logical Current of 0-35mA, Motor Supply Voltage maximum of 46V, Motor Supply Current maximum of 2A, it can control up to two DC/Stepper Motors.

![L298D](https://user-images.githubusercontent.com/101916087/235342951-ed8c2e5c-3eb2-4694-af8b-07a9a87a359e.jpeg)

<h1>The competition rounds</h1>

For the open challenge, we've programmed our Gamma robot to autonomously drive around the playmat without crashing into the walls with the help of our PI camera and servo motor. The PI camera uses black colors in order to detect the track borders and depending on the size and the position of the detected black colors, the servo motor will change in order to avoid the black walls. the distance between the track borders could either be 600mm or 1000mm (+/- 100mm for the international Final) so we prepared our robot to adapt to the changes of the borders in open challenge. There will be a coin toss combination that will determine the starting section. The starting position will be based on the orange and blue lines in the corners of the race track. If the robot detects the blue line first and then the orangle line, it will turn right but if it detects the orange line first and then the blue line, it will turn left. The timing of the round will be 3 minutes.

For the obstacle challenge, we've programmed our Gamma robot to autonomously drive around the playmat without crashing into the walls and obstacle blocks with the help of our PI camera + multi-color detection and servo motor. The PI camera uses black, red and green colors in order to detect the track borders and obstacle blocks, depending on the size and the position of the detected colors, the servo motor will change its angle in order to avoid the black walls and obstacle blocks. the distance between the track borders could either be 600mm or 1000mm (+/- 100mm for the international Final) so we prepared our robot to adapt to the changes of the borders in obstacle challenge. There will be a coin toss combination that will determine the starting section. The starting position will be based on the orange and blue lines in the corners of the race track. If the robot detects the blue line first and then the orangle line, it will turn right but if it detects the orange line first and then the blue line, it will turn left. The timing of the round is also 3 minutes, much like the open challenge.

<h1>Design of the vehicle</h1>

For our Gamma robot it uses a motor driver that runs two steering wheels that it allows it to move. It has a servo motor which changes the angle which allows the robot to drive in a certain angle in order to pass through and avoid obstacles. The PI camera takes in the input of color detections and sends it to the servo motor which will change the angle and direction of the robot. The servo motor is placed inside the base below the PI camera so that it can take control of the two front wheels and change their angle. The motor driver is in the back of the base of the vehicle which takes control of the EV3 medium motor in order to control the steering wheels which drives the robot forward.

The Gamma robot is powered by a regular powerbank and the LEGO Medium Motor is using a 9 volt battery. The powerbank's capacity can range from single charge (3000mAh) to well over (20,000mAh) (Amp hours).
The Raspberry Pi 4 needs an input of around 5 volts and the powerbank should at least have a capacity of 2.5 - 3 amps. The Pi Camera takes about 200-250mA. The LEGO Medium Motor use 9 volts and 35 mA. Meanwhile, the SG90 9G micro servo motor uses 4.8 - 6.6 volts and 70 amps. They power the vehicle together in order for the vehicle to drive the steering wheels to move.                

<h1>3D printed parts</h1>

3D printing (also known as additive manufacturing) is a process of creating three-dimensional physical objects from a digital model. It is a manufacturing technique that builds objects layer by layer, adding material on top of each layer until the final object is created. There are multiple types of 3D printing such as:

• Fused Deposition Modeling (FDM): This method uses a thermoplastic filament that is heated and extruded through a nozzle, which moves along a predefined path to create the object layer by layer.

• Stereolithography (SLA): These printers use a liquid resin that is solidified layer by layer using a laser or ultraviolet light.

• Selective Laser Sintering (SLS): In this technique, a laser fuses powdered material (typically plastics or metals) layer by layer to create the object.

• Digital Light Processing (DLP): Similar to SLA printers, DLP printers use a projector to cure liquid resin layer by layer, producing the final object.

The process typically begins with a digital 3D model created using computer-aided design (CAD) software or obtained from a 3D scanner. The digital model is then sliced into thin cross-sectional layers, and the 3D printer reads these layers to build the object. The printer deposits material layer by layer, often melting or fusing the material to create a solid structure. There are various types of 3D printing technologies, each with its own method of building objects. 

The 3D printer software we use is Cura, a powerful and easy-to-use 3D print slicing software. Cura slices the user's model file into layers and generates printer-specific G-code.
Once the process is complete, you can send G-code to the printer to generate physical objects.

We designed a 3D printed part for our PI camera because there are no LEGO parts that can be integrated with the PI camera. The PI camera is placed inside the part that is being held by other LEGO parts for the robot to see the obstacles in its way. 

<h1>The workings of the Gamma robot</h1>

In the Gamma robot, there is a motor driver responsible for the controlling of the movement of two steering wheels, enabling the robot to navigate. Additionally, a servo motor is utilized to adjust the angle, allowing the robot to drive in specific directions and avoid obstacles.
To process color detections, the robot incorporates a PI camera, which captures visual input. This information is then sent to the servo motor, enabling it to modify the angle and alter the robot's direction accordingly.
The servo motor is positioned beneath the PI camera within the robot's base, granting it control over the adjustment of the two front wheels. In terms of the physical layout, the motor driver is situated at the rear of the robot's base. It operates the EV3 medium motor, which is responsible for controlling the steering wheels, propelling the robot forward. We have chosen the EV3 medium motor because it's minimal size allows us to place it in the robot without the need ot enlarge the robot's design. We placed in the back of the robot where the differential gears are at, so that it can control the speed of the vehicle. We have chosen the servo motor because it allows use to steer the vehicle. We have put on the front if the vehicle behind the PI camera in order to steer the vehicle. We placed the PI camera at the front of the vehicle where the servo motor is behind it so that we can visualize what's in front of us. We also installed the raspberry pi 4 that is responsible for the processing of the input data coming from the modules installed on the Gamma robot. The raspberry pi also contains a powerbank. It powers up the raspberry pi which in turn powers the robot as a whole.
The robot contains two lithium ion batterys with each voltage of 3.7V and the model-number of the GAMMA robot is MT3608.
The Gamma robot knows how to drive around the vehicle. The robot has the servo motor which allows the steering of the vehicle.
the robot has the powerbank which has the output of five volts. the robot has the ability to go around the obstacle round and open challenge.
The lithium ion batterys are used to power to the raspberry PI. We use the DC to DC to make the voltage go up to nine volts.





