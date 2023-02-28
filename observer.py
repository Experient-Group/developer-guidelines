from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Manage_Subscriber(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        #attach an observer to the newspaper
        pass

    @abstractmethod
    def detach(self,observer: Observer) -> None:
        #detach an observer from the newspaper
        pass

    @abstractmethod
    def notify(self) -> None:
        #update observer about event
        pass

class NewsPaper_Subscriber(Manage_Subscriber):
    #keep tracks of the state to see if any change is made
    _state: int = None
    #list of observers
    _observers: List[Observer]=[]


    def attach(self, observer : Observer) -> None:
        #add oberver to subscriber list
        print("Attach a subcriber to NewsPaper")
        self._observers.append(observer)

    def detach(self, observer : Observer) -> None:
        #remove observer from subscriber list
        self._observers.remove(observer)

    def notify(self) -> None:
        #notify all observers in subscriber/observer list
        print("Notify Observers of new events")
        for observer in self._observers:
            observer.update(self)

    def business_logic(self) -> None:
        #current news in one state
        print("\nCurrent News")
        self.state = randrange(0,10)
        #state is changed for notify to update the observer
        print(f"NewsPaper Event has changed to : {self.state}")
        self.notify()


class Observer(ABC):
    #abstract method for observer
    @abstractmethod
    def update(self, subject : Manage_Subscriber) -> None:
        pass

class AbleObserver(Observer):
    def update(self,subject :Manage_Subscriber) -> None:
        #observer updating the new event
        if subject.state <3:
            print("Able reacted to event")
        
class BeckyObserver(Observer):
    def update(self,subject :Manage_Subscriber) -> None:
        if subject.state ==3 or subject.state >= 2:
            print("Becky reacted to event")


if __name__ == "__main__":
    # The client code.

    subject = NewsPaper_Subscriber()

    observer_a = AbleObserver()
    subject.attach(observer_a)

    observer_b = BeckyObserver()
    subject.attach(observer_b)

    subject.business_logic()
    subject.business_logic()

    subject.detach(observer_a)

    subject.business_logic()