# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])
print(captains.get("Enterprise"))
print(captains.get("NX-01"))

for ship in captains:
    print(ship + ": " +captains[ship])