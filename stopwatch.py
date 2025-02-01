
import math
import os
import sys


class Swimmer():
    def __init__(self, swimmer_name, times):
        self.info = swimmer_name.split('-')
        self.name = self.info[0]
        self.age = self.info[1]
        self.length = self.info[2]
        self.stroke = self.info[3].removesuffix(".txt")  
        self.time_db = []
        for time in times.split(','):
            self.time_db.append(self.convert_to_seconds(time))  

    def add_time(self, time):
        self.time_db.append(self.convert_to_seconds(time))  
   
    def __str__(self):

        return f"{self.name} has and best time of {self.get_best_time()} when swimming {self.stroke} at {self.length} and an average time of {self.get_average_time()}"
    
    def get_best_time(self):
        return self.convert_to_minutes(min(self.time_db))
    
    def get_worst_time(self):
        return max(self.time_db)
    
    def get_average_time(self):
        avg_time_seconds = sum(self.time_db) / len(self.time_db)  # ✅ Average in seconds
        minutes = int(avg_time_seconds // 60)
        seconds = int(avg_time_seconds % 60)
        milliseconds = round((avg_time_seconds - int(avg_time_seconds)) * 100)  # ✅ Proper rounding

        return f"{minutes}:{seconds:02}.{milliseconds:02}"  # ✅ Ensures correct output
    
    def convert_to_seconds(self, time):
        if "." in time and ":" in time:
            time = time.replace('.', ':')
            minutes, seconds, milliseconds = time.split(':')
        else:
            seconds, milliseconds = time.split('.')
            minutes = 0
        return int(minutes) * 60 + int(seconds) + int(milliseconds) / 100
    
    def convert_to_minutes(self, time):
        minutes = int(time // 60)
        seconds = int(time % 60)
        milliseconds = round((time - int(time)) * 100)
        return f"{minutes}:{seconds:02}.{milliseconds:02}"

class SwimBook:
    def __init__(self):
        self.swimmers = []

    def print_all(self):
        for person in self.swimmers:
            print(person)

    def print_person(self, person, stroke):
        swim_list = []
        for swimmer in self.swimmers:
            if swimmer.name == person and (stroke is None or swimmer.stroke == stroke):
                swim_list.append(swimmer)
        return swim_list

    def load_data_from_file(self):
        directory = c_dir = os.getcwd()
        self.directory = directory + '/swimdata'
        all_files_path = []
        all_files_just_name = []

        for root, dirs, files in os.walk(self.directory):
            for file in files:
                all_files_path.append(os.path.join(root, file))
                all_files_just_name.append(file)
        for x, swimmer in enumerate(all_files_just_name):
            if swimmer.startswith("."):
                continue
            else:
                f = open(all_files_path[x], "r")
                self.swimmers.append(Swimmer(swimmer,f.readline()))
        

class Files:
    def __init__(self):
        directory = c_dir = os.getcwd()
        self.directory = directory + '/swimdata'

    def get_numnber_of_files(self):
        file_count = 0
        print(self.directory)
        for root, dirs, files in os.walk(self.directory):
            file_count += len(files)
        return file_count      
      

    


def app():
    swimbook = SwimBook()
    swimbook.load_data_from_file()
    while True:
        choice = input('(S)earch for swimmer, (A)dd swim time, (Q)uit ')
        if choice.upper() == "Q":
            sys.exit(1)
        elif choice.upper() == 'S':
            name = input("Name of swimmer: ")
            swim_type = input("Swim Type (empty will query every age): ") or None
            swim_list = swimbook.print_person(name, swim_type)
            for swimmer in swim_list:
                print(swimmer)

if __name__ == "__main__":
    app()







