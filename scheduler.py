import time, threading

class Scheduler:
    def __init__(self, interface=None, timer=2, timer_measurement="seconds"):
        self.time_measurement_conv_table = {"seconds": 1, "minutes": 60, "hours": 3600}
        self.interface = interface
        self.waiting_time = timer * self.time_measurement_conv_table[timer_measurement]

        self._start_thread()

    def _start_thread(self):
        self.timer_thread = threading.Thread(target=self._wait)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def _wait(self):
        while True:
            time.sleep(self.waiting_time)
            self.interface.trigger_prompt()

