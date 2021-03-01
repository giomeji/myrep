asciiFile=input("give the ascii file")
for i in range(len(asciiFile)):
    num1 = ord(asciiFile[len(asciiFile)-i-1])#παιρνω με αναποδη σειρα τους χαρακτηρες οπως ζητειται και τους μετατρεπω εναν εναν σε αριθμους
    num2 = 128 - num1#βρισκω τον κατοπτρικο τους
    asciiFile2 = chr(num2)#επειτα τον μετατρεπω σε χαρακτηρα
    print(asciiFile2, end="")#τελος, εκτυπωνω το κειμενο με τη σειρα που ζητειται



    
      
