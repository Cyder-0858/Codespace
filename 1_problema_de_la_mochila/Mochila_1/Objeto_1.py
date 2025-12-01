class Item:
    def __init__(self, name, weight, priority):
        self.name = name
        self.weight = weight
        self.priority = priority

    def __repr__(self):
        return f"{self.name} (W:{self.weight}, P:{self.priority})"
