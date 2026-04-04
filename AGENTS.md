You are going to help me write pybricks programs for a lego spike kit PrimeHub controller. We have motors, sensors, primehub.

Here are the docs / code for the pybricks package. Use this as a reference when suggesting pybricks programs.

We typically care only about these modules and objects, but are not limited to these.

"""
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
"""

Here are some sample programs

```
"""
This program is for Kiki the Dog.

Follow the corresponding building instructions in the LEGO® SPIKE™ Prime App.

Kiki shall respond to the blue, yellow or green objects by displaying something
on the Hub's screen.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Color, Icon, Port


# Configure the Hub and the Color Sensor
hub = PrimeHub()
color_sensor = ColorSensor(Port.B)


# Kiki walks around and sees things
while True:
    # if he sees blue, he thinks it's the sky above
    if color_sensor.color() == Color.BLUE:
        hub.display.image([
            [100, 100, 100, 100, 100],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])

    # if he sees yellow, he thinks it's a house
    elif color_sensor.color() == Color.YELLOW:
        hub.display.image(Icon.UP)

    # if he sees green, he thinks it's the grass below
    elif color_sensor.color() == Color.GREEN:
        hub.display.image([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [100, 100, 100, 100, 100]
        ])

    else:
        hub.display.off()
```

```
# Hand-Controlled Grabber:
# press the Force Sensor to grab objects,
# and release the Force Sensor to let go.


from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor, Motor
from pybricks.parameters import Port


# Configure the Hub, the Force Sensor and the Motor
hub = PrimeHub()
force_sensor = ForceSensor(Port.E)
motor = Motor(Port.A)


while True:
    # Grab when the Force Sensor is pressed
    if force_sensor.pressed():
        motor.run(speed=-1000)

    # else let go
    else:
        motor.run_until_stalled(speed=1000)
```

```
"""
This program is for CNC Machine
(in the "Invention Squad: Broken" lesson unit).

Follow the corresponding building instructions in the LEGO® SPIKE™ Prime App.

This program will draw a rectangle.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port


# Configure the Hub, the Force Sensor and the Motor
hub = PrimeHub()
horizontal_motor = Motor(Port.A)
vertical_motor = Motor(Port.C)

# Draw a rectangle
horizontal_motor.run_angle(speed=1000, rotation_angle=400)   # go right
vertical_motor.run_angle(speed=1000, rotation_angle=100)   # go down
horizontal_motor.run_angle(speed=1000, rotation_angle=-400)   # go left
vertical_motor.run_angle(speed=1000, rotation_angle=-100)   # go up
```

Docs and source code starts here

```
./__init__.py
---
from typing import Tuple


version: Tuple[str, str, str] = (
    "hub",
    "3.X.YbZ",
    "v3.X.YbZ-GIT_HASH on DATE",
)


---
./_common.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Generic cross-platform module for typical devices like lights, displays,
speakers, and batteries."""

from __future__ import annotations

from typing import (
    Union,
    Iterable,
    overload,
    Optional,
    Tuple,
    Collection,
    Set,
    TYPE_CHECKING,
)

from .tools import Matrix
from .parameters import Axis, Direction, Stop, Button, Port, Color, Side

if TYPE_CHECKING:
    from typing import Any, Awaitable, TypeVar

    from .parameters import Number

    _T_co = TypeVar("_T_co", covariant=True)

    class MaybeAwaitable(None, Awaitable[None]): ...

    # HACK: Cannot subclass bool, so using Any instead.
    class MaybeAwaitableBool(Any, Awaitable[bool]): ...

    class MaybeAwaitableFloat(float, Awaitable[float]): ...

    class MaybeAwaitableInt(int, Awaitable[int]): ...

    class MaybeAwaitableTuple(Tuple[_T_co], Awaitable[Tuple[_T_co]]): ...

    class MaybeAwaitableColor(Color, Awaitable[Color]): ...


class System:
    """System control actions for a hub."""

    def set_stop_button(
        self, button: Optional[Union[Button, Iterable[Button]]]
    ) -> None:
        """
        set_stop_button(button)

        Sets the button or button combination that stops a running script.

        Normally, the center button is used to stop a running script. You can
        change or disable this behavior in order to use the button for other
        purposes.

        Arguments:
            button (Button): A button such
                as :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>`,
                or a tuple of multiple buttons. Choose ``None`` to disable the
                stop button altogether. If you do, you can still turn the hub
                off by holding the center button for three seconds.
        """

    def shutdown(self) -> None:
        """shutdown()

        Stops your program and shuts the hub down."""

    @overload
    def storage(self, offset: int, *, read: int) -> bytes: ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None: ...

    def storage(self, offset, read=None, write=None):
        """
        storage(offset, write=)
        storage(offset, read=) -> bytes

        Reads or writes binary data to persistent storage.

        This lets you store data that can be used the next time you run the
        program.

        The data will be saved to flash memory when you turn the hub off
        normally. It will not be saved if the batteries are removed *while* the
        hub is still running.

        Once saved, the data will remain available even after you remove the
        batteries.

        Args:
            offset (int): The offset from the start of the user storage memory, in bytes.
            read (int): The number of bytes to read. Omit this argument when writing.
            write (bytes): The bytes to write. Omit this argument when reading.

        Returns:
            The bytes read if reading, otherwise ``None``.

        Raises:
            ValueError:
                If you try to read or write data outside of the allowed range.
        """

    def reset_storage(self) -> None:
        """reset_storage()

        Resets all user settings to default values and erases user programs.
        """

    def info(self) -> dict:
        """info() -> dict

        Gets information about the hub as a dictionary with the following keys:

         - ``"name"``: The hub name. This is the name you see when connecting
           via Bluetooth.
         - ``"reset_reason"``: Why the hub (re)booted. It is ``0`` if the hub
           was previously powered off normally. It is ``1`` if the hub rebooted
           automatically, like after a firmware update. It is ``2`` if the hub
           previously crashed due to a watchdog timeout, which indicates a
           firmware issue.
         - ``"host_connected_ble"``: ``True`` if the hub is connected to a
           computer, tablet, or phone via Bluetooth, and ``False`` otherwise.
         - ``"program_start_type"``: It is ``1`` if the program started
           automatically when the hub was powered on. It is ``2`` if the program
           was started with the hub buttons. It is ``3`` if the program was
           started from your connected computer.

        Returns:
            A dictionary with system info.

        .. versionchanged:: 3.6
            The name and reset reason where previously available as separate
            methods. Now they are included in the info dictionary. The methods
            are still available for backwards compatibility.
        """


class DCMotor:
    """Generic class to control simple motors without rotation sensors, such
    as train motors."""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (Number, %): The duty cycle (-100.0 to 100).
        """

    def stop(self) -> None:
        """stop()

        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction."""

    def brake(self) -> None:
        """brake()

        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving."""

    @overload
    def settings(self, max_voltage: Number) -> None: ...

    @overload
    def settings(self) -> Tuple[int]: ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> Tuple[int]

        Configures motor settings. If no arguments are given,
        this returns the current values.

        Arguments:
            max_voltage (Number, mV):
                Maximum voltage applied to the motor during all motor commands.
        """


class Control:
    """Class to interact with PID controller and settings."""

    scale: int

    """
    Scaling factor between the controlled integer variable
    and the physical output. For example, for a single
    motor this is the number of encoder pulses per degree of rotation.
    """

    @overload
    def limits(
        self,
        speed: Optional[Number] = None,
        acceleration: Optional[Number] = None,
        torque: Optional[Number] = None,
    ) -> None: ...

    @overload
    def limits(self) -> Tuple[int, int, int]: ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> Tuple[int, int, int]

        Configures the maximum speed, acceleration, and torque.

        If no arguments are given, this will return the current values.

        The new ``acceleration`` and ``speed`` limit will become effective
        when you give a new motor command. Ongoing maneuvers are not affected.

        Arguments:
            speed (Number, deg/s or Number, mm/s):
                Maximum speed. All speed commands will be capped to this value.
            acceleration (Number, deg/s² or Number, mm/s²):
                Slope of the speed curve when accelerating or decelerating.
                Use a tuple to set acceleration and deceleration separately.
                If one value is given, it is used for both.
            torque (:ref:`torque`):
                Maximum feedback torque during control.
        """

    @overload
    def pid(
        self,
        kp: Optional[Number] = None,
        ki: Optional[Number] = None,
        kd: Optional[Number] = None,
        integral_deadzone: Optional[Number] = None,
        integral_rate: Optional[Number] = None,
    ) -> None: ...

    @overload
    def pid(self) -> Tuple[int, int, int, int, int]: ...

    def pid(self, *args):
        """pid(kp, ki, kd, integral_deadzone, integral_rate)
        pid() -> Tuple[int, int, int, int, int]

        Gets or sets the PID values for position and speed control.

        If no arguments are given, this will return the current values.

        Arguments:
            kp (int): Proportional position control
                constant. It is the feedback torque per degree of
                error: µNm/deg.
            ki (int): Integral position control constant. It is the feedback
                torque per accumulated degree of error: µNm/(deg s).
            kd (int): Derivative position (or proportional speed) control
                constant. It is the feedback torque per
                unit of speed: µNm/(deg/s).
            integral_deadzone (Number, deg or Number, mm): Zone around the
                target where the error integral does not accumulate errors.
            integral_rate (Number, deg/s or Number, mm/s): Maximum rate at
                which the error integral is allowed to grow.
        """

    @overload
    def target_tolerances(
        self, speed: Optional[Number] = None, position: Optional[Number] = None
    ) -> None: ...

    @overload
    def target_tolerances(self) -> Tuple[int, int]: ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> Tuple[int, int]

        Gets or sets the tolerances that say when a maneuver is done.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): Allowed deviation
                from zero speed before motion is considered complete.
            position (Number, deg or :ref:`distance`): Allowed
                deviation from the target before motion is considered
                complete.
        """

    @overload
    def stall_tolerances(
        self, speed: Optional[Number] = None, time: Optional[Number] = None
    ) -> None: ...

    @overload
    def stall_tolerances(self) -> Tuple[int, int]: ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> Tuple[int, int]

        Gets or sets stalling tolerances.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): If the controller
                cannot reach this speed for some ``time`` even with maximum
                actuation, it is stalled.
            time (Number, ms): How long the controller has to be below this
                minimum ``speed`` before we say it is stalled.
        """


class Model:
    """Class to interact with motor state observer and settings."""

    def state(self) -> Tuple[float, float, float, bool]:
        """state() -> Tuple[float, float, float, bool]

        Gets the estimated angle, speed, current, and stall state of the motor,
        using a simulation model that mimics the real motor.
        These estimates are updated faster than the real measurements,
        which can be useful when building your own PID controllers.

        For most applications it is better to used the *measured*
        :meth:`angle <pybricks.pupdevices.Motor.angle>`,
        :meth:`speed <pybricks.pupdevices.Motor.speed>`,
        :meth:`load <pybricks.pupdevices.Motor.load>`, and
        :meth:`stall <pybricks.pupdevices.Motor.stalled>` state instead.

        Returns:
            Tuple with the estimated angle (deg), speed (deg/s), current (mA),
            and stall state (``True`` or ``False``).
        """

    @overload
    def settings(self, values: tuple) -> None: ...

    @overload
    def settings(self) -> tuple: ...

    def settings(self, speed, time):
        """settings(values)
        settings() -> Tuple

        Gets or sets model settings as a tuple of integers. If no arguments are
        given, this will return the current values. This method is mainly used
        to debug the motor model class. Changing these settings should not be
        needed in user programs.

        .. _model settings: https://docs.pybricks.com/projects/pbio/en/latest/struct__pbio__observer__settings__t.html

        Arguments:
            values (Tuple): Tuple with `model settings`_.
        """


class Motor(DCMotor):
    """Generic class to control motors with built-in rotation sensors."""

    control = Control()
    """The motors use PID control to accurately track the speed and
    angle targets that you specify. You can change its behavior through the
    ``control`` attribute of the motor. See :ref:`control` for an overview
    of available methods."""

    model = Model()
    """Model representing the observer that estimates the motor state."""

    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle.
            gears (list):
                List of gears linked to the motor. The gear connected
                to the motor comes first and the gear connected to the output
                comes last.

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth gear connected to the motor and a 36-tooth gear
                connected to the output. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio. The motor direction remains unchanged by this.
            reset_angle (bool):
                Choose ``True`` to reset the rotation sensor value to the
                absolute marker angle (between -180 and 179).
                Choose ``False`` to keep the
                current value, so your program knows where it left off last
                time.
            profile (Number, deg): Precision profile. This is the approximate
                position tolerance in degrees that is acceptable in your
                application. A lower value gives more precise but more erratic
                movement; a higher value gives less precise but smoother
                movement. If no value is given, a suitable profile for this
                motor type will be selected automatically (about 11 degrees).
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the rotation angle of the motor.

        Returns:
            Motor angle.
        """

    def speed(self, window: Number = 100) -> int:
        """speed(window=100) -> int: deg/s

        Gets the speed of the motor.

        The speed is measured as the change in the motor angle during the
        given time window. A short window makes the speed value more
        responsive to motor movement, but less steady. A long window makes the
        speed value less responsive, but more steady.

        Arguments:
            window (Number, ms): The time window used to determine the speed.

        Returns:
            Motor speed.

        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Checks if the motor is currently stalled.

        It is stalled when it cannot reach the target speed or position, even
        with the maximum actuation signal.

        Returns:
            ``True`` if the motor is stalled, ``False`` if not.
        """

    def load(self) -> int:
        """load() -> int: mNm

        Estimates the load that holds back the motor when it tries to move.

        Returns:
            The load torque.
        """

    def reset_angle(self, angle: Optional[Number]) -> None:
        """
        reset_angle(angle)

        Sets the accumulated rotation angle of the motor to a desired value.

        If this motor is also being used by a drive base, its distance and
        angle values will also be affected. You might want to
        use its :meth:`reset <pybricks.robotics.DriveBase.reset>`
        method instead.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """

    def hold(self) -> None:
        """hold()

        Stops the motor and actively holds it at its current angle."""

    def run(self, speed: Number) -> None:
        """run(speed)

        Runs the motor at a constant speed.

        The motor accelerates to the given speed and keeps running at this
        speed until you give a new command.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed for a given amount of time.

        The motor accelerates to the given speed, keeps running at this speed,
        and then decelerates. The total maneuver lasts for exactly the given
        amount of ``time``.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            time (Number, ms): Duration of the maneuver.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed by a given angle.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            rotation_angle (Number, deg): Angle by which the motor should
                rotate.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed towards a given target angle.

        The direction of rotation is automatically selected based on the target
        angle. It does not matter if ``speed`` is positive or negative.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            target_angle (Number, deg): Angle that the motor should rotate to.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target
                before continuing with the rest of the program.
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Optional[Number] = None,
    ) -> MaybeAwaitableInt:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        Runs the motor at a constant speed until it stalls.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            then (Stop): What to do after coming to a standstill.
            duty_limit (Number, %): Duty cycle limit during this
                command. This is useful to avoid applying the full motor
                torque to a geared or lever mechanism. If it is ``None``, the
                duty limit won't be changed during this command.

        Returns:
            Angle at which the motor becomes stalled.
        """

    def done(self) -> bool:
        """done() -> bool

        Checks if an ongoing command or maneuver is done.

        Returns:
            ``True`` if the command is done, ``False`` if not.
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        Tracks a target angle. This is similar to :meth:`.run_target`, but
        the usual smooth acceleration is skipped: it will move to the target
        angle as fast as possible. This method is useful if you want to
        continuously change the target angle.

        Arguments:
            target_angle (Number, deg): Target angle that the motor should
                rotate to.
        """

    def close(self) -> None:
        """close()

        Closes the motor object so you can call ``Motor`` again to initialize
        a new object.

        This allows advanced users to change properties such as gearing in the
        middle of the program, which can be useful for removeable attachments.
        """


class Speaker:
    """Plays beeps and sounds using a speaker."""

    @overload
    def volume(self, volume: Number) -> None: ...

    @overload
    def volume(self) -> int: ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        Gets or sets the speaker volume.

        If no volume is given, this method returns the current volume.

        Arguments:
            volume (Number, %): Volume of the speaker in the 0-100 range.
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> MaybeAwaitable:
        """beep(frequency=500, duration=100)

        Play a beep/tone.

        Arguments:
            frequency (Number, Hz):
                Frequency of the beep in the 64-24000 Hz range.
            duration (Number, ms):
                Duration of the beep. If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> MaybeAwaitable:
        """play_notes(notes, tempo=120)

        Plays a sequence of musical notes. For example:
        ``["C4/4", "C4/4", "G4/4", "G4/4"]``.

        Each note is a string with the following format:

            - The first character is the name of the note, ``A`` to ``G``
              or ``R`` for a rest.
            - Note names can also include an accidental ``#`` (sharp) or
              ``b`` (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not
              allowed.
            - The note name is followed by the octave number ``2``
              to ``8``. For example ``C4`` is middle C. The octave changes
              to the next number at the note C, for example, ``B3`` is the
              note below middle C (``C4``).
            - The octave is followed by ``/`` and a number that indicates
              the size of the note. For example ``/4`` is a quarter note,
              ``/8`` is an eighth note and so on.
            - This can optionally followed by a ``.`` to make a dotted
              note. Dotted notes are 1-1/2 times as long as notes without a
              dot.
            - The note can optionally end with a ``_`` which is a tie or a
              slur. This causes there to be no pause between this note and
              the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played.
            tempo (int):
                Beats per minute. A quarter note is one beat.
        """


class ColorLight:
    """Control a multi-color light."""

    def on(self, color: Color) -> None:
        """on(color)

        Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light.
        """

    def off(self) -> None:
        """off()

        Turns off the light."""

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        Blinks the light at a given color by turning it on and off for given
        durations.

        The light keeps blinking indefinitely while the rest of your
        program keeps running.

        This method provides a simple way to make basic but useful patterns.
        For more generic and multi-color patterns, use ``animate()``
        instead.

        Arguments:
            color (Color): Color of the light.
            durations (list): Sequence of time values of the
                form ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        Animates the light with a sequence of colors, shown one by
        one for the given interval.

        The animation runs in the background while the rest of your program
        keeps running. When the animation completes, it repeats.

        Arguments:
            colors (list): Sequence of :class:`Color <.parameters.Color>`
                values.
            interval (Number, ms): Time between color updates.
        """


class ExternalColorLight:
    """Control a multi-color light."""

    def on(self, color: Color) -> MaybeAwaitable:
        """on(color)

        Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Turns off the light.
        """


class LightArray3:
    """Control an array of three single-color lights."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of three values to set the brightness
                of each light individually.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Turns off all the lights.
        """


class LightArray4(LightArray3):
    """Control an array of four single-color lights."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of four values to set the brightness
                of each light individually. The order of the lights is shown
                in the image above.
        """


class LightMatrix:
    """Control a rectangular grid of single-color lights."""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        Initializes the light matrix display.

        Arguments:
            rows (int): Number of rows in the grid
            columns (int): Number of columns in the grid
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        Sets the orientation of the light matrix display.

        Only new displayed images and pixels are affected. The existing display
        contents remain unchanged.

        Arguments:
            up (Side): Which side of the light matrix display is "up" in your
                design. Choose ``Side.TOP``, ``Side.LEFT``, ``Side.RIGHT``,
                or ``Side.BOTTOM``.
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        Displays an icon, represented by a matrix of :ref:`brightness`
        values.

        Arguments:
            icon (Matrix): Matrix of intensities (:ref:`brightness`). A 2D
                list is also accepted.
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        Displays an animation made using a list of images.

        Each image has the same format as above. Each image is
        shown for the given interval. The animation repeats
        forever while the rest of your program keeps running.

        Arguments:
            matrices (iter): Sequence of
                :class:`Matrix <pybricks.tools.Matrix>` of intensities.
            interval (Number, ms): Time to display each image in the list.
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        Turns on one pixel at the specified brightness.

        Arguments:
            row (Number): Vertical grid index, starting at 0 from the top.
            column (Number): Horizontal grid index, starting at 0 from the left.
            brightness (Number :ref:`brightness`): Brightness of the pixel.
        """

    def off(self) -> None:
        """off()

        Turns off all the pixels."""

    def number(self, number: Number) -> None:
        """number(number)

        Displays a number in the range -99 to 99.

        A minus sign (``-``) is shown as a faint dot
        in the center of the display. Numbers greater than 99 are
        shown as ``>``. Numbers less than -99 are shown as ``<``.

        Arguments:
            number (int): The number to be displayed.
        """

    def char(self, char: str) -> None:
        """char(char)

        Displays a character or symbol on the light grid. This may
        be any letter (``a``--``z``), capital letter (``A``--``Z``) or one of
        the following symbols: ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): The character or symbol to be displayed.
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        Displays a text string, one character at a time, with a pause
        between each character. After the last character is shown, all lights
        turn off.

        Arguments:
            text (str): The text to be displayed.
            on (Number, ms): For how long a character is shown.
            off (Number, ms): For how long the display is off between
                characters.
        """


class Keypad:
    """Get status of buttons on a keypad layout."""

    def __init__(self, active_buttons): ...

    def pressed(self) -> Set[Button]:
        """pressed() -> Set[Button]

        Checks which buttons are currently pressed.

        Returns:
            Set of pressed buttons.
        """


class Battery:
    """Get the status of a battery."""

    def voltage(self) -> int:
        """voltage() -> int: mV

        Gets the voltage of the battery.

        Returns:
            Battery voltage.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the current supplied by the battery.

        Returns:
            Battery current.
        """


class Charger:
    """Get the status of a battery charger."""

    def connected(self) -> bool:
        """connected() -> bool

        Checks whether a charger is connected via USB.

        Returns:
            ``True`` if a charger is connected, ``False`` if not.
        """

    def status(self) -> int:
        """status() -> int

        Gets the status of the battery charger, represented by one of the
        following values. This corresponds to the battery light indicator
        right next to the USB port.

            0. Not charging (light is off).
            1. Charging (light is red).
            2. Charging is complete (light is green).
            3. There is a problem with the charger (light is yellow).

        Returns:
            Status value.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the charging current.

        Returns:
            Charging current.
        """


class SimpleAccelerometer:
    """Get measurements from an accelerometer."""

    def acceleration(self) -> Tuple[int, int, int]:
        """acceleration() -> Tuple[int, int, int]: mm/s²

        Gets the acceleration of the device.

        Returns:
            Acceleration along all three axes.
        """

    def up(self) -> Side:
        """up() -> Side

        Checks which side of the hub currently faces upward.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` or ``Side.BACK``.
        """

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]

        Gets the pitch and roll angles. This is relative to the
        :ref:`user-specified neutral orientation <robotframe>`.

        The order of rotation is pitch-then-roll. This is equivalent to a
        positive rotation along the robot y-axis and then a positive rotation
        along the x-axis.

        Returns:
            Tuple of pitch and roll angles in degrees.
        """


class IMU:

    def up(self, calibrated: bool = True) -> Side:
        """up(calibrated=True) -> Side

        Checks which side of the hub currently faces upward.

        Arguments:
            calibrated (bool): Choose ``True`` to use calibrated gyroscope and
                accelerometer data to determine which way is up. Choose
                ``False`` to use raw acceleration values.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` or ``Side.BACK``.
        """

    def tilt(self, calibrated: bool = True) -> Tuple[int, int]:
        """tilt(calibrated=True) -> Tuple[int, int]

        Gets the pitch and roll angles. This is relative to the
        :ref:`user-specified neutral orientation <robotframe>`.

        The order of rotation is pitch-then-roll. This is equivalent to a
        positive rotation along the robot y-axis and then a positive rotation
        along the x-axis.

        Arguments:
            calibrated (bool): Choose ``True`` to use calibrated gyroscope and
                accelerometer data to determine the tilt. Choose ``False``
                to use raw acceleration values.

        Returns:
            Tuple of pitch and roll angles in degrees.
        """

    @overload
    def acceleration(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def acceleration(self, calibrated: bool = True) -> Matrix: ...

    def acceleration(self, *args):
        """
        acceleration(axis, calibrated=True) -> float: mm/s²
        acceleration(calibrated=True) -> vector: mm/s²

        Gets the acceleration of the device along a given axis in the
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the acceleration should be
                measured, or ``None`` to get a vector along all axes.
            calibrated (bool): Choose ``True`` to use calibrated acceleration
                values. Choose ``False`` to use raw acceleration values.

        Returns:
            Acceleration along the specified axis. If you specify no axis,
            this returns a vector of accelerations along all axes.
        """

    def ready(self) -> bool:
        """ready() -> bool

        Checks if the device is calibrated and ready for use.

        This becomes ``True`` when the robot has been sitting stationary for a
        few seconds, which allows the device to re-calibrate. It is ``False``
        if the hub has just been started, or if it hasn't had a chance to
        calibrate for more than 10 minutes.

        Returns:
            ``True`` if it is ready for use, ``False`` if not.
        """

    def stationary(self) -> bool:
        """stationary() -> bool

        Checks if the device is currently stationary (not moving).

        Returns:
            ``True`` if stationary for at least a second, ``False`` if it is
            moving.
        """

    @overload
    def settings(
        self,
        *,
        angular_velocity_threshold: float = None,
        acceleration_threshold: float = None,
        heading_correction: float = None,
        angular_velocity_bias: Tuple[float, float, float] = None,
        angular_velocity_scale: Tuple[float, float, float] = None,
        acceleration_correction: Tuple[float, float, float, float, float, float] = None,
    ) -> None: ...

    @overload
    def settings(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        Tuple[float, float, float],
        Tuple[float, float, float],
        Tuple[float, float, float, float, float, float],
    ]: ...

    def settings(self, *args):
        """
        settings(*, angular_velocity_threshold, acceleration_threshold, heading_correction, angular_velocity_bias, angular_velocity_scale, acceleration_correction)
        settings() -> Tuple

        Configures the IMU settings. If no arguments are given,
        this returns the current values. Use keyword arguments for each value
        to ensure correct behavior because settings may be added or changed in
        future releases.

        These IMU settings are saved on the hub. They will keep their values
        until you change them again. The values will be reset to default values
        if you update the hub to a different firmware version or call the
        ``hub.system.reset_storage`` method.

        The ``angular_velocity_threshold`` and ``acceleration_threshold``
        define when the hub is considered stationary. If all
        measurements stay below these thresholds for one second, the IMU
        will recalibrate itself. In a noisy room with high ambient vibrations (such as a
        competition hall), you can increase the thresholds
        slightly to give your robot the chance to calibrate.
        To verify that your settings are working as expected, test that
        the ``stationary()`` method gives ``False`` if your robot is moving,
        and ``True`` if it is sitting still.

        The gyroscope measures how fast the hub rotates to estimate the total
        angle. Due to variations in the production process, each
        hub consistently reports a different value for a full rotation. For
        example, your hub might consistently report `357` degrees for every
        `360` degree turn. You can measure this value
        with ``hub.imu.rotation(-Axis.Z, calibrated=False)`` and enter it as
        the ``heading_correction`` setting. Then, the ``hub.imu.heading()``
        method will take it into account going forward, correctly scaling it
        to 360 degrees for a full rotation.

        Arguments:
            angular_velocity_threshold (Number, deg/s): The threshold for
                variations in the angular velocity below which the hub is
                considered stationary enough to calibrate.
                After a reset the value is 2 deg/s.
            acceleration_threshold (Number, mm/s²): The threshold for
                variations in acceleration below which the hub is considered
                stationary enough to calibrate. After a reset the value
                is 2500 mm/s².
            heading_correction (Number, deg): Number of degrees
                reported by for one full rotation of your robot.
                After a reset the value is 360 degrees. This is applied on top
                of any scaling that is done by the ``angular_velocity_scale``
                setting.
            angular_velocity_bias (tuple, deg/s): Initial bias for angular
                velocity measurements along x, y, and z immediately after boot.
                After a reset the value is (0, 0, 0) deg/s.
            angular_velocity_scale (tuple, deg): Scale adjustment for x, y, and
                z rotation to account for manufacturing differences. After a
                reset the value is (360, 360, 360) deg/s. The correct values
                can be obtained using `hub.imu.rotation(Axis.X, calibrated=False)`
                and repeating it for each axis.
            acceleration_correction (tuple, mm/s²): Scale adjustment for x, y,
                and z gravity magnitude in both directions to account for
                manufacturing differences. After a reset the
                value is (9806.65, -9806.65, 9806.65, -9806.65, 9806.65, -9806.65) mm/s².
                The correct values can be
                obtained using `hub.imu.acceleration(Axis.X, calibrated=False)`
                and repeating it for all axes in both directions.
        """

    def heading(self) -> float:
        """heading() -> float: deg

        Gets the heading angle of your robot. A positive value means a
        clockwise turn.

        The heading is 0 when your program starts. The value continues to grow
        even as the robot turns more than 180 degrees. It does not wrap around
        to -180 like it does in some apps.


        .. note:: *For now, this method only keeps track of the heading while
                  the robot is on a flat surface.*

                  This means that the value is
                  no longer correct if you lift it from the table or turn on
                  a ramp. Try ``hub.imu.heading('3D')`` for a heading value
                  that compensates for this. This will become the default in a
                  future release. If you try it, please let us know on our
                  forums!

        Returns:
            Heading angle relative to starting orientation.

        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        Resets the accumulated heading angle of the robot.

        This cannot be called while a drive base is using the gyro to drive or
        hold position.
        Use :meth:`DriveBase.reset() <pybricks.robotics.DriveBase.reset>`
        instead, which will stop the robot and then set the new heading value.

        .. versionchanged:: 3.6 Resetting the angle while driving is not allowed. Stop first.

        Arguments:
            angle (Number, deg): Value to which the heading should be reset.

        Raises:
            OSError:
                There is a drive base that is currently using the gyro.
        """

    @overload
    def angular_velocity(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def angular_velocity(self, calibrated: bool = True) -> Matrix: ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis, calibrated=True) -> float: deg/s
        angular_velocity(calibrated=True) -> vector: deg/s

        Gets the angular velocity of the device along a given axis in
        the :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the angular velocity should be
                measured, or ``None`` to get a vector along all axes.
            calibrated (bool): Choose ``True`` to compensate for the estimated
                bias and configured scale of the gyroscope. Choose ``False``
                to get raw angular velocity values.

        Returns:
            Angular velocity along the specified axis. If you specify no axis,
            this returns a vector of accelerations along all axes.
        """

    def rotation(self, axis: Axis, calibrated: bool = True) -> float:
        """
        rotation(axis, calibrated=True) -> float: deg

        Gets the rotation of the device along a given axis in
        the :ref:`robot reference frame <robotframe>`.

        This value is useful if your robot *only* rotates along the requested
        axis. For general three-dimensional motion, use the
        ``orientation()`` method instead.

        Arguments:
            axis (Axis): Axis along which the rotation should be measured.
            calibrated (bool): Choose ``True`` to compensate for configured
                scale of the gyroscope. Choose ``False`` to get unscaled values.

        Returns:
            The rotation angle.
        """

    def orientation(self) -> Matrix:
        """
        orientation() -> Matrix

        Gets the three-dimensional orientation of the robot in
        the :ref:`robot reference frame <robotframe>`.

        It returns a rotation matrix whose columns represent the ``X``, ``Y``,
        and ``Z`` axis of the robot.

        Returns:
            The 3x3 rotation matrix.
        """


class CommonColorSensor:
    """Generic color sensor that supports Pybricks color calibration."""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def color(self) -> MaybeAwaitableColor:
        """color() -> Color

        Scans the color of a surface.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Returns:
            Detected color.
        """

    def hsv(self) -> MaybeAwaitableColor:
        """hsv() -> Color

        Scans the color of a surface.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """

    def ambient(self) -> MaybeAwaitableInt:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark)
            to 100% (bright).
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Measures how much a surface reflects the light emitted by the
        sensor.

        Returns:
            Measured reflection, ranging from 0% (no reflection) to
            100% (high reflection).
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None: ...

    @overload
    def detectable_colors(self) -> Collection[Color]: ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        Configures which colors the ``color()`` method should detect.

        Specify only colors that you wish to detect in your application.
        This way, the full-color measurements are rounded to the nearest
        desired color, and other colors are ignored. This improves reliability.

        If you give no arguments, the currently chosen colors will be returned.

        When coding with blocks, this is configured in the sensor setup block.

        Arguments:
            colors (list or tuple): List of :class:`Color <.parameters.Color>`
                objects: the colors that you want to detect. You can pick
                standard colors such as ``Color.MAGENTA``, or provide your
                own colors like ``Color(h=348, s=96, v=40)`` for even
                better results. You measure your own colors with the
                ``hsv()`` method.
        """


class AmbientColorSensor(CommonColorSensor):
    """Like CommonColorSensor, but also detects ambient colors when the sensor
    light is turned off"""

    def color(self, surface: bool = True) -> MaybeAwaitableColor:
        """color(surface=True) -> Color

        Scans the color of a surface or an external light source.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Detected color.`
        """

    def hsv(self, surface: bool = True) -> MaybeAwaitableColor:
        """hsv(surface=True) -> Color

        Scans the color of a surface or an external light source.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """


class BLE:
    """
    Bluetooth Low Energy.

    .. versionadded:: 3.3
    """

    def broadcast(self, data: Union[bool, int, float, str, bytes]) -> MaybeAwaitable:
        """broadcast(data)

        Starts broadcasting the given data on
        the ``broadcast_channel`` you selected when initializing the hub.

        Data may be of type ``int``, ``float``, ``str``, ``bytes``,
        ``True``, or ``False``. It can also be a list or tuple of these.

        Choose ``None`` to stop broadcasting. This helps improve performance
        when you don't need the broadcast feature, especially when observing
        at the same time.

        The total data size is quite limited (26 bytes). ``True`` and
        ``False`` take 1 byte each. ``float`` takes 5 bytes. ``int`` takes 2 to
        5 bytes depending on how big the number is. ``str`` and ``bytes`` take
        the number of bytes in the object plus one extra byte.

        When multitasking, only one task can broadcast at a time. To broadcast
        information from multiple tasks (or block stacks), you could use a
        dedicated separate task that broadcast new values when one or more
        variables change.

        Args:
            data: The value or values to be broadcast.

        .. versionadded:: 3.3
        """

    def observe(
        self, channel: int
    ) -> Optional[Tuple[Union[bool, int, float, str, bytes], ...]]:
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        Retrieves the last observed data for a given channel.

        Receiving data is more reliable when the hub is not connected
        to a computer or other devices at the same time.

        Args:
            channel (int): The channel to observe (0 to 255).

        Returns:
            The received data in the same format as it was sent, or ``None``
            if no recent data is available.

        .. versionadded:: 3.3
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        Gets the average signal strength in dBm for the given channel.

        This indicates how near the broadcasting device is. Nearby devices
        may have a signal strength around -40 dBm, while far away devices
        might have a signal strength around -70 dBm.

        Args:
            channel (int): The channel number (0 to 255).

        Returns:
            The signal strength or ``-128`` if there is no recent observed data.

        .. versionadded:: 3.3
        """

    def version(self) -> str:
        """version() -> str

        Gets the firmware version from the Bluetooth chip.

        .. versionadded:: 3.3
        """


---
./ev3devices.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 motors and sensors."""

from typing import Optional, Tuple, List

from . import _common
from .parameters import (
    Button as _Button,
    Color as _Color,
    Direction as _Direction,
    Port as _Port,
)


class Motor(_common.Motor):
    """LEGO® MINDSTORMS® EV3 Motor."""


class TouchSensor:
    """LEGO® MINDSTORMS® EV3 Touch Sensor."""

    def __init__(self, port: _Port):
        """TouchSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def pressed(self) -> bool:
        """pressed() -> bool

        Checks if the sensor is pressed.

        Returns:
            ``True`` if the sensor is pressed, ``False`` if it is
            not pressed.
        """


class ColorSensor:
    """LEGO® MINDSTORMS® EV3 Color Sensor."""

    def __init__(self, port: _Port):
        """ColorSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def color(self) -> Optional[_Color]:
        """color() -> Color

        Measures the color of a surface.

        Returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``,
            ``Color.YELLOW``, ``Color.RED``, ``Color.WHITE``, ``Color.BROWN``,
            or ``None`` if no color is detected.

        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark)
            to 100% (bright).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0% (no reflection) to
            100% (high reflection).

        """

    def rgb(self) -> Tuple[int, int, int]:
        """rgb() -> Tuple[int, int, int]

        Measures the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            Tuple of reflections for red, green, and blue light, each
            ranging from 0.0% (no reflection) to 100.0% (high reflection).
        """


class InfraredSensor:
    """LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon."""

    def __init__(self, port: _Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self) -> int:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object using
        infrared light.

        Returns:
            Relative distance ranging from 0% (closest)
            to 100% (farthest).

        """

    def beacon(self, channel: int) -> Tuple[Optional[int], Optional[int]]:
        """
        beacon(channel) -> Tuple[int, int]
        beacon(channel) -> Tuple[None, None]

        Measures the relative distance and angle between the remote and the
        infrared sensor.

        Arguments:
            channel (int): Channel number of the remote.

        Returns:
            Tuple of relative distance (0% to 100%) and approximate angle
            (-75 to 75 degrees) between remote and infrared sensor or
            a tuple of (``None``, ``None``) if no remote is detected.
        """

    def buttons(self, channel: int) -> List[_Button]:
        """buttons(channel) -> List[Button]

        Checks which buttons on the infrared remote are pressed.

        This method can detect up to two buttons at once. If you press
        more buttons, you'll still get just two buttons.

        Arguments:
            channel (int): Channel number of the remote.

        Returns:
            List of pressed buttons on the remote on the selected channel.

        """

    def keypad(self) -> List[_Button]:
        """keypad() -> List[Button]

        Checks which buttons on the infrared remote are pressed.

        This method can independently detect all 4 up/down buttons, but
        it cannot detect the beacon button.

        This method only works with the remote in channel 1.

        Returns:
            List of pressed buttons.
        """


class GyroSensor:
    """LEGO® MINDSTORMS® EV3 Gyro Sensor."""

    def __init__(self, port: _Port, direction: _Direction = _Direction.CLOCKWISE):
        """GyroSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
            direction (Direction):
                Positive rotation direction when looking at the red dot on top
                of the sensor.

        """

    def speed(self) -> int:
        """speed() -> int: deg/s

        Gets the speed (angular velocity) of the sensor.

        Returns:
            Angular velocity.

        """

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the accumulated angle of the sensor.

        Returns:
            Rotation angle.

        """

    def reset_angle(self, angle: int) -> None:
        """reset_angle(angle)

        Sets the rotation angle of the sensor to a desired value.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor."""

    def __init__(self, port: _Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self, silent: bool = False) -> int:
        """distance(silent=False) -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Arguments:
            silent (bool): Choose ``True`` to turn the sensor off after
                           measuring the distance. This reduces interference
                           with other ultrasonic sensors. If you do
                           this too frequently, the sensor can freeze.
                           If this happens, unplug it and plug it back in.

        Returns:
            Measured distance.

        """

    def presence(self) -> bool:
        """presence() -> bool

        Checks for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        If the other ultrasonic sensor is operating in silent mode, you can
        only detect the presence of that sensor while it is taking a
        measurement.

        Returns:
            ``True`` if ultrasonic sounds are detected,
            ``False`` if not.
        """


---
./hubs.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Programmable Hubs."""

from typing import Sequence

from . import _common
from .ev3dev import _speaker
from .media.ev3dev import Image as _Image
from .parameters import Button as _Button, Axis


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.UP,
            _Button.DOWN,
        ]
    )
    screen = _Image("_screen_")
    speaker = _speaker.Speaker()
    battery = _common.Battery()
    light = _common.ColorLight()


class MoveHub:
    """LEGO® BOOST Move Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.SimpleAccelerometer()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = None, observe_channels: Sequence[int] = []
    ):
        """MoveHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = None, observe_channels: Sequence[int] = []
    ):
        """CityHub(broadcast_channel=None, observe_channels=[])

        Arguments:
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and front side
        (with the light) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class EssentialHub:
    """LEGO® SPIKE Essential Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad([_Button.CENTER])
    charger = _common.Charger()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """EssentialHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and the front side (with the USB
        port, and I/O ports A and B) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """
        pass


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        ]
    )
    charger = _common.Charger()
    light = _common.ColorLight()
    display = _common.LightMatrix(5, 5)
    speaker = _common.Speaker()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the buttons) and front side (with the USB
        port) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).

        .. versionchanged:: 3.3
            Added *broadcast_channel* and *observe_channels* arguments.
        """


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""


# HACK: hide from jedi
del Axis


---
./iodevices.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Generic input/output devices."""

from __future__ import annotations

from typing import Dict, Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Port as _Port

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


class PUPDevice:
    """Powered Up motor or sensor."""

    def __init__(self, port: _Port):
        """PUPDevice(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def info(self) -> Dict[str, str]:
        """info() -> Dict

        Gets information about the device.

        Returns:
            Dictionary with information, such as the device ``id``.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values from a given mode.

        Arguments:
            mode (int): Device mode.

        Returns:
            Values read from the sensor.
        """

    def write(self, mode: int, data: Tuple) -> MaybeAwaitable:
        """write(mode, data)

        Writes values to the sensor. Only selected sensors and modes support
        this.

        Arguments:
            mode (int): Device mode.
            data (tuple): Values to be written.
        """


class LUMPDevice:
    """Devices using the LEGO UART Messaging Protocol."""

    def __init__(self, port: _Port):
        """LUMPDevice(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values from a given mode.

        Arguments:
            mode (int): Device mode.

        Returns:
            Values read from the sensor.
        """


class DCMotor(_common.DCMotor):
    """DC Motor for LEGO® MINDSTORMS EV3."""


class Ev3devSensor:
    """Read values of an ev3dev-compatible sensor."""

    sensor_index: int
    """Index of the ev3dev sysfs `lego-sensor`_ class."""

    port_index: int
    """Index of the ev3dev sysfs `lego-port`_ class."""

    def __init__(self, port: _Port):
        """Ev3devSensor(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def read(self, mode: str) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Reads values at a given mode.

        Arguments:
            mode (str): `Mode name`_.

        Returns:
            values read from the sensor.
        """


class AnalogSensor:
    """Generic or custom analog sensor."""

    def __init__(self, port: _Port):
        """AnalogSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Measures analog voltage.

        Returns:
            Analog voltage.
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        Measures resistance.

        This value is only meaningful if the analog device is a passive load
        such as a resistor or thermistor.

        Returns:
            Resistance of the analog device.
        """

    def active(self) -> None:
        """active()

        Sets sensor to active mode. This sets pin 5 of the sensor
        port to `high`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light on.
        From then on, ``voltage()`` returns the raw reflected light value.
        """

    def passive(self) -> None:
        """passive()

        Sets sensor to passive mode. This sets pin 5 of the sensor
        port to `low`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light off.
        From then on, ``voltage()`` returns the raw ambient light value.
        """


class I2CDevice:
    """Generic or custom I2C device."""

    def __init__(self, port: _Port, address: int):
        """I2CDevice(port, address)

        Arguments:
            port (Port): Port to which the device is connected.
            address(int): I2C address of the client device. See
                :ref:`I2C Addresses <i2caddress>`.
        """

    def read(self, reg: Optional[int], length: Optional[int] = 1) -> bytes:
        """read(reg, length=1)

        Reads bytes, starting at a given register.

        Arguments:
            reg (int): Register at which to begin
                reading: 0--255 or 0x00--0xFF.
            length (int): How many bytes to read.

        Returns:
            Bytes returned from the device.
        """

    def write(self, reg: Optional[int], data: Optional[bytes] = None) -> None:
        """write(reg, data=None)

        Writes bytes, starting at a given register.

        Arguments:
            reg (int): Register at which to begin
                writing: 0--255 or 0x00--0xFF.
            data (bytes): Bytes to be written.
        """


class UARTDevice:
    """Generic UART device."""

    def __init__(self, port: _Port, baudrate: int, timeout: Optional[int] = None):
        """UARTDevice(port, baudrate, timeout=None)

        Arguments:
            port (Port): Port to which the device is connected.
            baudrate (int): Baudrate of the UART device.
            timeout (Number, ms): How long to wait
                during ``read`` before giving up. If you choose ``None``,
                it will wait forever.
        """

    def read(self, length: int = 1) -> bytes:
        """read(length=1) -> bytes

        Reads a given number of bytes from the buffer.

        Your program will wait until the requested number of bytes are
        received. If this takes longer than ``timeout``, the ``ETIMEDOUT``
        exception is raised.

        Arguments:
            length (int): How many bytes to read.

        Returns:
            Bytes returned from the device.
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        Reads all bytes from the buffer.

        Returns:
            Bytes returned from the device.
        """

    def write(self, data: bytes) -> None:
        """write(data)

        Writes bytes.

        Arguments:
            data (bytes): Bytes to be written.
        """

    def waiting(self) -> int:
        """waiting() -> int

        Gets how many bytes are still waiting to be read.

        Returns:
            Number of bytes in the buffer.
        """

    def clear(self) -> None:
        """clear()

        Empties the buffer."""


class LWP3Device:
    """
    Connects to a hub running official LEGO firmware using the
    `LEGO Wireless Protocol v3`_.

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(
        self,
        hub_kind: int,
        name: str = None,
        timeout: int = 10000,
        pair: bool = False,
        num_notifications: int = 8,
    ):
        """LWP3Device(hub_kind, name=None, timeout=10000, pair=False, num_notifications=8)

        Arguments:
            hub_kind (int):
                The `hub type identifier`_ of the hub to connect to.
            name (str):
                The name of the hub to connect to or ``None`` to connect to any
                hub.
            timeout (int):
                The time, in milliseconds, to wait for a connection before
                raising an exception.
            pair (bool): Whether to attempt pairing for a secure connection.
                This is required for some newer hubs.
            num_notifications (int): Number of incoming messages from the remote
                hub to store before discarding older messages.

        .. versionchanged:: 3.6

            Added ``pair`` parameter.

        .. versionchanged:: 3.7

            Added ``num_notifications`` parameter.

        .. _`hub type identifier`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the device.

        Arguments:
            name (str): New Bluetooth name of the device. If no name is given,
                this method returns the current name.
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        Sends a message to the remote hub.

        Arguments:
            buf (bytes): The raw binary message to send.
        """

    def read(self) -> bytes | None:
        """read() -> bytes | None

        Retrieves the oldest buffered message received from the remote hub.

        If all buffered messages have already been read, this returns ``None``.

        Returns:
            The oldest raw binary message or ``None`` if there are no more messages.

        .. versionchanged:: 3.7

            Now supports reading multiple buffered messages instead of blocking
            until one new message was received.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the remote LWP3Device from the hub.
        """


class XboxController:
    """Use the Microsoft® Xbox® controller as a sensor in your projects to
    control them remotely.

    The hub will scan for the controller and connect to it. It will disconnect
    when the program ends.

    For tips on connectivity and pairing, see :ref:`below <xbox-controller-pairing>`.
    """

    buttons = _common.Keypad([])

    def __init__(self):
        """"""

    def joystick_left(self) -> Tuple[int, int]:
        """joystick_left() -> Tuple

        Gets the left joystick position as percentages between -100%
        and 100%. The center position is (0, 0).

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.
        """

    def joystick_right(self) -> Tuple[int, int]:
        """joystick_right() -> Tuple

        Gets the right joystick position as percentages between -100%
        and 100%. The center position is (0, 0).

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.
        """

    def triggers(self) -> Tuple[int, int]:
        """triggers() -> Tuple

        Gets the left and right trigger positions as percentages between 0%
        and 100%.

        Returns:
            Tuple of left and right trigger positions.
        """

    def dpad(self) -> int:
        """dpad() -> int

        Gets the direction-pad value. ``1`` is up, ``2`` is up-right, ``3``
        is right, ``4`` is down-right, ``5`` is down, ``6`` is down-left,
        ``7`` is left, ``8`` is up-left, and ``0`` is not pressed.

        This is essentially the same as reading the state of the
        ``Button.UP``, ``Button.RIGHT``, ``Button.DOWN``, and ``Button.LEFT``
        buttons, but this method conveniently returns a number that indicates
        a direction.

        Returns:
            Direction-pad position, indicating a direction.
        """

    def profile(self) -> int:
        """profile() -> int

        Gets the current profile of the controller. Only available on the
        Xbox Elite Controller Series 2.

        Returns:
            Profile number.
        """

    def rumble(
        self,
        power: Number | Tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        Makes the builtin actuators rumble, creating force feedback.

        If you give a single ``power`` value, the left and right main actuators
        will both rumble with that power. For more fine-grained control, set
        ``power`` as a tuple of four values, which control the left main
        actuator, right main actuator, left trigger actuator, and the right
        trigger actuator, respectively. For example, ``power=(0, 0, 100, 0)``
        makes the left trigger rumble at full power.

        The rumble runs in the background while your program continues. To
        make your program wait, just pause the program for a matching duration.
        For one rumble, this equals ``duration``. For multiple rumbles, this
        equals ``count * (duration + delay)``.

        Arguments:
            power (Number, % or tuple): Rumble power.
            duration (Number, ms): Rumble duration.
            count (int): Rumble count.
            delay (Number, ms): Delay before each rumble. Only if ``count > 1``.
        """


# hide from jedi
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableTuple
    del Number


---
./messaging.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""
Classes to exchange messages between EV3 bricks.
"""

from __future__ import annotations

from typing import abstractmethod, TypeVar, Optional, Callable, Generic

T = TypeVar("T")


class Connection:
    @abstractmethod
    def read_from_mailbox(self, name: str) -> bytes:
        ...

    @abstractmethod
    def send_to_mailbox(self, name: str, data: bytes) -> None:
        ...

    @abstractmethod
    def wait_for_mailbox_update(self, name: str) -> None:
        ...


class Mailbox(Generic[T]):
    def __init__(
        self,
        name: str,
        connection: Connection,
        encode: Optional[Callable[[T], bytes]] = None,
        decode: Optional[Callable[[bytes], T]] = None,
    ):
        """Mailbox(name, connection, encode=None, decode=None)

        Object that represents a mailbox containing data.

        You can read data that is delivered by other EV3 bricks, or send data
        to other bricks that have the same mailbox.

        By default, the mailbox reads and send only bytes. To send other
        data, you can provide an ``encode`` function that encodes your Python
        object into bytes, and a ``decode`` function to convert bytes back to
        a Python object.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
            encode (callable):
                Function that encodes a Python object to bytes.
            decode (callable):
                Function that creates a new Python object from bytes.
        """

    def read(self) -> T:
        """read()

        Gets the current value of the mailbox.

        Returns:
            The current value or ``None`` if the mailbox is empty.
        """
        return ""

    def send(self, value: T, brick: Optional[str] = None) -> None:
        """send(value, brick=None)

        Sends a value to this mailbox on connected devices.

        Arguments:
            value:
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None`` to
                to broadcast to all connected devices.

        Raises:
            OSError:
                There is a problem with the connection.
        """

    def wait(self) -> None:
        """wait()

        Waits for the mailbox to be updated by remote device."""

    def wait_new(self) -> T:
        """wait_new()

        Waits for a new value to be delivered to the mailbox that is not
        equal to the current value in the mailbox.

        Returns:
            The new value.
        """
        return object()


class LogicMailbox(Mailbox[bool]):
    def __init__(self, name: str, connection: Connection):
        """LogicMailbox(name, connection)

        Object that represents a mailbox containing boolean data.

        This works just like a regular :class:`Mailbox`, but values
        must be ``True`` or ``False``.

        This is compatible with the "logic" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class NumericMailbox(Mailbox[float]):
    def __init__(self, name: str, connection: Connection):
        """NumericMailbox(name, connection)

        Object that represents a mailbox containing numeric data.

        This works just like a regular :class:`Mailbox`, but values must be a
        number, such as ``15`` or ``12.345``

        This is compatible with the "numeric" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class TextMailbox(Mailbox[str]):
    def __init__(self, name: str, connection: Connection):
        """TextMailbox(name, connection)

        Object that represents a mailbox containing text data.

        This works just like a regular :class:`Mailbox`, but data must be a
        string, such as ``'hello!'``.

        This is compatible with the "text" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class BluetoothMailboxServer:
    """Object that represents a Bluetooth connection from one or more remote
    EV3s.

    The remote EV3s can either be running MicroPython or the standard EV3
    firmware.

    A "server" waits for a "client" to connect to it.
    """

    def __enter__(self) -> BluetoothMailboxServer:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.server_close()

    def wait_for_connection(self, count: int = 1) -> None:
        """wait_for_connection(count=1)

        Waits for a :class:`BluetoothMailboxClient` on a remote device to
        connect.

        Arguments:
            count (int):
                The number of remote connections to wait for.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def server_close(self) -> None:
        """server_close()

        Closes all connections."""


class BluetoothMailboxClient:
    """Object that represents a Bluetooth connection to one or more remote EV3s.

    The remote EV3s can either be running MicroPython or the standard EV3
    firmware.

    A "client" initiates a connection to a waiting "server".
    """

    def __enter__(self) -> BluetoothMailboxClient:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.close()

    def connect(self, brick: str) -> None:
        """connect(brick)

        Connects to an :class:`BluetoothMailboxServer` on another device.

        The remote device must be paired and waiting for a connection. See
        :meth:`BluetoothMailboxServer.wait_for_connection`.

        Arguments:
            brick (str):
                The name or Bluetooth address of the remote EV3 to connect to.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def close(self) -> None:
        """close()

        Closes all connections."""


---
./nxtdevices.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Use LEGO® MINDSTORMS® NXT motors and sensors with the EV3 brick."""


from .parameters import Port

from ._common import ColorLight, CommonColorSensor
from .iodevices import AnalogSensor


from typing import Callable, Optional, Tuple


class TouchSensor:
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port: Port):
        """TouchSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def pressed(self) -> bool:
        """pressed() -> bool

        Checks if the sensor is pressed.

        Returns:
            ``True`` if the sensor is pressed, ``False`` if it is
            not pressed.
        """


class LightSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port: Port):
        """LightSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark) to 100% (bright).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0% (no reflection) to 100% (high
            reflection).
        """


class ColorSensor(CommonColorSensor):
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = ColorLight()

    def rgb(self) -> Tuple[int, int, int]:
        """Measures the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            Tuple of reflections for red, green, and blue light, each
            ranging from 0.0% (no reflection) to 100.0% (high reflection).
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            Measured distance.
        """


class SoundSensor:
    """LEGO® MINDSTORMS® NXT Sound Sensor."""

    def __init__(self, port: Port):
        """SoundSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def intensity(self, audible_only: bool = True) -> int:
        """intensity(audible_only=True) -> int: %

        Measures the ambient sound intensity (loudness).

        Arguments:
            audible_only (bool): Detect only audible sounds. This tries to
                filter out frequencies that cannot be heard by the
                human ear.

        Returns:
            Sound intensity.
        """


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Temperature Sensor."""

    def __init__(self, port: Port):
        """TemperatureSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def temperature(self) -> int:
        """temperature() -> float: °C

        Measures the temperature.

        Returns:
            Measured temperature.
        """


class EnergyMeter:
    """LEGO® MINDSTORMS® Education NXT Energy Meter."""

    def __init__(self, port: Port):
        """EnergyMeter(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def storage(self) -> int:
        """storage() -> int: J

        Gets the total available energy stored in the battery.

        Returns:
            Remaining stored energy.
        """

    def input(self) -> Tuple[int, int, int]:
        """input() -> Tuple[int, int, int]

        Measures the electrical signals at the input (bottom) side
        of the energy meter. It measures the voltage applied to it and the
        current passing through it. The product of these two values is power.
        This power value is the rate at which the stored energy increases. This
        power is supplied by an energy source such as the provided solar panel
        or an externally driven motor.

        Returns:
            Voltage (mV), current (mA), and power (mW) measured at the input
            port.
        """

    def output(self) -> Tuple[int, int, int]:
        """output() -> Tuple[int, int, int]

        Measures the electrical signals at the output (top) side
        of the energy meter. It measures the voltage applied to the external
        load and the current passing to it. The product of these two values
        is power. This power value is the rate at which the stored energy
        decreases. This power is consumed by the load, such as a light or a
        motor.

        Returns:
            Voltage (mV), current (mA), and power (mW) measured at the output
            port.
        """


class VernierAdapter(AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors."""

    def __init__(self, port: Port, conversion: Optional[Callable[[int], float]] = None):
        """VernierAdapter(port, conversion=None)

        Arguments:
            port (Port): Port to which the sensor is connected.
            conversion (callable): Function of the format :meth:`.conversion`.
                This function is used to convert the raw analog voltage to the
                sensor-specific output value. Each Vernier Sensor has its
                own conversion function. The example given below demonstrates
                the conversion for the Surface Temperature Sensor.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Measures the raw analog sensor voltage.

        Returns:
            Analog voltage.
        """

    def conversion(self, voltage: int) -> float:
        """conversion(voltage) -> float

        Converts the raw voltage (mV) to a sensor value.

        If you did not provide a :meth:`.conversion` function earlier, no
        conversion will be applied.

        Arguments:
            voltage (Number, mV): Analog sensor voltage

        Returns:
            Converted sensor value.
        """

    def value(self) -> float:
        """value() -> float

        Measures the sensor :meth:`.voltage` and then
        applies your :meth:`.conversion` to give you the sensor value.

        Returns:
            Converted sensor value.
        """


---
./parameters.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from __future__ import annotations

from enum import Enum
from typing import Union, TYPE_CHECKING
import os

from .tools import Matrix as _Matrix, vector as _vector

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = Union[int, float]
    """
    Numbers can be represented as integers or floating point values:

        * Integers (:class:`int <ubuiltins.int>`) are whole numbers
          like ``15`` or ``-123``.
        * Floating point values (:class:`float <ubuiltins.float>`) are decimal
          numbers like ``3.14`` or ``-123.45``.

    If you see :class:`Number` as the argument type, both
    :class:`int <ubuiltins.int>` and :class:`float <ubuiltins.float>` may be used.

    For example, :func:`wait(15) <pybricks.tools.wait>` and
    :func:`wait(15.75) <pybricks.tools.wait>` are both allowed. In most functions,
    however, your input value will be truncated to a whole number anyway. In this
    example, either command makes the program pause for just 15 milliseconds.

    .. note::
        The BOOST Move hub doesn't support floating point numbers due to
        limited system resources. Only integers can be used on that hub.
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Axis:
    """Unit axes of a coordinate system.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """

    X: _Matrix = _vector(1, 0, 0)
    Y: _Matrix = _vector(0, 1, 0)
    Z: _Matrix = _vector(0, 0, 1)


class Color:
    """Light or surface color."""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Hue.
            s (Number, %): Saturation.
            v (Number, %): Brightness value.
        """

        self.h = int(h) % 360
        """
        The hue.
        """

        self.s = max(0, min(int(s), 100))
        """
        The saturation.
        """

        self.v = max(0, min(int(v), 100))
        """
        The brightness value.
        """

    def __iter__(self):
        """Allows unpacking of the Color instance into h, s, and v."""
        return iter((self.h, self.s, self.v))

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool: ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """Port on the programmable brick or hub."""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """Action after the motor stops or reaches its target."""

    COAST: Stop = 0
    """Let the motor move freely."""

    COAST_SMART: Stop = 4
    """
    Let the motor move freely. For the next relative angle maneuver,
    take the last target angle (instead of the current angle) as the new
    starting point. This reduces cumulative errors. This will apply only if the
    current angle is less than twice the configured position tolerance.
    """

    BRAKE: Stop = 1
    """Passively resist small external forces."""

    HOLD: Stop = 2
    """Keep controlling the motor to hold it at the commanded angle."""

    NONE: Stop = 3
    """
    Do not decelerate when approaching the target position. This can be used
    to concatenate multiple motor or drive base maneuvers without stopping. If
    no further commands are given, the motor will proceed to run indefinitely
    at the given speed.
    """


class Direction(_PybricksEnum):
    """Rotational direction for positive speed or angle values."""

    CLOCKWISE: Direction = 0
    """A positive speed value should make the motor move clockwise."""

    COUNTERCLOCKWISE: Direction = 1
    """A positive speed value should make the motor move counterclockwise."""


class Button(_PybricksEnum):
    """Buttons on a hub or remote."""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9
    A: Button = 0
    B: Button = 0
    X: Button = 0
    Y: Button = 0
    LB: Button = 0
    RB: Button = 0
    LJ: Button = 0
    RJ: Button = 0
    P1: Button = 0
    P2: Button = 0
    P3: Button = 0
    P4: Button = 0
    GUIDE: Button = 0
    MENU: Button = 0
    UPLOAD: Button = 0
    VIEW: Button = 0


class Side(_PybricksEnum):
    """Side of a hub or a sensor."""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    """Icons to display on a light matrix.

    Each of the following attributes are matrices. This means you can scale
    icons to adjust the brightness or add icons to make composites.
    """

    UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    """
    DOWN: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨🟨
    | ⬜⬜🟨⬜⬜
    """
    RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | 🟨🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT_UP: _Matrix = ...
    """
    | ⬜⬜🟨🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    | 🟨⬜⬜⬜⬜
    """
    ARROW_RIGHT_DOWN: _Matrix = ...
    """
    | 🟨⬜⬜⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨🟨🟨
    """
    ARROW_LEFT_UP: _Matrix = ...
    """
    | 🟨🟨🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | ⬜⬜⬜⬜🟨
    """
    ARROW_LEFT_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨🟨⬜⬜
    """
    ARROW_UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜🟨⬜🟨
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_DOWN: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    | 🟨⬜🟨⬜🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    HAPPY: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | 🟨⬜⬜⬜🟨
    | ⬜🟨🟨🟨⬜
    """
    SAD: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜⬜⬜🟨
    """
    EYE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW_UP: _Matrix = ...
    """
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW_UP: _Matrix = ...
    """
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    HEART: _Matrix = ...
    """
    | ⬜🟨⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    PAUSE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    EMPTY: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FULL: _Matrix = ...
    """
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    """
    SQUARE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_RIGHT: _Matrix = ...
    """
    | ⬜🟨⬜⬜⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    """
    TRIANGLE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜⬜⬜🟨⬜
    """
    TRIANGLE_UP: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    CIRCLE: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    """
    CLOCKWISE: _Matrix = ...
    """
    | 🟨🟨🟨🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    """
    COUNTERCLOCKWISE: _Matrix = ...
    """
    | ⬜🟨🟨🟨🟨
    | ⬜🟨⬜⬜🟨
    | ⬜🟨⬜⬜🟨
    | 🟨🟨🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    """
    TRUE: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FALSE: _Matrix = ...
    """
    | 🟨⬜⬜⬜🟨
    | ⬜🟨⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜🟨⬜
    | 🟨⬜⬜⬜🟨
    """


---
./pupdevices.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from __future__ import annotations

from typing import TYPE_CHECKING, Collection, Optional, Union, overload

from . import _common
from .parameters import Button, Color, Direction

if TYPE_CHECKING:
    from ._common import (
        MaybeAwaitable,
        MaybeAwaitableBool,
        MaybeAwaitableFloat,
        MaybeAwaitableInt,
        MaybeAwaitableTuple,
    )
    from .parameters import Number, Port


class DCMotor(_common.DCMotor):
    """LEGO® Powered Up motor without rotation sensors."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """


class Motor(_common.Motor):
    """LEGO® Powered Up motor with rotation sensors."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle.
            gears (list):
                List of gears linked to the motor. The gear connected
                to the motor comes first and the gear connected to the output
                comes last.

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth gear connected to the motor and a 36-tooth gear
                connected to the output. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio. The motor direction remains unchanged by this.
            reset_angle (bool):
                Choose ``True`` to reset the rotation sensor value to the
                absolute marker angle (between -180 and 179).
                Choose ``False`` to keep the
                current value, so your program knows where it left off last
                time.
            profile (Number, deg): Precision profile. This is the approximate
                position tolerance in degrees that is acceptable in your
                application. A lower value gives more precise but more erratic
                movement; a higher value gives less precise but smoother
                movement. If no value is given, a suitable profile for this
                motor type will be selected automatically (about 11 degrees).
        """

    def reset_angle(self, angle: Optional[Number] = None) -> None:
        """reset_angle(angle=None)

        Sets the accumulated rotation angle of the motor to a desired value.

        If this motor is also being used by a drive base, its distance and
        angle values will also be affected. You might want to
        use its :meth:`reset <pybricks.robotics.DriveBase.reset>`
        method instead.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
                                 Choose ``None`` to reset it to the absolute
                                 value of the motor.
        """


class Remote:
    """LEGO® Powered Up Bluetooth Remote Control."""

    light = _common.ExternalColorLight()
    buttons = _common.Keypad(
        (
            Button.LEFT_MINUS,
            Button.RIGHT_MINUS,
            Button.LEFT,
            Button.CENTER,
            Button.RIGHT,
            Button.LEFT_PLUS,
            Button.RIGHT_PLUS,
        )
    )
    address: Union[str, None]

    def __init__(self, name: Optional[str] = None, timeout: int = 10000):
        """Remote(name=None, timeout=10000)

        When you instantiate this class, the hub will search for a remote
        and connect automatically.

        The remote must be on and ready for a connection, as indicated by a
        white blinking light.

        Arguments:
            name (str): Bluetooth name of the remote. If no name is given,
                the hub connects to the first remote that it finds.
            timeout (Number, ms): How long to search for the remote.
        """

    @overload
    def name(self, name: str) -> None: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the remote.

        Arguments:
            name (str): New Bluetooth name of the remote. If no name is given,
                this method returns the current name.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the remote from the hub.
        """


class TiltSensor:
    """LEGO® Powered Up Tilt Sensor."""

    def __init__(self, port: Port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def tilt(self) -> MaybeAwaitableTuple[int, int]:
        """tilt() -> Tuple[int, int]: deg

        Measures the tilt relative to the horizontal plane.

        Returns:
            Tuple of pitch and roll angles.
        """


class ColorDistanceSensor(_common.CommonColorSensor):
    """LEGO® Powered Up Color and Distance Sensor."""

    light = _common.ExternalColorLight()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            Distance ranging from 0% (closest) to 100% (farthest).
        """


class PFMotor:
    """Control Power Functions motors with the infrared functionality of the
    :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`."""

    def __init__(
        self,
        sensor: ColorDistanceSensor,
        channel: int,
        color: Color,
        positive_direction: Direction = Direction.CLOCKWISE,
    ):
        """PFMotor(sensor, channel, color, positive_direction=Direction.CLOCKWISE)

        Arguments:
            sensor (ColorDistanceSensor):
                Sensor object.
            channel (int):
                Channel number of the receiver: ``1``, ``2``, ``3``, or ``4``.
            color (Color):
                Color marker on the receiver:
                :class:`Color.BLUE <.parameters.Color>` or
                :class:`Color.RED <.parameters.Color>`
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """

    def dc(self, duty: Number) -> MaybeAwaitable:
        """dc(duty)

        Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (Number, %): The duty cycle (-100.0 to 100).
        """

    def stop(self) -> MaybeAwaitable:
        """stop()

        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction.
        """

    def brake(self) -> MaybeAwaitable:
        """brake()

        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving.
        """


class ColorSensor(_common.AmbientColorSensor):
    """LEGO® SPIKE Color Sensor."""

    lights = _common.LightArray3()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """


class UltrasonicSensor:
    """LEGO® SPIKE Color Sensor."""

    lights = _common.LightArray4()

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            Measured distance. If no valid distance was measured,
            it returns 2000 mm.

        """

    def presence(self) -> MaybeAwaitableBool:
        """presence() -> bool

        Checks for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        Returns:
            ``True`` if ultrasonic sounds are detected, ``False`` if not.
        """


class ForceSensor:
    """LEGO® SPIKE Force Sensor."""

    def __init__(self, port: Port):
        """ForceSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def force(self) -> MaybeAwaitableFloat:
        """force() -> float: N

        Measures the force exerted on the sensor.

        Returns:
            Measured force (up to approximately 10.00 N).
        """

    def distance(self) -> MaybeAwaitableFloat:
        """distance() -> float: mm

        Measures by how much the sensor button has moved.

        Returns:
            Movement up to approximately 8.00 mm.
        """

    def pressed(self, force: Number = 3) -> MaybeAwaitableBool:
        """pressed(force=3) -> bool

        Checks if the sensor button is pressed.

        Arguments:
            force (Number, N): Minimum force to be considered pressed.

        Returns:
            ``True`` if the sensor is pressed, ``False`` if it is not.
        """

    def touched(self) -> MaybeAwaitableBool:
        """touched() -> bool

        Checks if the sensor is touched.

        This is similar to :meth:`pressed`, but it detects slight movements of
        the button even when the measured force is still considered zero.

        Returns:
            ``True`` if the sensor is touched or pressed, ``False``
            if it is not.
        """


class ColorLightMatrix:
    """
    LEGO® SPIKE 3x3 Color Light Matrix.
    """

    def __init__(self, port: Port):
        """ColorLightMatrix(port)

        Arguments:
            port (Port): Port to which the device is connected.

        """
        ...

    def on(self, color: Union[Color, Collection[Color]]) -> MaybeAwaitable:
        """on(colors)

        Turns the lights on.

        Arguments:
            colors (Color or list):
                If a single :class:`.Color` is given, then all 9 lights are set
                to that color. If a list of colors is given, then each light is
                set to that color.
        """
        ...

    def off(self) -> MaybeAwaitable:
        """off()

        Turns all lights off.
        """
        ...


class InfraredSensor:
    """LEGO® Powered Up Infrared Sensor."""

    def __init__(self, port: Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Measures the reflection of a surface using an infrared light.

        Returns:
            Measured reflection, ranging from 0% (no reflection) to
            100% (high reflection).
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            Distance ranging from 0% (closest) to 100% (farthest).
        """

    def count(self) -> MaybeAwaitableInt:
        """count() -> int

        Counts the number of objects that have passed by the sensor.

        Returns:
            Number of objects counted.
        """


class Light:
    """LEGO® Powered Up Light."""

    def __init__(self, port: Port):
        """Light(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def on(self, brightness: Number = 100) -> None:
        """on(brightness=100)

        Turns on the light at the specified brightness.

        Arguments:
            brightness (Number, %):
                Brightness of the light.
        """

    def off(self) -> None:
        """off()

        Turns off the light."""


# HACK: exclude from jedi
if TYPE_CHECKING:
    del Button
    del Color
    del Direction
    del MaybeAwaitable
    del MaybeAwaitableBool
    del MaybeAwaitableFloat
    del MaybeAwaitableInt
    del MaybeAwaitableTuple
    del Number
    del Port


---
./robotics.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Robotics module for the Pybricks API."""

from __future__ import annotations

from typing import Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Stop

if TYPE_CHECKING:
    from ._common import Motor, MaybeAwaitable
    from .parameters import Number


class DriveBase:
    """A robotic vehicle with two powered wheels and an optional support
    wheel or caster.

    By specifying the dimensions of your robot, this class
    makes it easy to drive a given distance in millimeters or turn by a given
    number of degrees.

    **Positive** distances, radii, or drive speeds mean
    driving **forward**. **Negative** means **backward**.

    **Positive** angles and turn rates mean turning **right**.
    **Negative** means **left**. So when viewed from the top,
    positive means clockwise and negative means counterclockwise.

    See the `measuring`_ section for tips to measure and adjust the diameter
    and axle track values.
    """

    distance_control = _common.Control()
    """The traveled distance and drive speed are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``distance_control`` attribute has the same
    functionality, but the settings apply to every millimeter driven by the
    drive base, instead of degrees turned by one motor."""

    heading_control = _common.Control()
    """The robot turn angle and turn rate are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``heading_control`` attribute has the same
    functionality, but the settings apply to every degree of rotation of the
    whole drive base (viewed from the top) instead of degrees turned by one
    motor."""

    def __init__(
        self,
        left_motor: Motor,
        right_motor: Motor,
        wheel_diameter: Number,
        axle_track: Number,
    ):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                The motor that drives the left wheel.
            right_motor (Motor):
                The motor that drives the right wheel.
            wheel_diameter (Number, mm): Diameter of the wheels.
            axle_track (Number, mm): Distance between the points where
                both wheels touch the ground.
        """

    def drive(self, speed: Number, turn_rate: Number) -> None:
        """drive(speed, turn_rate)

        Starts driving at the specified speed and turn rate. Both values are
        measured at the center point between the wheels of the robot.

        Arguments:
            speed (Number, mm/s): Speed of the robot.
            turn_rate (Number, deg/s): Turn rate of the robot.
        """

    def stop(self) -> None:
        """stop()

        Stops the robot by letting the motors spin freely."""

    def brake(self) -> None:
        """brake()

        Stops the robot by passively braking the motors.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Gets the estimated driven distance.

        Returns:
            Driven distance since last reset.
        """

    def angle(self) -> float:
        """angle() -> float: deg

        Gets the estimated rotation angle of the drive base.

        Returns:
            Accumulated angle since last reset.
        """

    def state(self) -> Tuple[int, int, int, int]:
        """state() -> Tuple[int, int, int, int]

        Gets the state of the robot.

        Returns:
            Tuple of distance, drive speed, angle, and turn rate of the robot.
        """

    def reset(self, distance: Number = 0, angle: Number = 0) -> None:
        """reset(distance=0, angle=0)

        Resets the estimated driven distance and heading angle.

        This also calls :meth:`.stop` to stop ongoing movements.
        If your robot is controlled with :meth:`.use_gyro` set to ``True``,
        calling this method will `also` set the gyro to the given angle.

        Arguments:
            distance (Number, mm): Speed of the robot.
            angle (Number, deg): Heading angle of the robot.
        """

    @overload
    def settings(
        self,
        straight_speed: Optional[Number] = None,
        straight_acceleration: Optional[Number] = None,
        turn_rate: Optional[Number] = None,
        turn_acceleration: Optional[Number] = None,
    ) -> None: ...

    @overload
    def settings(self) -> Tuple[int, int, int, int]: ...

    def settings(self, *args):
        """
        settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> Tuple[int, int, int, int]

        Configures the drive base speed and acceleration.

        If you give no arguments, this returns the current values as a tuple.

        The initial values are automatically configured based on your wheel
        diameter and axle track. They are selected such that your robot
        drives at about 40% of its maximum speed.

        The speed values given here do not apply to the :meth:`.drive` method,
        since you provide your own speed values as arguments in that method.

        Arguments:
            straight_speed (Number, mm/s): Straight-line speed of the robot.
            straight_acceleration (Number, mm/s²): Straight-line
                acceleration and deceleration of the robot. Provide a tuple with
                two values to set acceleration and deceleration separately.
            turn_rate (Number, deg/s): Turn rate of the robot.
            turn_acceleration (Number, deg/s²): Angular acceleration and
                deceleration of the robot. Provide a tuple with
                two values to set acceleration and deceleration separately.
        """

    def straight(
        self, distance: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """straight(distance, then=Stop.HOLD, wait=True)

        Drives straight for a given distance and then stops.

        Arguments:
            distance (Number, mm): Distance to travel
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """

    def turn(
        self, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """turn(angle, then=Stop.HOLD, wait=True)

        Turns in place by a given angle and then stops.

        Arguments:
            angle (Number, deg): Angle of the turn.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """

    def arc(
        self,
        radius: Number,
        angle: Number = None,
        distance: Number = None,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """arc(radius, angle=None, distance=None, then=Stop.HOLD, wait=True)

        Drives an arc (a partial circle) with a given radius. You can specify
        how far to drive using either an angle or a distance.

        With a positive radius, the robot drives along a circle to its right.
        With a negative radius, the robot drives along a circle to its left.

        You can specify how far to travel along that circle as an angle
        (degrees) or distance (mm). A positive value means driving forward
        along the circle. Negative means driving in reverse.

        Arguments:
            radius (Number, mm): Radius of the circle.
            angle (Number, deg): Angle to drive along the circle.
            distance (Number, mm): Distance to drive along the circle,
                                   measured at the center of the robot.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        Raises:
            ValueError:
                You must specify ``angle`` or ``distance``, but not both. The
                radius cannot be zero. Use :meth:`.turn` for in-place turns.
        """

    def curve(
        self, radius: Number, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """curve(radius, angle, then=Stop.HOLD, wait=True)

        Drives an arc along a circle of a given radius, by a given angle.

        Arguments:
            radius (Number, mm): Radius of the circle.
            angle (Number, deg): Angle along the circle.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """

    def done(self) -> bool:
        """done() -> bool

        Checks if an ongoing command or maneuver is done.

        Returns:
            ``True`` if the command is done, ``False`` if not.
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Checks if the drive base is currently stalled.

        It is stalled when it cannot reach the target speed or position, even
        with the maximum actuation signal.

        Returns:
            ``True`` if the drive base is stalled, ``False`` if not.
        """

    def use_gyro(self, use_gyro: bool) -> None:
        """use_gyro(use_gyro)

        Choose ``True`` to use the gyro sensor for turning and driving
        straight. Choose ``False`` to rely only on the motor's built-in
        rotation sensors.

        This method will automatically call :meth:`.stop` to stop ongoing
        movements.

        Arguments:
            use_gyro (bool): ``True`` to enable, ``False`` to disable.
        """


class Car:
    """A vehicle with one steering motor, and one or more motors for driving.

    When you use this class, the steering motor will automatically find the
    center position. This also determines which angle corresponds to 100%
    steering.
    """

    def __init__(
        self,
        steer_motor: Motor,
        drive_motors: Motor | Tuple[Motor, ...],
        torque_limit: Number = 100,
    ):
        """Car(steer_motor, drive_motors, torque_limit=100)

        Arguments:
            steer_motor (Motor):
                The motor that steers the front wheels.
            drive_motors (Motor): The motor that drives the wheels. Use a tuple
                for multiple motors.
            torque_limit (Number, %): The maximum torque limit used to find the
                endpoints for the steering mechanism, as a percentage of the
                maximum torque of the steering motor.
        """

    def steer(self, percentage: Number) -> None:
        """steer(percentage)

        Steers the front wheels by a given amount. For 100% steering, it
        steers right by the angle that was determined on initialization.
        For -100% steering, it steers left and 0% means straight.

        Arguments:
            steering (Number, %): Amount to steer the front wheels.
        """

    def drive_power(self, power: Number) -> None:
        """drive_power(power)

        Drives the car at a given power level. Positive values drive forward,
        negative values drive backward.

        The ``power`` value is used to set the motor voltage as a percentage of
        the battery voltage. Below 10%, the car will coast the wheels in order
        to roll out smoothly instead of braking abruptly.

        This command is useful for remote control applications where you want
        instant response to button presses or joystick movements.

        Arguments:
            speed (Number, %): Speed of the car.
        """

    def drive_speed(self, speed: Number) -> None:
        """drive_speed(speed)

        Drives the car at a given motor speed. Positive values drive forward,
        negative values drive backward.

        This command is useful for more precise driving with gentle
        acceleration and deceleration. This automatically increases the power
        to maintain speed as you drive across obstacles.

        Arguments:
            speed (Number, deg/s): Angular velocity of the drive motors.
        """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Motor
    del Number
    del MaybeAwaitable
    del Stop


---
./tools.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Common tools for timing, data logging, and linear algebra."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Sequence, Tuple, overload, Coroutine

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


def wait(time: Number) -> MaybeAwaitable:
    """wait(time)

    Pauses the user program for a specified amount of time.

    Arguments:
        time (Number, ms): How long to wait.
    """


class StopWatch:
    """A stopwatch to measure time intervals. Similar to the stopwatch
    feature on your phone."""

    def __init__(self): ...

    def time(self) -> int:
        """time() -> int: ms

        Gets the current time of the stopwatch.

        Returns:
            Elapsed time.
        """

    def pause(self) -> None:
        """pause()

        Pauses the stopwatch."""

    def resume(self) -> None:
        """resume()

        Resumes the stopwatch."""

    def reset(self) -> None:
        """reset()

        Resets the stopwatch time to 0.

        The run state is unaffected:

        * If it was paused, it stays paused (but now at 0).
        * If it was running, it stays running (but starting again from 0).
        """


class DataLog:
    """Create a file and log data."""

    def __init__(
        self,
        *headers: str,
        name: str = "log",
        timestamp: bool = True,
        extension: str = "csv",
        append: bool = False,
    ):
        """DataLog(*headers, name='log', timestamp=True, extension='csv', append=False)

        Arguments:
            headers (str, str, ...): Column headers. These are the
                names of the data columns. For example, choose ``'time'`` and
                ``'angle'``.
            name (str): Name of the file.
            timestamp (bool): Choose ``True`` to add the date and time to the
                file name. This way, your file has a unique name.
                Choose ``False`` to omit the timestamp.
            extension (str): File extension.
            append (bool): Choose ``True`` to reopen an existing data log file
                and append data to it. Choose ``False`` to clear existing
                data. If the file does not exist yet, an empty file will be
                created either way.
        """

    def log(self, *values: Any) -> None:
        """log(value1, value2, ...)

        Saves one or more values on a new line in the file.

        Arguments:
            values (object, object, ...): One or more objects or values.
        """


class Matrix:
    """Mathematical representation of a matrix. It supports
    addition (``A + B``), subtraction (``A - B``),
    and matrix multiplication (``A * B``) for matrices of compatible size.

    It also supports scalar multiplication (``c * A`` or ``A * c``)
    and scalar division (``A / c``).

    A :class:`.Matrix` object is immutable."""

    def __add__(self, other) -> Matrix: ...

    def __iadd__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __isub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __rmul__(self, other) -> Matrix: ...

    def __imul__(self, other) -> Matrix: ...

    def __truediv__(self, other) -> Matrix: ...

    def __itruediv__(self, other) -> Matrix: ...

    def __floordiv__(self, other) -> Matrix: ...

    def __ifloordiv__(self, other) -> Matrix: ...

    def __init__(self, rows: Sequence[Sequence[float]]):
        """Matrix(rows)

        Arguments:
            rows (list): List of rows. Each row is itself a list of numbers.

        """

    @property
    def T(self) -> Matrix:  # noqa: N802
        """Returns a new :class:`.Matrix` that is the transpose of the
        original."""

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns a tuple (``m``, ``n``),
        where ``m`` is the number of rows and ``n`` is the number of columns.
        """


@overload
def vector(x: float, y: float) -> Matrix:
    """
    Convenience function to create a :class:`.Matrix` with the shape (``2``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.

    Returns:
        A matrix with the shape of a column vector.
    """


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    """
    Convenience function to create a :class:`.Matrix` with the shape (``3``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector.

    Returns:
        A matrix with the shape of a column vector.
    """


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    Convenience function to create a :class:`.Matrix` with the
    shape (``2``, ``1``) or (``3``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector (optional).

    Returns:
        A matrix with the shape of a column vector.
    """


def cross(a: Matrix, b: Matrix) -> Matrix:
    """
    cross(a, b) -> Matrix

    Gets the cross product ``a`` × ``b`` of two vectors.

    Arguments:
        a (Matrix): A three-dimensional vector.
        b (Matrix): A three-dimensional vector.

    Returns:
        The cross product, also a three-dimensional vector.
    """


def read_input_byte(last: bool = False, chr: bool = False) -> Optional[int | str]:
    """
    read_input_byte() -> int | str | None

    Reads one byte from standard input without blocking and removes it from the
    input buffer.

    Arguments:
        last (bool): Choose ``True`` to read the last (most recent) byte in the buffer and discard the rest.
                     Choose ``False`` to read only the first (oldest) byte.
        chr (bool): Choose ``True`` to convert the result to a one-character string.

    Returns:
        The byte that was read, as a numeric value (``0`` to ``255``) or
        string (e.g. ``"B"``). Returns ``None`` if no data is available. If
        ``chr=True``, it also return ``None`` if the byte that was read is not
        printable as a character.
    """


def hub_menu(*symbols: int | str) -> int | str:
    """
    hub_menu(symbol1, symbol2, ...) -> int | str

    Shows a menu on the hub display and waits for the user to select an item
    using the buttons. Can be used in your own menu-program that lets you
    choose which of your other programs to run.

    Note that this is just a convenience function that combines the display,
    buttons, and waits to make a simple menu. This means that it can be used
    anywhere in a program, not just at the start.

    Arguments:
        symbol1 (int or str): The first symbol to show in the menu.
        symbol2 (int or str): The second symbol, and so on...

    Returns:
        The selected symbol.
    """


def multitask(*coroutines: Coroutine, race=False) -> MaybeAwaitableTuple:
    """
    multitask(coroutine1, coroutine2, ...) -> Tuple

    Runs multiple coroutines concurrently. This creates a new coroutine that
    can be used like any other, including in another ``multitask`` statement.

    Arguments:
        coroutines (coroutine, coroutine, ...): One or more coroutines to run
            in parallel.
        race (bool): Choose ``False`` to wait for all coroutines to finish.
            Choose ``True`` to wait for one coroutine to finish and then
            cancel the others, as if it's a "race".

    Returns:
        Tuple of the return values of each coroutine. Unfinished coroutines
        will have ``None`` as their return value.
    """


def run_task(coroutine: Coroutine) -> Optional[bool]:
    """
    run_task(coroutine) -> bool | None

    Runs a coroutine from start to finish while blocking the rest of the
    program. This is used primarily to run the main coroutine of a program.

    Calls to this function are not allowed to be nested.

    Arguments:
        coroutine (coroutine): The main coroutine to run.

    Returns:
        If no ``coroutine`` is given, this function returns whether the
        run loop is currently active (``True``) or not (``False``).
    """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Number
    del MaybeAwaitable
    del MaybeAwaitableTuple


---
./ev3dev/_speaker.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

from typing import Iterable, Union, Optional

from ..media.ev3dev import SoundFile


class Speaker:
    """Plays beeps and sounds using a speaker."""

    def beep(self, frequency: int = 500, duration: int = 100) -> None:
        """beep(frequency=500, duration=100)

        Play a beep/tone.

        Arguments:
            frequency (Number, Hz):
                Frequency of the beep. Frequencies below 100 Hz are treated as
                100 Hz.
            duration (Number, ms):
                Duration of the beep. If the duration is less than 0, then the
                method returns immediately and the frequency play continues to
                play indefinitely.
        """

    def play_notes(self, notes: Iterable[str], tempo: int = 120) -> None:
        """play_notes(notes, tempo=120)

        Plays a sequence of musical notes. For example:
        ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Each note is a string with the following format:

            - The first character is the name of the note, ``A`` to ``G``
              or ``R`` for a rest.
            - Note names can also include an accidental ``#`` (sharp) or
              ``b`` (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not
              allowed.
            - The note name is followed by the octave number ``2``
              to ``8``. For example ``C4`` is middle C. The octave changes
              to the next number at the note C, for example, ``B3`` is the
              note below middle C (``C4``).
            - The octave is followed by ``/`` and a number that indicates
              the size of the note. For example ``/4`` is a quarter note,
              ``/8`` is an eighth note and so on.
            - This can optionally followed by a ``.`` to make a dotted
              note. Dotted notes are 1-1/2 times as long as notes without a
              dot.
            - The note can optionally end with a ``_`` which is a tie or a
              slur. This causes there to be no pause between this note and
              the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played.
            tempo (int):
                Beats per minute. A quarter note is one beat.
        """

    def play_file(self, file_name: Union[SoundFile, str]) -> None:
        """play_file(file_name)

        Plays a sound file.

        Arguments:
            file (str):
                Path to the sound file, including the file extension.
        """

    def say(self, text: str) -> None:
        """say(text)

        Says a given text string.

        You can configure the language and voice of the text using
        :meth:`.set_speech_options`.

        Arguments:
            text (str): What to say.
        """

    def set_speech_options(
        self,
        language: Optional[str] = None,
        voice: Optional[str] = None,
        speed: Optional[int] = None,
        pitch: Optional[int] = None,
    ):
        """set_speech_options(language, voice, speed, pitch)

        Configures speech settings used by the :meth:`.say` method.

        Any option that is set to ``None`` will not be changed. If an option
        is set to an invalid value :meth:`.say` will use the default value
        instead.

        Arguments:
            language (str):
                Language of the text. For example, you can choose ``'en'``
                (English) or ``'de'`` (German). [#espeak_lang]_
            voice (str):
                The voice to use. For example, you can choose ``'f1'`` (female
                voice variant 1) or ``'m3'`` (male voice variant 3).
                [#espeak_lang]_
            speed (int):
                Number of words per minute.
            pitch (int):
                Pitch (0 to 99). Higher numbers make the voice higher pitched
                and lower numbers make the voice lower pitched.
        """

    def set_volume(self, volume: int, which: str = "_all_") -> None:
        """set_volume(volume, which="_all_")

        Sets the speaker volume.

        Arguments:
            volume (Number, %):
                Volume of the speaker.
            which (str):
                Which volume to set. ``'Beep'`` sets the volume for
                `beep` and `play_notes`. ``'PCM'`` sets the
                volume for :meth:`.play_file` and :meth:`.say`. ``'_all_'``
                sets both at the same time.
        """


---
./media/__init__.py
---


---
./media/ev3dev.py
---
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Images and Sounds for Pybricks on ev3dev."""

from __future__ import annotations

from typing import Union, Literal, overload, Optional, Any

from ..parameters import Color


class Image:
    """Object representing a graphics image. This can either be an in-memory
    copy of an image or the image displayed on a screen."""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    @overload
    def __init__(self, /, source: Union[Image, ImageFile, str]):
        ...

    @overload
    def __init__(
        self, /, source: Image, sub: Literal[False], x1: int, y1: int, x2: int, y2: int
    ):
        ...

    def __init__(self, *args):
        """Image(source, sub=False)


        Arguments:
            source (str or Image):
                The source of the image.

                If ``source`` is a string, then the image will be loaded from
                the file path given by the string. Only ``.png`` files are
                supported. As a special case, if the string is ``_screen_``,
                the image will be configured to draw directly on the screen.

                If an :class:`Image` is given, the new object will contain a
                copy of the ``source`` image object.

            sub (bool):
                If ``sub`` is ``True``, then the image object will act as a
                sub-image of the ``source`` image (this only works if the type
                of ``source`` is :class:`Image` and not when it is a ``str``).

                Additional keyword arguments ``x1``, ``y1``, ``x2``, ``y2`` are
                needed when ``sub=True``. These specify the top-left and
                bottom-right coordinates in the ``source`` image that will be
                used as the bounds for the sub-image.
        """

    @property
    def width(self) -> int:
        """Gets the width of |this image| in pixels."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of |this image| in pixels."""
        return 0

    def clear(self) -> None:
        """clear()

        Clears |this image|. All pixels on |this image| will be set to
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.
        """

    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        """draw_pixel(x, y, color=Color.BLACK)

        Draws a single pixel on |this image|.

        Arguments:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            color (Color): The color of the pixel.
        """

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_line(x1, y1, x2, y2, width=1, color=Color.BLACK)

        Draws a line on |this image|.

        Arguments:
            x1 (int): The x coordinate of the starting point of the line.
            y1 (int): The y coordinate of the starting point of the line.
            x2 (int): The x coordinate of the ending point of the line.
            y2 (int): The y coordinate of the ending point of the line.
            width (int): The width of the line in pixels.
            color (Color): The color of the line.
        """

    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_box(x1, y1, x2, y2, r=0, fill=False, color=Color.BLACK)

        Draws a box on |this image|.

        Arguments:
            x1 (int): The x coordinate of the left side of the box.
            y1 (int): The y coordinate of the top of the box.
            x2 (int): The x coordinate of the right side of the box.
            y2 (int): The y coordinate of the bottom of the box.
            r (int): The radius of the corners of the box.
            fill (bool): If ``True``, the box will be filled with ``color``,
                otherwise only the outline of the box will be drawn.
            color (Color): The color of the box.
        """

    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None:
        """draw_circle(x, y, r, fill=False, color=Color.BLACK)

        Draws a circle on |this image|.

        Arguments:
            x (int): The x coordinate of the center of the circle.
            y (int): The y coordinate of the center of the circle.
            r (int): The radius of the circle.
            fill (bool): If ``True``, the circle will be filled with
                ``color``, otherwise only the circumference will be drawn.
            color (Color): The color of the circle.
        """

    def draw_image(
        self,
        x: int,
        y: int,
        source: Union[Image, ImageFile, str],
        transparent: Optional[Color] = None,
    ) -> None:
        """draw_image(x, y, source, transparent=None)

        Draws the ``source`` image on |this image|.

        Arguments:
            x (int):
                The x-axis value where the left side of the image will start.
            y (int):
                The y-axis value where the top of the image will start.
            source (Image or str):
                The source :class:`Image <pybricks.media.ev3dev.Image>`. If
                the argument is a string, then the ``source`` image is loaded
                from file.
            transparent (Color):
                The color of ``image`` to treat as transparent or ``None`` for
                no transparency.
        """

    def load_image(self, source: Union[Image, ImageFile, str]) -> None:
        """load_image(source)

        Clears this image, then draws the ``source`` image centered in
        |this image|.

        Arguments:
            source (Image or str):
                The source :class:`Image <pybricks.media.ev3dev.Image>`. If
                the argument is a string, then the ``source`` image is loaded
                from file.
        """

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Optional[Color] = None,
    ) -> None:
        """draw_text(x, y, text, text_color=Color.BLACK, background_color=None)

        Draws text on |this image|.

        The most recent font set using :meth:`.set_font` will be used or
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` if no font
        has been set yet.

        Arguments:
            x (int):
                The x-axis value where the left side of the text will start.
            y (int):
                The y-axis value where the top of the text will start.
            text (str):
                The text to draw.
            text_color (Color):
                The color used for drawing the text.
            background_color (Color):
                The color used to fill the rectangle behind the text or
                ``None`` for transparent background.
        """

    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        """print(*args, sep=" ", end="\\n")

        Prints a line of text on |this image|.

        This method works like the builtin ``print()`` function, but it writes
        on |this image| instead.

        You can set the font using :meth:`.set_font`. If no font has been set,
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` will be
        used. The text is always printed used black text with a white
        background.

        Unlike the builtin ``print()``, the text does not wrap if it is too
        wide to fit on |this image|. It just gets cut off. But if the text
        would go off of the bottom of |this image|, the entire image is
        scrolled up and the text is printed in the new blank area at the
        bottom of |this image|.

        Arguments:
            args (Any): Zero or more objects to print.
            sep (str): Separator that will be placed between each object that
                is printed.
            end (str): End of line that will be printed after the last object.
        """

    def set_font(self, font: Font) -> None:
        """set_font(font)

        Sets the font used for writing on |this image|.

        The font is used for both :meth:`.draw_text` and :meth:`.print`.

        Arguments:
            font (Font):
                The font to use.
        """

    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image:
        """empty(width=178, height=128) -> Image

        Creates a new empty :class:`Image` object.

        Arguments:
            width (int):
                The width of the image in pixels.
            height (int):
                The height of the image in pixels.

        Returns:
            A new image with all pixels set
            to :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.

        Raises:
            TypeError:
                If ``width`` or ``height`` is not a number.
            ValueError:
                If ``width`` or ``height`` is less than 1.
            RuntimeError:
                If there was a problem allocating a new image.
        """

    def save(self, filename: str) -> None:
        """save(filename)

        Saves |this image| as a ``.png`` file.

        Arguments:
            filename (str):
                The path to the file to be saved.

        Raises:
            TypeError:
                ``filename`` is not a string.
            OSError:
                There was a problem saving the file.
        """


class Font:
    """Object that represents a font for writing text."""

    DEFAULT: Font = None  # assigned later since we can't use Font() here
    """The default font."""

    def __init__(
        self,
        family: Optional[str] = None,
        size: int = 12,
        bold: bool = False,
        monospace: bool = False,
        lang: Optional[str] = None,
        script: Optional[str] = None,
    ):
        """Font(family=None, size=12, bold=False, monospace=False, lang=None, script=None)

        The font object will be a font that is the "best" match based on the
        parameters given and available fonts installed.

        Arguments:
            family (str):
                The preferred font family or ``None`` to use the default value.
            size (int):
                The preferred font size. Most fonts have sizes between 6 and 24.
                This is the "point" size and not the same as :attr:`height`.
            bold (bool):
                When ``True``, prefer bold fonts.
            monospace (bool):
                When ``True`` prefer monospaced fonts. This is useful for
                aligning multiple rows of text.
            lang (str):
                A language code, such as ``'en'`` or ``'zh-cn'`` or ``None`` to
                use the default language. [#font_lang]_
            script (str):
                A unicode script identifier such as ``'Runr'`` or ``None``.
        """

    @property
    def family(self) -> str:
        """Gets the family name of the font."""
        return "Lucida"

    @property
    def style(self) -> str:
        """style -> str

        Gets a string describing the font style.

        Can be "Regular" or "Bold".
        """
        return "Regular"

    @property
    def width(self) -> int:
        """Gets the width of the widest character of the font."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of the font."""
        return 0

    def text_width(self, text: str) -> int:
        """text_width(text)

        Gets the width of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The width in pixels.
        """
        return 0

    def text_height(self, text: str) -> int:
        """text_height(text)

        Gets the height of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The height in pixels.
        """
        return 0


Font.DEFAULT = Font("Lucida", 12)


class SoundFile:
    """Paths to standard EV3 sounds."""

    _BASE_PATH: str = "/usr/share/sounds/ev3dev/"
    SHOUTING: str = _BASE_PATH + "expressions/shouting.wav"
    CHEERING: str = _BASE_PATH + "expressions/cheering.wav"
    CRYING: str = _BASE_PATH + "expressions/crying.wav"
    OUCH: str = _BASE_PATH + "expressions/ouch.wav"
    LAUGHING_2: str = _BASE_PATH + "expressions/laughing_2.wav"
    SNEEZING: str = _BASE_PATH + "expressions/sneezing.wav"
    SMACK: str = _BASE_PATH + "expressions/smack.wav"
    BOING: str = _BASE_PATH + "expressions/boing.wav"
    BOO: str = _BASE_PATH + "expressions/boo.wav"
    UH_OH: str = _BASE_PATH + "expressions/uh-oh.wav"
    SNORING: str = _BASE_PATH + "expressions/snoring.wav"
    KUNG_FU: str = _BASE_PATH + "expressions/kung_fu.wav"
    FANFARE: str = _BASE_PATH + "expressions/fanfare.wav"
    CRUNCHING: str = _BASE_PATH + "expressions/crunching.wav"
    MAGIC_WAND: str = _BASE_PATH + "expressions/magic_wand.wav"
    LAUGHING_1: str = _BASE_PATH + "expressions/laughing_1.wav"
    LEFT: str = _BASE_PATH + "information/left.wav"
    BACKWARDS: str = _BASE_PATH + "information/backwards.wav"
    RIGHT: str = _BASE_PATH + "information/right.wav"
    OBJECT: str = _BASE_PATH + "information/object.wav"
    COLOR: str = _BASE_PATH + "information/color.wav"
    FLASHING: str = _BASE_PATH + "information/flashing.wav"
    ERROR: str = _BASE_PATH + "information/error.wav"
    ERROR_ALARM: str = _BASE_PATH + "information/error_alarm.wav"
    DOWN: str = _BASE_PATH + "information/down.wav"
    FORWARD: str = _BASE_PATH + "information/forward.wav"
    ACTIVATE: str = _BASE_PATH + "information/activate.wav"
    SEARCHING: str = _BASE_PATH + "information/searching.wav"
    TOUCH: str = _BASE_PATH + "information/touch.wav"
    UP: str = _BASE_PATH + "information/up.wav"
    ANALYZE: str = _BASE_PATH + "information/analyze.wav"
    STOP: str = _BASE_PATH + "information/stop.wav"
    DETECTED: str = _BASE_PATH + "information/detected.wav"
    TURN: str = _BASE_PATH + "information/turn.wav"
    START: str = _BASE_PATH + "information/start.wav"
    MORNING: str = _BASE_PATH + "communication/morning.wav"
    EV3: str = _BASE_PATH + "communication/ev3.wav"
    GO: str = _BASE_PATH + "communication/go.wav"
    GOOD_JOB: str = _BASE_PATH + "communication/good_job.wav"
    OKEY_DOKEY: str = _BASE_PATH + "communication/okey-dokey.wav"
    GOOD: str = _BASE_PATH + "communication/good.wav"
    NO: str = _BASE_PATH + "communication/no.wav"
    THANK_YOU: str = _BASE_PATH + "communication/thank_you.wav"
    YES: str = _BASE_PATH + "communication/yes.wav"
    GAME_OVER: str = _BASE_PATH + "communication/game_over.wav"
    OKAY: str = _BASE_PATH + "communication/okay.wav"
    SORRY: str = _BASE_PATH + "communication/sorry.wav"
    BRAVO: str = _BASE_PATH + "communication/bravo.wav"
    GOODBYE: str = _BASE_PATH + "communication/goodbye.wav"
    HI: str = _BASE_PATH + "communication/hi.wav"
    HELLO: str = _BASE_PATH + "communication/hello.wav"
    MINDSTORMS: str = _BASE_PATH + "communication/mindstorms.wav"
    LEGO: str = _BASE_PATH + "communication/lego.wav"
    FANTASTIC: str = _BASE_PATH + "communication/fantastic.wav"
    SPEED_IDLE: str = _BASE_PATH + "movements/speed_idle.wav"
    SPEED_DOWN: str = _BASE_PATH + "movements/speed_down.wav"
    SPEED_UP: str = _BASE_PATH + "movements/speed_up.wav"
    BROWN: str = _BASE_PATH + "colors/brown.wav"
    GREEN: str = _BASE_PATH + "colors/green.wav"
    BLACK: str = _BASE_PATH + "colors/black.wav"
    WHITE: str = _BASE_PATH + "colors/white.wav"
    RED: str = _BASE_PATH + "colors/red.wav"
    BLUE: str = _BASE_PATH + "colors/blue.wav"
    YELLOW: str = _BASE_PATH + "colors/yellow.wav"
    TICK_TACK: str = _BASE_PATH + "mechanical/tick_tack.wav"
    HORN_1: str = _BASE_PATH + "mechanical/horn_1.wav"
    BACKING_ALERT: str = _BASE_PATH + "mechanical/backing_alert.wav"
    MOTOR_IDLE: str = _BASE_PATH + "mechanical/motor_idle.wav"
    AIR_RELEASE: str = _BASE_PATH + "mechanical/air_release.wav"
    AIRBRAKE: str = _BASE_PATH + "mechanical/airbrake.wav"
    RATCHET: str = _BASE_PATH + "mechanical/ratchet.wav"
    MOTOR_STOP: str = _BASE_PATH + "mechanical/motor_stop.wav"
    HORN_2: str = _BASE_PATH + "mechanical/horn_2.wav"
    LASER: str = _BASE_PATH + "mechanical/laser.wav"
    SONAR: str = _BASE_PATH + "mechanical/sonar.wav"
    MOTOR_START: str = _BASE_PATH + "mechanical/motor_start.wav"
    INSECT_BUZZ_2: str = _BASE_PATH + "animals/insect_buzz_2.wav"
    ELEPHANT_CALL: str = _BASE_PATH + "animals/elephant_call.wav"
    SNAKE_HISS: str = _BASE_PATH + "animals/snake_hiss.wav"
    DOG_BARK_2: str = _BASE_PATH + "animals/dog_bark_2.wav"
    DOG_WHINE: str = _BASE_PATH + "animals/dog_whine.wav"
    INSECT_BUZZ_1: str = _BASE_PATH + "animals/insect_buzz_1.wav"
    DOG_SNIFF: str = _BASE_PATH + "animals/dog_sniff.wav"
    T_REX_ROAR: str = _BASE_PATH + "animals/t-rex_roar.wav"
    INSECT_CHIRP: str = _BASE_PATH + "animals/insect_chirp.wav"
    DOG_GROWL: str = _BASE_PATH + "animals/dog_growl.wav"
    SNAKE_RATTLE: str = _BASE_PATH + "animals/snake_rattle.wav"
    DOG_BARK_1: str = _BASE_PATH + "animals/dog_bark_1.wav"
    CAT_PURR: str = _BASE_PATH + "animals/cat_purr.wav"
    EIGHT: str = _BASE_PATH + "numbers/eight.wav"
    SEVEN: str = _BASE_PATH + "numbers/seven.wav"
    SIX: str = _BASE_PATH + "numbers/six.wav"
    FOUR: str = _BASE_PATH + "numbers/four.wav"
    TEN: str = _BASE_PATH + "numbers/ten.wav"
    ONE: str = _BASE_PATH + "numbers/one.wav"
    TWO: str = _BASE_PATH + "numbers/two.wav"
    THREE: str = _BASE_PATH + "numbers/three.wav"
    ZERO: str = _BASE_PATH + "numbers/zero.wav"
    FIVE: str = _BASE_PATH + "numbers/five.wav"
    NINE: str = _BASE_PATH + "numbers/nine.wav"
    READY: str = _BASE_PATH + "system/ready.wav"
    CONFIRM: str = _BASE_PATH + "system/confirm.wav"
    GENERAL_ALERT: str = _BASE_PATH + "system/general_alert.wav"
    CLICK: str = _BASE_PATH + "system/click.wav"
    OVERPOWER: str = _BASE_PATH + "system/overpower.wav"


class ImageFile:
    """Paths to standard EV3 images."""

    _BASE_PATH: str = "/usr/share/images/ev3dev/mono/"
    RIGHT: str = _BASE_PATH + "information/right.png"
    FORWARD: str = _BASE_PATH + "information/forward.png"
    ACCEPT: str = _BASE_PATH + "information/accept.png"
    QUESTION_MARK: str = _BASE_PATH + "information/question_mark.png"
    STOP_1: str = _BASE_PATH + "information/stop_1.png"
    LEFT: str = _BASE_PATH + "information/left.png"
    DECLINE: str = _BASE_PATH + "information/decline.png"
    THUMBS_DOWN: str = _BASE_PATH + "information/thumbs_down.png"
    BACKWARD: str = _BASE_PATH + "information/backward.png"
    NO_GO: str = _BASE_PATH + "information/no_go.png"
    WARNING: str = _BASE_PATH + "information/warning.png"
    STOP_2: str = _BASE_PATH + "information/stop_2.png"
    THUMBS_UP: str = _BASE_PATH + "information/thumbs_up.png"
    EV3: str = _BASE_PATH + "lego/ev3.png"
    EV3_ICON: str = _BASE_PATH + "lego/ev3_icon.png"
    TARGET: str = _BASE_PATH + "objects/target.png"
    BOTTOM_RIGHT: str = _BASE_PATH + "eyes/bottom_right.png"
    BOTTOM_LEFT: str = _BASE_PATH + "eyes/bottom_left.png"
    EVIL: str = _BASE_PATH + "eyes/evil.png"
    CRAZY_2: str = _BASE_PATH + "eyes/crazy_2.png"
    KNOCKED_OUT: str = _BASE_PATH + "eyes/knocked_out.png"
    PINCHED_RIGHT: str = _BASE_PATH + "eyes/pinched_right.png"
    WINKING: str = _BASE_PATH + "eyes/winking.png"
    DIZZY: str = _BASE_PATH + "eyes/dizzy.png"
    DOWN: str = _BASE_PATH + "eyes/down.png"
    TIRED_MIDDLE: str = _BASE_PATH + "eyes/tired_middle.png"
    MIDDLE_RIGHT: str = _BASE_PATH + "eyes/middle_right.png"
    SLEEPING: str = _BASE_PATH + "eyes/sleeping.png"
    MIDDLE_LEFT: str = _BASE_PATH + "eyes/middle_left.png"
    TIRED_RIGHT: str = _BASE_PATH + "eyes/tired_right.png"
    PINCHED_LEFT: str = _BASE_PATH + "eyes/pinched_left.png"
    PINCHED_MIDDLE: str = _BASE_PATH + "eyes/pinched_middle.png"
    CRAZY_1: str = _BASE_PATH + "eyes/crazy_1.png"
    NEUTRAL: str = _BASE_PATH + "eyes/neutral.png"
    AWAKE: str = _BASE_PATH + "eyes/awake.png"
    UP: str = _BASE_PATH + "eyes/up.png"
    TIRED_LEFT: str = _BASE_PATH + "eyes/tired_left.png"
    ANGRY: str = _BASE_PATH + "eyes/angry.png"


---
```
