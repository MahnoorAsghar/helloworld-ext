#This is the Vehicle Module.
#.. parameters:: parameters.yaml
#
class Vehicle:  
  def __init__(self, brand, model, vehicleType):
    """
    This function initialises the Vehicle.
    
    .. parameters:: parameters.yaml
       
       :brand: brand 
       :model: model
       :type: type

    """
    self.brand = brand
    self.model = model
    self.type = vechicleType
    self.gas_tank_size = 14
    self.fuel_level = 0

  def setAttributes(self, brand, model, vehicleType):
    """
    This function sets the Vehicle's brand.

    .. parameters:: parameters.yaml

       :brand: brand description
       :model: model description
       :vehicleType: type description
    """
    self.brand = brand
