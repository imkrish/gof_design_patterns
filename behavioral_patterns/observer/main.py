from clock_timer import ClockTimer
from digital_clock import DigitalClock
from analog_clock import AnalogClock
import threading


if __name__ == '__main__':

    subject = ClockTimer()  # Creates a subject object

    digital_clock1 = DigitalClock(subject)  # Creates an observer object and attaches its self to the subject
    analog_clock1 = AnalogClock(subject)  # Creates an observer object and attaches its self to the subject

    analog_clock1.unsubscribe()

    thread = threading.Timer(100, subject.cancel_interval)  # After 100 seconds will stop the subject from notifying 
    thread.start()

    # digital_clock2 = DigitalClock(subject)
    # analog_clock2 = AnalogClock(subject)



