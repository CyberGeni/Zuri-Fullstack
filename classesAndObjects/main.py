class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score      
    
    def change_name(self, name):
        print(name)
        
    def change_age(self, age):
        print(int(age))
        
    def add_track(self, *tracks):
        self.tracks.append(tracks)
        print(self.tracks)
        
    def get_score(self):
        print(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# user generated names
newName = input("Enter a new name: ")
newAge = int(input(" Enter a new age: "))
newTrack = input("Add track: ")

# Expected methods
Bob.change_name(newName)
Bob.change_age(newAge)
Bob.add_track(newTrack)
Bob.get_score()
