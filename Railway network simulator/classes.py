
import railML

class rollingstock(railML):
    pass

class vehicles(rollingstock):
    pass

class vehicle(vehicles):
    def __init__(self,length,speed,bruttoWeight,nettoWeight,tareWeight,adhesionWeight,numberofAxles,maximumAxleLoad,belongsToParent,id):
        self.length = length
        self.speed = speed
        self.bruttoWeight = bruttoWeight
        self.nettoWeight = nettoWeight
        self.tareWeight = tareWeight
        self.adhesionWeight = adhesionWeight
        self.numberofAxles = numberofAxles
        self.maximumAxleLoad = maximumAxleLoad
        self.belongsToParent = belongsToParent
        self.id = id

class administrativeData(vehicle):
    pass

class brakes(vehicle):
    pass

class formations(rollingstock):
    pass

class engine(vehicle):
    def __init__(self,tractivePower):
        self.tractivePower = tractivePower
    
class formation(formations):
    def __init__(self,length,speed,totalWeight,haulingWeight,numberOfAxles,numberOfWagons,maximumAxleLoad,maximumCantDeficiency,id):
        self.length = length
        self.speed = speed
        self.totalWeight = totalWeight
        self.haulingWeight = haulingWeight
        self.numberOfAxles = numberOfAxles
        self.numberOfWagons = numberOfWagons
        self.maximumAxleLoad = maximumAxleLoad
        self.maximumCantDeficiency = maximumCantDeficiency
        self.id = id

class keeper(administrativeData):
    def __init__(self,refersTo):
        self.refersTo = refersTo

class manufacturer(administrativeData):
    def __init__(self,refersTo):
        self.refersTo = refersTo

class operator(administrativeData):
    def __init__(self,refersTo):
        self.refersTo = refersTo
    
class owner(administrativeData):
    def __init__(self,refersTo):
        self.refersTo = refersTo

class powerMode(engine):
    pass

class trainEngine(formation):
    def __init__(self,meanAcceleration,maxAcceleration,minTimeHoldSpeed):
        self.meanAcceleration = meanAcceleration
        self.maxAcceleration = maxAcceleration
        self.minTimeHoldSpeed = minTimeHoldSpeed

class tractiveEffort(trainEngine):
    pass

class trainResistance(formation):
    pass

class brakeEffort(brakes):
    pass

class segmentTable(brakeEffort,tractiveEffort, trainResistance):
    def __init__(self,segmentStartValueName,segmentStartValueUnit,functionValueName,functionValueUnit):
        self.segmentStartValueName = segmentStartValueName
        self.segmentStartValueUnit = segmentStartValueUnit
        self.functionValueName = functionValueName
        self.functionValueUnit = functionValueUnit

class segmentStartLine(segmentTable):
    def __init__(self,segmentStartValue):
        self.segmentStartValue = segmentStartValue

class polynomialHeader(segmentTable):
    def __init__(self,exponentValue):
        self.order = exponentValue

class tractionMode(trainEngine):
    pass

class trainBrakes(formation):
    pass

class trainOrder(rollingstock):
    def __init__(self,orderNumber,vehicleRef,orientation):
        self.orderNumber = orderNumber
        self.vehicleRef = vehicleRef
        self.orientation = orientation

class valueTable(brakeEffort,tractiveEffort, trainResistance):
    def __init__(self,xValueName,xValueUnit,yValueName,yValueUnit,zValueName,zValueUnit):
        self.xValueName = xValueName
        self.xValueUnit = xValueUnit
        self.yValueName = yValueName
        self.yValueUnit = yValueUnit
        self.zValueName = zValueName
        self.zValueUnit = zValueUnit

class valueLine(valueTable):
    def __init__(self,xValue):
        self.xValue = xValue

class value(valueLine):
    def __init__(self,yValue):
        self.value = yValue

class vehicleBrakes(brakes):
    pass

class vehiclePart(vehicle):
    def __init__(self,partOrder,airTightness,emergencyBrakeOverride,maximumCantDeficiency,id):
        self.partOrder = partOrder
        self.airTightness = airTightness
        self.emergencyBrakeOverride = emergencyBrakeOverride
        self.maximumCantDeficiency = maximumCantDeficiency
        self.id = id

class constantValue(segmentStartLine):
    def __init__(self, coefficientValue):
        self.coefficientValue = coefficientValue

class passengerFacilities(vehiclePart):
    pass

class freightFacilities(vehiclePart):
    pass

class columnHeader(valueTable):
    # the value of z-coordinate for the realte columnm
    def __init__(self,zValue):
        self.zValue = zValue