nodes = {
    "Gate1": (707,607),
    "Gate2": (768,604),
    "MainBlock": (491,367),
    "PlayGround": (305,369),
    "Auditorium": (139,612),
    "Xerox": (394,454),
    "HealthCentre": (784,593),
    "BlockA": (820,226),
    "BlockB": (883,136),
    "BlockC": (817,136),
    "Canteen tea time": (759,226),
    "Hostel":(53,486),
    "ILP":(485,170),
    "Girls_hostel":(372,167),
    "Boys hostel":(606,167),
    "Apurva canteen":(303,188),
    "C2C canteen": (306,276),
    "Basket ball court":(139,612),
    "OAT": (271,453),
    "Parking 1": (784,504),
    "Parking 2": (433,580),
    "Main canteen": (228,450)
}
graph = {

   "Gate1": ["Statue","n1","n2"],

   "Gate2": ["n1"],
   "n1":["n2","Gate2"],
   "n2":["Statue","n1"],

   "Statue": [
       "Gate1",
       "Gate2",
       "MainBlock",
       "Auditorium"
   ],

   "MainBlock": [
       "Statue",
       "BlockA",
       "Xerox"
   ],

   "BlockA": [
       "MainBlock",
       "BlockB",
       "BlockC"
   ],

   "BlockB": [
       "BlockA"
   ],

   "BlockC": [
       "BlockA",
       "HealthCentre"
   ],

   "HealthCentre": [
       "BlockC"
   ],

   "Xerox": [
       "MainBlock",
       "Canteen"
   ],

   "Canteen": [
       "Xerox"
   ],

   "Auditorium": [
       "Statue",
       "PlayGround"
   ],

   "PlayGround": [
       "Auditorium"
   ]
}