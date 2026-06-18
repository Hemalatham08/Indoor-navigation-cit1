import qrcode

#locations = [
  #  "Gate1",
 #   "Gate2",
 #   "MainBlock",
 #   "Statue",
 #   "PlayGround",
 #   "Xerox",
 #   "HealthCentre",
 #   "BlockA",
 #   "BlockB",
   # "BlockC",
  #  "Canteen tea time",
 #   "Auditorium"
#]

#for location in locations:

 #   qr = qrcode.make(location)

 #   qr.save(f"static/{location}.png")
#    print("Created QR for", location)
data = "http://127.0.0.1:5000/?source=MainBlock"

img = qrcode.make(data)

img.save("static/MainBlock_qr.png")

print("QR Created")