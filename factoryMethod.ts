// Factory Method
abstract class Creator {
    public abstract factoryMethod(): Product; // implementation of the factoryMethod is handled by subclasses, which should return an object following the Product interface defined below

    public someOperation(): string {
        const product = this.factoryMethod();
        return `Creator: The same creator's code has just worked with ${product.operation()}`;
    }
}

class ConcreteCreator1 extends Creator {
    public factoryMethod(): Product { // overrides the factoryMethod from the Creator class
        return new ConcreteProduct1(); // returns ConcreteProduct1, which implements the Product inferface
    }
}

class ConcreteCreator2 extends Creator {
    public factoryMethod(): Product {
        return new ConcreteProduct2(); // returns ConcreteProduct2, which implements the Product inferface
    }
}

interface Product {
    operation(): string;
}

class ConcreteProduct1 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct1}';
    }
}

class ConcreteProduct2 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct2}';
    }
}

function clientCode(creator: Creator) {
    console.log('Client: I\'m not aware of the creator\'s class, but it still works.');
    console.log(creator.someOperation());
}

console.log('App: Launched with the ConcreteCreator1.');
clientCode(new ConcreteCreator1());

console.log('App: Launched with the ConcreteCreator2.');
clientCode(new ConcreteCreator2());