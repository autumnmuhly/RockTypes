from plotPolygons import PlotPoly
import matplotlib.pyplot as plt
from definePoly import print_rocktype
from data_reader_Zr import read_csv_file
from plotPolygons_Zr import add_ZrTi_fields
SiO2,Na2OK2O=read_csv_file('/Users/autumnmuhly/geol818/RockTypes/Voygar_samples_Zr.csv')
print_rocktype(SiO2,Na2OK2O)
figure=PlotPoly(SiO2,Na2OK2O,'All')
plt.show()

