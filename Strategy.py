from __future__ import annotations
from abc import ABC, abstractmethod


class Box():
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    def __str__(self):
        return self.name + ", " + self.color + " ," + self.size

class Organization():
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    def strategy(self):
        return self._strategy
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
    def organize_boxes(self, boxes):
        return(self._strategy.organize(boxes))

class Strategy(ABC):
    @abstractmethod
    def organize(self, data):
        pass

class ByColor(Strategy):
    def organize(self, data):
        return data.sort(key=lambda box: box.color)

class BySize(Strategy):
    def organize(self, data):
        return data.sort(key=lambda box: box.size)

class ByName(Strategy):
    def organize(self, data):
        return data.sort(key=lambda box: box.name)
    
if __name__ == "__main__":
    box1 = Box("box1", "red", "small")
    box2 = Box("box2", "blue", "large")
    box3 = Box("box3", "blue", "small")
    box4 = Box("box4", "red", "large")
    boxes = [box1, box2, box3, box4]

    organization = Organization(ByName)

    organization.set_strategy(ByColor())
    print("Sorted by color: ")
    organization.organize_boxes(boxes)
    for i in boxes:
        print(i)
    print("\n")

    organization.set_strategy(BySize())
    print("Sorted by size: ")
    organization.organize_boxes(boxes)
    for i in boxes:
        print(i)
    print("\n")

    organization.set_strategy(ByName())
    print("Sorted by name: ")
    organization.organize_boxes(boxes)
    for i in boxes:
        print(i)
    print("\n")