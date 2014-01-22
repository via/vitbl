import json
import StringIO
import sys
import re

class Table():
    def __init__(self):
        self.description = ""
        self.title = ""
        self.type = ""
        self.xlabel = ""        
        self.ylabel = ""        
        self.zlabel = ""        
        self.xdivs = []
        self.data = []

    def divisions(self):
        pass

    def interpolate(self, x, y): 
        pass

    def rescaleDivisions(self, newDivisions):
        pass

    def readJson(self, str):
        try: 
            jtbl = json.loads(str)
            self.title = jtbl['title']
            self.type = jtbl['type']
            self.description = jtbl['description']
            self.xlabel = jtbl['X']['label']
            self.ylabel = jtbl['Y']['label']
            self.zlabel = jtbl['Z']['label']
            self.xdivs = [float(x) for x in jtbl['X']['values']]
            self.data = [ [float(div)] for div in jtbl['Y']['values']]

            currow = 0
            for row in jtbl['Z']['values']:
                self.data[currow] = self.data[currow] + row
                currow = currow + 1
           
        except Exception:
            pass

    def writeJson(self, filename):
        pass

    def readPlain(self, f):
        m = re.match(r"\s*(.+)\((.+?)\)\s*$", f.readline().rstrip())
        if m is None:
            return
        if f.readline().rstrip() != "":
            return
        self.ylabel = f.readline().rstrip() 

    def writePlain(self):
        # Header (Description (Zlabel))
        #
        #Ylabel
	#
        # Ydiv
        # Ydiv
        # ...
        # Ydiv
        #
        # 	Xdiv	Xdiv	Xdiv
        #		Ylabel
        sio = StringIO.StringIO()
        sio.write(" {0} ({1})\n".format(self.description, self.zlabel))
        sio.write("\n")
        sio.write("{0}".format(self.ylabel))
        sio.write("\n")
        for y in self.data:
            for val in y: 
                sio.write("{0}\t".format(val))
            sio.write("\n")
        sio.write("\n{0}".format(self.xlabel))
        for x in self.xdivs:
            sio.write("\t{0}".format(x))
        return sio.getvalue()
        
    
        
        
  
if __name__ == "__main__":
    t = Table()
    t.readPlain(sys.stdin)
    #t.readJson(sys.stdin.read())
    #print t.writePlain()
