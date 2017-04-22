# adapted from http://gis.stackexchange.com/questions/28583/gdal-perform-simple-least-cost-path-analysis
# with documentation from http://scikit-image.org/docs/dev/api/skimage.graph.html?highlight=cost#skimage.graph.MCP.find_costs
import sys, getopt, gdal, osr, os, psycopg2
from skimage.graph import MCP
from skimage.morphology import disk
from scipy.ndimage.filters import minimum_filter
import numpy as np


def createLCD(costSurfaceArray,startIndexX,startIndexY):
    '''
    Creates a least cost distance matrix beginning at a point of origin and
    spreading outward using costs from a numpy array

    Inputs: costSurfaceArray -> Numpy array of cell costs
            startXIndex -> Index of the starting x coordinate in the cost array
            startYIndex -> Index of the starting y coordinate in the cost array

    Returns: Numpy array of cumulative costs
    '''

    # create cost surface
    graph = MCP(costSurfaceArray,fully_connected=False)
    fullCosts, costTraces = graph.find_costs([(startIndexY,startIndexX)])
    return fullCosts
