from math import cos,sin,asin,sqrt,pow,pi

class City:
    def __init__(self,name,lon,lat):
        self.name = name;
        self.lon = lon;
        self.lat = lat;
        

def calcDist(city1,city2):
    R = 6371;
    l1 = rad(city1.lat)
    l2 = rad(city2.lat)
    l3 = rad(city1.lon)
    l4 = rad(city2.lon)
    tmp = pow( sin( (l1 - l2) / 2) , 2)
    tmp +=  pow( sin( (l3 - l4) / 2) , 2) * cos(l1) * cos(l2)
    tmp = sqrt(tmp)
    return 2 * R * asin(tmp)

def rad(d):
    return d * pi / 180.00;



if __name__ == '__main__':
    c1 = City('北京',116.46,39.92);
    c2 = City('天津',117.2,39.13);
    print(calcDist(c1,c2));