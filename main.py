import mne
import sys
import numpy as np
import matplotlib.pyplot as plt

task = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
task = [3]

def main():
    data = mne.datasets.eegbci.load_data(1, task)
    raws = [mne.io.read_raw_edf(f, preload=True) for f in data]
    data = mne.io.concatenate_raws(raws)

    data.plot(block=True, lowpass=40)
    #data.plot_psd(tmax=np.inf, average=False)

    event = mne.find_events(data, consecutive=True, initial_event=True, output='offset')
    #print(np.shape(event))
    #print(event)

    epoch = mne.Epochs(data, events=event)
    print(np.shape(epoch))
    print(epoch)
    epoch_data = epoch['1'].get_data()
    epoch_data2 = epoch['2'].get_data()
    epoch_data3 = epoch['3'].get_data()
    print(epoch_data.shape)
    print(epoch_data2.shape)
    print(epoch_data3.shape)
    channel = 10
    plt.plot(epoch_data[6][channel], color='b')
    plt.plot(epoch_data2[6][channel], color='r')
    plt.plot(epoch_data3[6][channel], color='g')
    plt.xlabel('time(s)')
    plt.legend(['T0', 'T1', 'T2'])
    plt.show()
    
if  __name__ == '__main__':
    main()
