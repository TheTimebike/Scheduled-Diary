import time, threading

class Scheduler:
    def __init__(self, interface=None, timer=10, timer_measurement="seconds"):
        self.time_measurement_conv_table = {"seconds": 1, "minutes": 60, "hours": 3600}
        self.interface = interface
        self.waiting_time = int(timer) * self.time_measurement_conv_table[timer_measurement]

        self._start_thread()

    def _start_thread(self):
        self.timer_thread = threading.Thread(target=self._wait)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def _wait(self):
        while True:
            self.interface.trigger_prompt()
            time.sleep(self.waiting_time)

