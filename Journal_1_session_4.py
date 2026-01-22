class Horse:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Arm length:", self.arm_length)
        print("Leg length:", self.leg_length)
        print("Number of eyes:", self.num_eyes)
        print("Has a tail:", self.has_tail)
        print("Is furry:", self.is_furry)

horse = Horse(0.0, 1.6, 2, True, True)
horse.describe()