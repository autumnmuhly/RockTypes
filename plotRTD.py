from polygonCreate import PlotPoly
import matplotlib.pyplot as plt
from definePoly import print_rocktype
silica = [50, 60, 70]
total_alkalis = [4, 5, 6]
print_rocktype(50,4)
figure=PlotPoly(silica,total_alkalis)
plt.show()

