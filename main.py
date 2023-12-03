class Point:

    def __init__(self,X,Y):
        self.x_cor = X
        self.y_cor = Y

    def __str__(self):
        return "({},{})".format(self.x_cor,self.y_cor)

    def euclidean_distance(self,other):
        return ((self.x_cor - other.x_cor)**2 + (self.y_cor - other.y_cor)**2) ** 0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))

class Line:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.c < 0:
            return "{}x + {}y - {} = 0".format(self.a,self.b,(self.c)*-1)
        else:
            return "{}x + {}y + {} = 0".format(self.a,self.b,self.c)

    def point_on_line_obj(self,point):
        if self.a*point.x_cor + self.b*point.y_cor + self.c == 0:
            return "Point lies on line"
        else:
            return "Point does not lie on line"

    def minimal_distance_from_line(self,point):
        return abs(self.a*point.x_cor + self.b*point.y_cor + self.c)/ (self.a**2 + self.b**2)**0.5


