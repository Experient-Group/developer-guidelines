//
//  ViewController.swift
//  ObservableDesignPattern
//
//  Created by Tala Emami on 8/22/23.
//

import UIKit

///The Observer protocol confirms the update() method, is getting used by Publisher class
protocol Observable: AnyObject {
    func update(publisher: MagazinePublisher)
}
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
//        func ObserverTest() {
            let publisher = MagazinePublisher()
            let observerA = ClientobserverA()
            let observerB = ClientobserverB()

            publisher.addObserver(observer: observerA)
            publisher.addObserver(observer: observerB)
            publisher.businessLogic()
            publisher.businessLogic()
            publisher.removeObserver(observer: observerA)
            publisher.businessLogic()
//          }
    }

    

}

class MagazinePublisher {

    var state: Int = {
        return Int.random(in: 0..<5)
    }()
    
    /// Make the Publisher Singleton in order to share its instances with Observer classes
    static let shared: MagazinePublisher = MagazinePublisher()
    private lazy var observers = [Observable]()
    
    /// Get called from observer class to add the observer into the array
    func addObserver(observer: Observable) {
        print("Publisher: New observer is added. \n")
        observers.append(observer)
    }
    
    /// Get called form observer class to remove that observer from array
    func removeObserver(observer: Observable) {
        if let index = observers.firstIndex(where: { $0 === observer}) {
            observers.remove(at: index)
            print("Publisher: An observer is removed. \n")
        }
    }

    /// Call update method in each observer
    func notifyObserver() {
        print("Publisher: Notifying observers. \n")
        observers.forEach({ $0.update(publisher: self) })
    }

    /// The place that particular event happen, then call the notifyObserver method to call the update method in each observer
    func businessLogic() {
        print("\rPublisher: Here is business logic is running. \n")
        state = Int.random(in: 0..<5)
        print("Publisher: The state has changed to: \(state) \n")
        notifyObserver()
    }
}

/// Defined two observer classes
class ClientobserverA: Observable {
    init() {
        MagazinePublisher.shared.addObserver(observer: self)
    }
    func update(publisher: MagazinePublisher) {
        if publisher.state < 5 {
            print("observerA: Received the update call. \n")
        }
    }
}

class ClientobserverB: Observable {
    init() {
        MagazinePublisher.shared.addObserver(observer: self)
    }
    func update(publisher: MagazinePublisher) {
        if publisher.state == 4 {
            print("observerB: Received the update call. \n")
        }
    }
}

