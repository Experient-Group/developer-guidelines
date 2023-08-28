from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_product_chair(self) -> AbstractProductChair:
        pass

    @abstractmethod
    def create_product_sofa(self) -> AbstractProductSofa:
        pass

    @abstractmethod
    def create_product_coffeetable(self) -> AbstractProductCoffeeTable:
        pass


class ArtDecoFactory(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_chair(self) -> AbstractProductChair:
        return ArtDecoChair()

    def create_product_sofa(self) -> AbstractProductSofa:
        return ArtDecoSofa()
    
    def create_product_coffeetable(self) -> AbstractProductCoffeeTable:
        return ArtDecoCoffeeTable()


class VictorianFactory(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """
    def create_product_chair(self) -> AbstractProductChair:
        return VictorianChair()

    def create_product_sofa(self) -> AbstractProductSofa:
        return VictorianSofa()
    
    def create_product_coffeetable(self) -> AbstractProductCoffeeTable:
        return VictorianCoffeeTable()


class AbstractProductChair(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class AbstractProductSofa(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass
    

class AbstractProductCoffeeTable(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ArtDecoChair(AbstractProductChair):
    def useful_function_a(self) -> str:
        return "The result of the product ArtDecoChair."
    

class ArtDecoSofa(AbstractProductSofa):
    def useful_function_a(self) -> str:
        return "The result of the product ArtDecoSofa."

class ArtDecoCoffeeTable(AbstractProductCoffeeTable):
    def useful_function_a(self) -> str:
        return "The result of the product ArtDecoCoffeeTable."


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class VictorianChair(AbstractProductChair):
    def useful_function_a(self) -> str:
        return "The result of the product VictorianChair."

class VictorianSofa(AbstractProductSofa):
    def useful_function_a(self) -> str:
        return "The result of the product VictorianSofa."

class VictorianCoffeeTable(AbstractProductCoffeeTable):
    def useful_function_a(self) -> str:
        return "The result of the product VictorianCoffeeTable."
    

def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_chair = factory.create_product_chair()
    product_sofa = factory.create_product_sofa()

    print(f"{product_chair.useful_function_a()}")
    print(f"{product_sofa.useful_function_a()}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ArtDecoFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(VictorianFactory())