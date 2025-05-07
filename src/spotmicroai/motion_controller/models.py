from adafruit_motor import servo

class Coordinate:
    """A class the holds 3 values, x, y and z.

    Used to describe a point in 3-Dimensional space

    Attributes:
        x: The value in the X direction
        y: The value in the Y direction
        z: The value in the Z direction
    """
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

class Keyframe:
    """A class the holds 2 coordinates, the current and previous positions of the leg 

    Attributes:
        previous: The prior location of the leg
        current: The current location of the leg
    """

    previous: Coordinate
    current: Coordinate

    def __init__(self, previous: Coordinate, current: Coordinate):
        self.previous = previous
        self.current = current

class KeyframeCollection:
    """A class that contains the 4 keyframes, one per leg 

    Attributes:
        backLeft: The left hind leg
        backRight: The right hind leg
        frontLeft: The left front leg 
        frontRight: The right front leg
    """

    backLeft: Keyframe
    backRight: Keyframe
    frontLeft: Keyframe
    frontRight: Keyframe

    def __init__(self, backLeft: Keyframe, backRight: Keyframe, frontLeft: Keyframe, frontRight: Keyframe):
        self.backLeft = backLeft
        self.backRight = backRight
        self.frontLeft = frontLeft
        self.frontRight = frontRight

class Instinct:
    """A class defining an instinct 

    Attributes:
        rearLeft: The left rear leg
        rearRight: The right rear leg
        frontLeft: The left front leg 
        frontRight: The right front leg
    """

    rearLeft: Coordinate
    rearRight: Coordinate
    frontLeft: Coordinate
    frontRight: Coordinate

    def __init__(self, rearLeft: Coordinate, rearRight: Coordinate, frontLeft: Coordinate, frontRight: Coordinate):
        self.rearLeft = rearLeft
        self.rearRight = rearRight
        self.frontLeft = frontLeft
        self.frontRight = frontRight

class ServoConfigurations:
    """A class with variables that hold the current configurations of the servo.

    Used to track the configurations of a servo

    Attributes:
        channel: The channel number on the PCA9685 connected to the servo
        min_pulse: The minimum pulse width in microseconds
        max_pulse: The maximum pulse width in microseconds
        rest_angle: The value of the resting angle of the servo
    """
    channel = int
    minPulse = int
    maxPulse = int
    restAngle = float

    def __init__(self, channel: int, minPulse, maxPulse, restAngle):
        self.channel = channel
        self.minPulse = minPulse
        self.maxPulse = maxPulse
        self.restAngle = restAngle

class ServoConfigurationsForLimb:
    """A class containing the configurations for the 3 servos in a single limb.

    Used to track the configurations of 3 servos making a single limb

    Attributes:
        shoulder: The shoulder servo
        leg: The leg servo
        foot: The foot servo
    """
    shoulder = ServoConfigurations
    leg = ServoConfigurations
    foot = ServoConfigurations

    def __init__(self, shoulder: ServoConfigurations, leg: ServoConfigurations, foot: ServoConfigurations):
        self.shoulder = shoulder
        self.leg = leg
        self.foot = foot

class ServoConfigurationsCollection:
    """A class containing the configurations for all the 12 servos.

    Used to track the configurations of all servos

    Attributes:
        rearLeft: The rear left limb
        rearRight: The rear right limb
        frontLeft: The front left limb
        frontRight: The front right limb
    """
    rearLeft = ServoConfigurationsForLimb
    rearRight = ServoConfigurationsForLimb
    frontLeft = ServoConfigurationsForLimb
    frontRight = ServoConfigurationsForLimb

    def __init__(self, rearLeft: ServoConfigurationsForLimb, rearRight: ServoConfigurationsForLimb, frontLeft: ServoConfigurationsForLimb, frontRight: ServoConfigurationsForLimb):
        self.rearLeft = rearLeft
        self.rearRight = rearRight
        self.frontLeft = frontLeft
        self.frontRight = frontRight

class ServoStateForLimb:
    """A class containing the servos in a single limb.

    Used to track the servos that form a single limb

    Attributes:
        shoulder: The shoulder servo
        leg: The leg servo
        foot: The foot servo
    """
    shoulder = servo.Servo
    leg = servo.Servo
    foot = servo.Servo

    def __init__(self, shoulder: servo.Servo, leg: servo.Servo, foot: servo.Servo):
        self.shoulder = shoulder
        self.leg = leg
        self.foot = foot

class ServoStateCollection:
    """A class containing all the 12 servos.

    Used to track all 12 servos

    Attributes:
        rearLeft: The rear left limb
        rearRight: The rear right limb
        frontLeft: The front left limb
        frontRight: The front right limb
    """

    rearLeft = ServoStateForLimb
    rearRight = ServoStateForLimb
    frontLeft = ServoStateForLimb
    frontRight = ServoStateForLimb

    def __init__(self, rearLeft: ServoStateForLimb, rearRight: ServoStateForLimb, frontLeft: ServoStateForLimb, frontRight: ServoStateForLimb):
        self.rearLeft = rearLeft
        self.rearRight = rearRight
        self.frontLeft = frontLeft
        self.frontRight = frontRight