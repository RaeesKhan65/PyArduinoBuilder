import subprocess
from pathlib import Path


class PyArduinoConn:

    def __init__(self,name):
        self.path = Path.joinpath(Path().resolve(),"ArduinoSketches",name)
        self.core = "arduino:sam:arduino_due_x_dbg"
        self.board = "/dev/cu.usbmodem14201"


    def newSketch(self):

        try:
            subprocess.run(["arduino-cli","sketch","new",self.path,"-v"])
        except:
            print("Error")


    def compileSketch(self):

        try:
            subprocess.run(["arduino-cli","compile","-b",self.core,self.path,"-v"])
        except:
            print("Error")

    def uploadSketch(self):

        try:
            subprocess.run(["arduino-cli","upload","-b",self.core,"-p",self.board,self.path,"-v"])
        except:
            print("Error")

PyArduinoConn("test").newSketch()