asciiFile=input("give the ascii file")
for i in range(len(asciiFile)):
    num1 = ord(asciiFile[len(asciiFile)-i-1])#παιρνω με αναποδη σειρα τους χαρακτηρες οπως ζητειται και τους μετατρεπω εναν εναν σε αριθμους
    katop = 128 - num1#βρισκω τον κατοπτρικο τους
    xarakthras = chr(katop)#επειτα τον μετατρεπω σε χαρακτηρα
    print(xarakthras, end="")#τελος, εκτυπωνω το κειμενο με τη σειρα που ζητειται



    
      
