#added for group 32 project
#this is the observer class, to implement the observer design pattern 
#for the level win conditions

class Subject:
    def __init__(self):
        self.observers = []
        
    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            
    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(*args, **kwargs)
            
class Observer:
    def notify(self, *args, **kwargs):
        raise NotImplementedError("subclass must use this notify method")