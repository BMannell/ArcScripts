import arcpy
from arcpy import env

# script arguments
shape = arcpy.GetParameterAsText(0)

# extract extent from feature
extent = arcpy.Describe(shape).extent
west = extent.XMin
south = extent.YMin
east = extent.XMax
north = extent.YMax

# create hexagons
arcpy.management.GenerateTessellation(arcpy.GetParameterAsText(1), "%s %s %s %s" % (west, south, east, north), "HEXAGON", "30 Hectares")
