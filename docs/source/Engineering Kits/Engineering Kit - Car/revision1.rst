Revision 1
==========

  * Memory: every time the microcontroller is programmed, the memory remains until it is reprogrammed or the reset button is pressed. As we don’t want the line following or obstacle detecting function to run straight after it is powered, a power on/off button will be implemented on the controller.
Power supply: Two Li-ion 18650 is used to power the robot

  * A 9V battery was tested for use as it is cheaper but we haven’t been successful in getting a rechargeable 9V battery that is functional
While it is being programmed, the computer supplies the microcontroller
The li-ion batteries are USB rechargeable
Remote control: The user can control the robot wirelessly from the remote controller through a radio module. As we want the user to have as many interactions with the electronics of the kit, a physical controller was decided upon instead of an app. 
Open-source: A user can modify any portion of the code 
In the future will provide 3 different difficulties of programming; easy, medium and hard
Easy will provide comments in the code for the user to see how the code works. The user will have to write a very minimum or no code
Medium, there will be commented out sections with instructions for the user to fill in with their own code
Hard, No to very little code will be provided and the user will have to code the functionality from scratch
Documentation: A physical manual will be provided to the user, the manual will also be made available digitally on the CreateBase website
Documentation will provide:
Current applications in industry
Describe what is line following, obstacle avoiding and remote controlling
Describe how it works: the functionality of infrared sensors, ultrasonic sensors and radio modules
Challenges/Community Involvement






Community integration - Daily/weekly challenges, the ability to download user and CreateBase designed projects and the ability to upload and share programs/files with the rest of the community.
The base of the arm will potentially need to be designed in such a way that it can be mounted onto other kits or larger bases.
Arm movement: Servos will have a rotation range of 180 degrees whereas the stepper motor will be able to rotate a full 360 - just need to make sure that this doesn’t result in any tangled wires. 
The base stepper motor will control the waist rotation, the larger servos will be used for the shoulder and elbow joints, while the smaller servos will be used for the wrist roll, wrist and grip.
Waist rotation, wrist roll, wrist rotation and gripper position will all be controlled directly via the remote control/app. The shoulder and waist rotations will be controlled together using a single control by utilising basic inverse kinematics. The current easiest solution is to utilise existing libraries for Arduino code.

Electrical components:
Base arm:
Arduino Uno
Bluetooth
1 stepper motor
2 standard servos 
1 micro servo
Motor shield for controlling the stepper motor (will most likely need to design and build our own)
External power supply (either battery pack or wall adapter)
Gripper:
1 micro servo

Design and aesthetics:
We want the design to be simple, requiring the minimum amount of individual 3D printed parts.
Wires should be enclosed where possible to reduce the chance of them getting caught.
Colour scheme will be mostly white with purple and turquoise highlights. Need to do some testing to see how well the 3D printers operate with multiple colours on the same piece. We have to remember however that our servos are black so if we want exposed servos then we will need to either paint them or choose a colour scheme that won’t make them look out of place.
Square vs round design philosophy? Ideally we want a consistent design philosophy across all of our kits so we kind of need to decide as a team if we are going to favour smooth, round shapes or sharp, square/triangular shapes.
Power supply, Arduino Uno, motor shield and bluetooth module will be encased within the base of the arm.
Do we want the servos to be enclosed or exposed? At the moment I think we should leave them exposed to make them easy to access, reduce weight and make the arm look less bulky.
Stuff to talk about next fortnightly meeting: Universal design language (shapes and colours), we need a universal theme to separate our kits from everything else that is being sold via the marketplace and to make it obvious that all of our kits are related and from the same company. Questions around what shapes and colours we want to use (and how to reconcile this against things like exposed black servos and wires).

Specific use cases:
Schools teaching students about robotics and programming. Students get to build and program an arm using our instruction manuals. Teachers can also set their own programming tasks for students or give them challenges that they have to use their newly acquired programming skills and robotic arm to accomplish.
Parents who want to purchase educational toys for their children. The children get to build their own arm and program it to perform tasks from either our instruction manual, something they find online via our community section or something of their own design.
Using the arm for makeshift assembly lines, including mounting it onto other kits such as an RC car for improved mobility.
An example of using the memory feature would be teaching the robotic arm to stir a cup of coffee for you while you sit at your desk. Press play, manually stir a few times using the arm and then press replay and the robot will automatically interpolate the action into a repeatable sequence, carrying it out indefinitely while you carry on with your work.
Advanced expansion kits will let users upgrade their robotic arm, increasing the variety and difficulty of tasks that they can accomplish. Examples include adding the hardware and tutorials for machine vision and other variants of machine learning.

Learning Outcomes:
The hardware involved in a robotic arm including basic electronic knowledge.
Basic programming knowledge such as variables, loops and functions.
Arduino specific programming skills such as controlling servo and stepper motors and connecting to bluetooth.
How to turn input signals over bluetooth into commands for the arm.
Basics of inverse kinematics and how we can convert a command into the correct movement of the arm.
Preprogramming a set of instructions for the arm to complete.

Integration with other kits:
If the arm is light/small enough it can be mounted on top of an RC car or line follower robot. Will need to determine what kind of weight we want our arm to be able to lift as this will partly dictate the size of the arm. There would need to be mounting support between the base of the arm and the top of the car/line follower. I think that it is better to have the RC car doing its own thing, whereas because the line follower robot is much more industrial in both design and function (box shaped), it would be much easier to place the arm on top of and would make more sense. Part of this kit would be a tutorial to program the line follower/arm system to follow a path, pick up an object, then bring it to a second destination (this is a great example of an easy way to combine two kits as the user would simply be combining two programs that they have already made [follow a line and manipulate a claw] in a new and interesting way).
We could create a glove that could be used to control all of our kits using gestures, including the robotic arm, without needing line-of-sight. If we go for the robotic arm kit then this feature would be something to include.
Multiple robotic arms can be placed together in an assembly line. Would be nice to have multiple arms be controllable via a single program. If so, we would need some method of joining the Arduinos so that there is a centralised controller. Otherwise we can simply have each arm be programmed individually which would require no special support from us.
