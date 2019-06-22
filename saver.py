import json, datetime, sys, os

class Saver:
    def __init__(self):
        self.save_location = "./"
        self.save_name = "DiaryEntries.txt"

    def _create(self):
        if not os.path.isfile(self.save_location + self.save_name):
            with open(self.save_location+self.save_name, "w+") as new:
                json.dump({"test": 69}, new, indent=4)

    def _open(self):
        with open(self.save_location+self.save_name, "r+") as out:
            new_data = json.load(out)
        return new_data

    def _new_entry(self, entry="An Error Occured"):
        self._create()
        new_data = self._open()
        time_string = str(datetime.datetime.now()).replace(", ", "-")
        print(time_string)
        new_data[time_string] = entry
        with open(self.save_location+self.save_name, "w+") as new:
            json.dump(new_data, new, indent=4)
        
