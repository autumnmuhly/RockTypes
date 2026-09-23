from plotPolygons import PlotPoly
import matplotlib.pyplot as plt
from definePoly import print_rocktype
from data_reader import read_csv_file
SiO2,Na2OK2O=read_csv_file('/Users/autumnmuhly/geol818/RockTypes/Voygar_samples.csv')
print_rocktype(SiO2,Na2OK2O)
figure=PlotPoly(SiO2,Na2OK2O)
plt.show()

