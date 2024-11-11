class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Demonstration
engine = Engine()
car = Car(engine)
car.start_engine()
car.stop_engine()
