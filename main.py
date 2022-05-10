import pymzml
import matplotlib.pyplot as plt
import numpy as np

mzml_file = 'data/TQ8_201023SJ01_0103.mzML'

msrun = pymzml.run.Reader(mzml_file)

