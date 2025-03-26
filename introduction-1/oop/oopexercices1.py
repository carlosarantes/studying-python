# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self): # Square root = (x2 - x1)elv 2 + (y2 - y1)elv 2 
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        d = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return d
    

    def slope(self): # m = y2 - y1 / x2 - x1
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        m = (y2 - y1)/(x2 - x1)
        return m

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1, coordinate2)
line.distance() # 9.433981132056603
line.slope() # 1.6


# Fill in the class
class Cylinder:

    PI = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self): # V=πr2h
        v = self.PI*(self.radius**2)*self.height
        return v
    
    def surface_area(self): # A=2 π r h + 2πr2
        a = (2*self.PI*self.radius*self.height) + (2*self.PI*self.radius*2)
        return a


cylinder = Cylinder(5, 1.8)
print('Surface area {}'.format(cylinder.surface_area()))
print('Volume {}'.format(cylinder.volume()))