import pymzml
file = "data/TQ8_201023SJ01_0103.mzML"
run = pymzml.run.Reader(
        file,
        MS1_Precision=5e-6,
        MSn_Precision=20e-6
    )

cumulative_spec = pymzml.spec.Spectrum(measured_precision = 20e-6)

for spec in run:
    cumulative_spec += spec


p = pymzml.plot.Factory()
p.new_plot()
p.add(cumulative_spec.peaks("reprofiled"), color=(0, 0, 0), style="sticks", name="peaks")
p.save(filename="./img/comulative_spectrogram.html")