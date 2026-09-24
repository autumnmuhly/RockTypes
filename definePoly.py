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
    vertices['trachybasalt']=[(45,5),(49,7),(52,5)]
    vertices['basaltic trachyandesite']=[(52,5),(50,7),(53,9),(57,6)]
    vertices['trachyandesite']=[(57,6),(53,9),(57,11.5),(63,6)]
    vertices['Trachyte\n(Q < 20%)\n\nTrachydacite\n(Q > 20%']=[(69,7.5),(63,6.5),(58,11.5)]
    vertices['Tephrite\n(Ol < 10%\n\nBasanite\n(Ol > 10%']=[(41,3),(41,7),(45,9.3),(49,7.3),(45,5),(45,3)]
    vertices['picro basalt']=[(41,1),(41,3),(45,3),(45,1)]
    vertices['Phonotephrite']=[(49,7),(45,9.5),(49,11.5),(53,9)]
    vertices['tephriphonolite']=[(53,9),(48,11.5),(53,14),(57,11.5)]
    vertices['phonolite']=[(61,13),(58,11.5),(51,15)]
    vertices['rhyolite']=[(77,1),(69,7.5),(70,13)]
    for si,total_alk in zip(silica,total_alkalis):
        for rockType in vertices:
            polygon=Polygon(vertices[rockType])
            point=Point(si,total_alk)
            if str(polygon.contains(point)) == 'True':
                [print(f'the point {si,total_alk} is {rockType})')]

