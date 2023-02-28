from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFurnitureFactory(ABC):
    #abstract class for fruniture
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    def create_table(self) -> AbstractTable:
        pass

class VictorianFactory(AbstractFurnitureFactory):
    #using abstract class as base, creat fruniture for victorian style
    def create_chair(self) -> AbstractChair:
        return VictorianFactoryChair()

    def create_table(self) -> AbstractTable:
        return VictorianFactoryTable()

class ModernFactory(AbstractFurnitureFactory):
    #using abstract class as base, creat fruniture for modern style
    def create_chair(self) -> AbstractChair:
        return ModernFactoryChair()

    def create_table(self) -> AbstractTable:
        return ModernFactoryTable()
    
class AbstractChair(ABC):
    #abstarct class for chair
    @abstractmethod
    def make_chair(self) -> str:
        pass

class VictorianFactoryChair(AbstractChair):
    #make victorian chair
    def make_chair(self) -> str:
        return "Victorian Chair!"
    
class ModernFactoryChair(AbstractChair):
    #make modern chair
    def make_chair(self) -> str:
        return "Modern Chair!"

class AbstractTable(ABC):
    #abstract class for table
    @abstractmethod
    def make_table(self) -> str:
        pass
class VictorianFactoryTable(AbstractTable):
    #make victorian table
    def make_table(self) -> str:
        return "Victorian Chair"

class ModernFactoryTable(AbstractTable):
    #make modern table
    def make_table(self) -> str:
        return "Modern Table"
    

def client_code(factory :AbstractFurnitureFactory) -> None:
    Chair = factory.create_chair()
    Table = factory.create_table()
    
    print(f"{Table.make_table()}")



if __name__ == "__main__":

    print("Code Test for Victorian Chair")
    client_code(VictorianFactory())
    print("\n")
    print("Code Test for Modern Table")
    client_code(ModernFactory())


