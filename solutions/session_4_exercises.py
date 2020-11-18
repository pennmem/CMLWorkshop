# Exercise: Analyze 3 seconds of the power sectrum of the first channel for subject R1292E. What do you notice?

# Where's the line noise?
plt.figure(figsize=(3.5, 3))
ax = plt.subplot(111)
plt.plot(freqs, np.log10(np.mean(psds[:, 0, :], 0)), linewidth=2)
plt.title('Average PSD')
plt.xlabel('Frequency (Hz)')
plt.ylabel('log Power')
plt.vlines([60, 120], ymin=ax.get_ylim()[0], ymax=ax.get_ylim()[1], color='red', alpha=0.5)

######################################

# Filtering out the 60 Hz electrical line noise and its harmonic at 120 Hz
# Here's a potential solution:

# Butterworth filtering: 60 Hz and 120 Hz
filt_data = eeg.filter(l_freq=62., h_freq=58., method='iir')
filt_data = filt_data.filter(l_freq=122., h_freq=118., method='iir')

# Get power spectral densities
psds, freqs = time_frequency.psd_welch(filt_data, fmin=3, fmax=150)  #the output is size (events x channels x freqs)

# Plot individual trial example
plt.figure(figsize=(7, 3))
ax = plt.subplot(121);
plt.plot(filt_data.get_data()[0, 0, :]);
plt.title('EEG trace')
plt.xlabel('Time (samples)')
plt.ylabel('Voltage')

ax = plt.subplot(122);
plt.plot(freqs, np.log10(psds[0, 0, :]))
plt.title('Power Spectral Density')
plt.xlabel('Frequency')
plt.ylabel('log Power')

plt.tight_layout()

# Plot average PSD
plt.figure(figsize=(3.5, 3))
ax = plt.subplot(111)
plt.plot(freqs, np.log10(np.mean(psds[:, 0, :], 0)), linewidth=2)
plt.title('Notch Filtered Data')

######################################3

import mne

# Load the EEG as an mne object.
eeg = load.LoadMNE(df_sess, ev_start=0, ev_len=3000)
# Select all word events.
eeg = eeg[word_evs.index]
# Select the 62nd electrode.
eeg = eeg.pick_channels(eeg.ch_names[0:1])

# spectrum_fit method
filt_data = mne.filter.notch_filter(eeg.get_data(), Fs=eeg.info['sfreq'], freqs=[60, 120],
                                    method='spectrum_fit')

# Get power spectral densities
# the output is size (events x channels x freqs)
psds, freqs = mne.time_frequency.psd_array_welch(filt_data, sfreq=eeg.info['sfreq'],
                                                 fmin=3, fmax=150)

plt.figure(figsize=(3.5, 3))
ax = plt.subplot(111)
plt.plot(freqs, np.log10(np.mean(psds[:, 0, :], 0)), linewidth=2)
plt.title('Notch Filtered Data')


