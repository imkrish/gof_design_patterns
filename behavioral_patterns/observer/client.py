from behavioral_patterns.observer.clock_timer import ClockTimer
from behavioral_patterns.observer.digital_clock import DigitalClock
from behavioral_patterns.observer.analog_clock import AnalogClock
import threading


if __name__ == '__main__':

    subject = ClockTimer()
    digital_clock = DigitalClock(subject)
    analog_clock = AnalogClock(subject)

    thread = threading.Timer(10, subject.cancel_interval)
    thread.start()
