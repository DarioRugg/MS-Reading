import pymzml
run = pymzml.run.Reader(
    "../data/TQ8_201023SJ01_0103.mzML",
    MS_precisions =  {
        1 : 5e-6,
        2 : 20e-6
    }
)
for entry in run:
    if isinstance(entry, pymzml.spec.Chromatogram):
        for time, intensity in entry.peaks:
            print(time, intensity)