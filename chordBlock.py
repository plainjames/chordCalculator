class octave:
  def __init__(self, keyArray):
    self.keyArray = keyArray
    self.isMajor = False
    self.isMinor = False


  def printNotes(self):
        print(" C:", + self.keyArray[0], " Db:", self.keyArray[1]," D:",self.keyArray[2],
         " Eb:", self.keyArray[3]," E:", self.keyArray[4]," F:",self.keyArray[5],
          " Gb:",self.keyArray[6], " G:",self.keyArray[7], " Ab:", self.keyArray[8],
          " A:", self.keyArray[9], " Bb:" ,self.keyArray[10], " B:",self.keyArray[11])

  def chordReverse(self):
      self.keyArray.reverse()
      self.chordPrint()

  def UpSemitone(self, i):
      self.parseOctave()
      self.printState()
      print("Translating up ",i, " semitones...")
      while (i >0):
         x = self.keyArray[11]
         self.keyArray.pop(11)
         self.keyArray.insert(0, x)
         self.parseOctave()
         self.printState()
         i = i- 1
      print("done")

  def DownSemitone(self, i):
      print("Will translate")
      self.parseOctave()
      self.printState()
      print("down",i,"semitones...")
      while (i >0):
         x = self.keyArray[0]
         self.keyArray.pop(0)
         self.keyArray.insert(11, x)
         self.parseOctave()
         self.printState()
         i = i- 1
      print("done")

  def printState(self):
      if self.isMajor:
          print(self.keyArray, 'I am a major chord.')

      if self.isMinor:
          temporaryList = list(self.keyArray)
          popCounter = 0
          rootNote = ""
          for e in temporaryList:
              if e == 0:
                  temporaryList.pop(e)
                  popCounter += 1
              elif popCounter == 0:
                  rootNote = "C"
              elif popCounter == 1:
                  rootNote == "C#"
              elif popCounter == 2:
                  rootNote == "D"
              elif popCounter == 3:
                  rootNote == "D#"
          print(self.keyArray, rootNote, "minor chord I am.")


  def parseOctave(self):
      c = self.keyArray[0]
      db = self.keyArray[1]
      d = self.keyArray[2]
      eb = self.keyArray[3]
      e = self.keyArray[4]
      f = self.keyArray[5]
      gb = self.keyArray[6]
      g = self.keyArray[7]
      ab = self.keyArray[8]
      a = self.keyArray[9]
      bb = self.keyArray[10]
      b = self.keyArray[11]

      #Major Key state checker and setter (based on intervals 4 semitones and 7 semitones from the root note)
      x=0
      while (x < 4):
          switch = True
          if (self.keyArray[x] == 1 and self.keyArray[x+4] == 1 and self.keyArray[x+7] == 1 and switch == True):
              self.isMajor = True

              self.isMinor = False
              break
          else:
              x = x + 1

      #Minor-chord state checker and setter (based on intervals of 3 and 7 semitones from the root note)
      y=0
      while (y < 4):
          switch = True
          if (self.keyArray[y] == 1 and self.keyArray[y+3] == 1 and self.keyArray[y+7] == 1 and switch == True):
              self.isMinor = True

              self.isMajor = False
              break
          else:
              y = y + 1



def main():
  print("Welcome to chordCalculator")



if __name__ == "__main__":
  main()

  majorC= octave([1,0,0,1,0,0,0,1,0,0,0,0])

  majorC.UpSemitone(100)
  majorC.DownSemitone(10)
  majorC.printNotes()

