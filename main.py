class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = int(new_age)
    def add_track(self, new_track):
        self.tracks.append(new_track)
    def get_score(self):
        return self.score
Bob = Student("Bob", 26, ["FE","BE"], 20.90)
# print(Bob.tracks)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
# print(Bob.name)
# print(Bob.age)
# print(Bob.tracks)
# print(Bob.get_score())

Scott = Student('Scott', 24, ["Fullstack", "Web3.0"], 30)
print(Scott.name)
Scott.change_name('Elijah')
print(Scott.name)
Scott.add_track('Product management')
print(Scott.tracks)
print(Scott.get_score())