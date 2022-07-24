import pymzml

file = "data/TQ8_201023SJ01_0103.mzML"
run = pymzml.run.Reader(
    file
)

cumulative_spec = pymzml.spec.Spectrum(measured_precision=5e-1)

for spec in list(run)[:50]:
    cumulative_spec += spec

print(len(cumulative_spec.peaks("reprofiled")))
print(run.MS_precisions)

# p = pymzml.plot.Factory()
# p.new_plot()
# p.add(cumulative_spec.peaks("reprofiled"), color=(0, 0, 0), style="sticks", name="peaks")
# p.save(filename="./img/cumulative_spectrogram.html")
