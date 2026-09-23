import matplotlib.pyplot as plt
from shapely.geometry import Point,Polygon 
__all__ = ['add_LeMaitre_fields']

class MissingModuleException(Exception):
    pass

 
# Plot LeMaitre lines
def add_LeMaitre_fields(plot_axes, fontsize=8, color=(0.6, 0.6, 0.6)):
    """Add fields for geochemical classifications from LeMaitre et al (2002)
    to pre-existing axes.  If necessary, the axes object can be retrieved via
    plt.gca() command. e.g.
    
    ax1 = plt.gca()
    add_LeMaitre_fields(ax1)
    ax1.plot(Zr_Ti, Nb_Y, 'o')
    
    Fontsize and color options can be used to change from the defaults.
    
    It may be necessary to follow the command with plt.draw() to update
    the plot.
    
    Le Maitre RW (2002) Igneous rocks : IUGS classification and glossary of
        terms : recommendations of the International Union of Geological 
        Sciences Subcommission on the Systematics of igneous rocks, 2nd ed. 
        Cambridge University Press, Cambridge
"""

    # Check matplotlib is imported
    import sys
    if 'matplotlib.pyplot' not in sys.modules:
        raise MissingModuleException("""Matplotlib not imported.
        Matplotlib is installed as part of many scientific packages and is
        required to create plots.""")
    
    # Check that plot_axis can plot
    if 'plot' not in dir(plot_axes):
        raise TypeError('plot_axes is not a matplotlib axes instance.')
    
    # Prepare the field information
    from collections import namedtuple
    FieldLine = namedtuple('FieldLine', 'x1 y1 x2 y2')
    lines = (FieldLine(x1=0.67, y1=0.002, x2=0.67, y2=0.2),
             FieldLine(x1=0.67, y1=0.2, x2=0.065, y2=2),
             FieldLine(x1=0.67, y1=0.2, x2=5.52, y2=2),
             FieldLine(x1=2.81, y1=0.002, x2=2.81, y2=0.99),
             FieldLine(x1=0.1, y1=0.008, x2=20, y2=0.067),
             FieldLine(x1=0.1, y1=0.026, x2=20, y2=0.2))
             

    FieldName = namedtuple('FieldName', 'name x y rotation')
    names = (FieldName('Alkali Basalt', 0.8, 0.01, 0),
             FieldName('Basalt', 0.1, 0.06, 0),
             FieldName('Andesite/Basaltic Andesite', 0.2, 0.02, 0),
             FieldName('Rhyolite/Dacite', 0.4, 2, 0),
             FieldName('Trachyte', 1, 2, 0),
             FieldName('Phonolite', 5, 4, 0),
             FieldName('Tephraphonolite', 5, 0.8, 0),
             FieldName('Alkali Rhyolite', 0.2, 1, 0),
             FieldName('Trachyandesite)', 0.8, 0.4, 0),
             FieldName('Foidite', 5, .06, 0),)

    # Plot the lines and fields
    for line in lines:
        plot_axes.plot([line.x1, line.x2], [line.y1, line.y2],
                       '-', color=color, zorder=0)
    for name in names:
        plot_axes.text(name.x, name.y, name.name, color=color, size=fontsize,
                 horizontalalignment='center', verticalalignment='top',
                 rotation=name.rotation, zorder=0)



def PlotPoly(Zr_Ti, Nb_Y, name='Zr_plot.png'):
    """
    Plots Zr/Ti vs Nb/Y plot. Must give a point, saves plot as Zr_plot.png
    """
    fig = plt.figure()
    ax1 = plt.gca()
    add_LeMaitre_fields(ax1)
    ax1.plot(Zr_Ti, Nb_Y, 'o')
    plt.xscale('log')
    plt.yscale('log')
    saved_fig=plt.savefig('Zr_plot.png', dpi=900, bbox_inches='tight', pad_inches=0.1)
    return saved_fig