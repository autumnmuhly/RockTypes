from shapely import Point,Polygon
def print_rocktype(silica,total_alkalis):
    """
    Takes in a point and tells you the rock type
    """
    vertices={}
    vertices['basalt']=[(45,1),(45,5),(52,5),(52,1)]
    vertices['basAnd']=[(52,1),(52,5),(57,6),(57,1)]
    vertices['ande']=[(57,1),(57,6),(63,7),(63,1)]
    vertices['dac']=[(63,1),(63,7),(70,7.5),(76,1)]
    point=Point(silica,total_alkalis)
    for rockType in vertices:
        polygon=Polygon(vertices[rockType])
        point=Point(silica,total_alkalis)
        if str(polygon.contains(point)) == 'True':
            [print(f'the point {silica,total_alkalis} is {rockType})')]