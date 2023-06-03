#Difficulty-Class has most Values, to simulate different Difficulties 
# easy | medium | hard 
class Difficulty:
  truckSpeed = 6
  truckFuelCapacity = 100
  fuelConsumptionPerMove = .1
  fuelPerTick = 2
  truckCapacity = 100
  loadPerTick = 1
  unloadPerTick = 1
  helicopterSpeed = 2.5
  helicopterStealPerTick = .5
  fuelStationCapacity = 1000
  warehouseCapacity = 1000
  storeCapacity = 500

  # Set difficulty (0=easy, 1=medium, 2=hard)
  def SetDifficulty(self, difficulty):
    # easy
    if difficulty == 0:
      self.truckSpeed = 6
      self.truckFuelCapacity = 100
      self.fuelConsumptionPerMove = .1
      self.fuelPerTick = 2
      self.truckCapacity = 100
      self.loadPerTick = 1
      self.unloadPerTick = 1
      self.helicopterSpeed = 2.5
      self.helicopterStealPerTick = .5
      self.fuelStationCapacity = 1000
      self.warehouseCapacity = 1000
      self.storeCapacity = 500
    # medium
    if difficulty == 1:
      self.truckSpeed = 6
      self.truckFuelCapacity = 100
      self.fuelConsumptionPerMove = .125
      self.fuelPerTick = 2
      self.truckCapacity = 100
      self.loadPerTick = .9
      self.unloadPerTick = .9
      self.helicopterSpeed = 3.5
      self.helicopterStealPerTick = .6
      self.fuelStationCapacity = 850
      self.warehouseCapacity = 900
      self.storeCapacity = 600
    # hard
    if difficulty == 2:
      self.truckSpeed = 6
      self.truckFuelCapacity = 100
      self.fuelConsumptionPerMove = .15
      self.fuelPerTick = 2
      self.truckCapacity = 100
      self.loadPerTick = .8
      self.unloadPerTick = .8
      self.helicopterSpeed = 4.5
      self.helicopterStealPerTick = .7
      self.fuelStationCapacity = 700
      self.warehouseCapacity = 800
      self.storeCapacity = 700
