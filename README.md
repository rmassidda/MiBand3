# MiBand3
Python3 scripts to communicate with Xiaomi MiBand 3.

## Preparation
To install the prerequisites for the scripts:

```
pip install -r requirements.txt --user
```

To communicate with the MiBand3 the Bluetooth must obviously be turned on.
Further you need to find out the [MAC address](https://en.wikipedia.org/wiki/MAC_address) of your wrist band, to do so on a Linux machine you can use:

```
sudo hcitool lescan
```

Then you need to authorize the device with the following command, this should be done only the first time.

```
python3 mibandcli.py MAC_ADDRESS init
```

## Usage
After having paired Xiaomi MiBand3 you can run any of the commands listed in the helper.

```
python3 mibandcli.py --help
```

For instance to retrieve the battery level:

```
python3 mibandcli.py MAC_ADDRESS battery
```

### BLE Troubleshooting

If you having problems (BLE can glitch sometimes)

```
sudo hciconfig hci0 reset
```

#### If you have trouble installing bluepy

```
sudo apt-get install libglib2-dev
```


#### Fix hcitool I/O Error

```
sudo service bluetooth restart
```

## Attribution
This work is based on the efforts of numerous devs:

- [leojrfs/miband2](https://github.com/leojrfs/miband2)
- [vshymanskyy/miband2-python-test](https://github.com/vshymanskyy/miband2-python-test)
- [creotiv/MiBand2](https://github.com/creotiv/MiBand2)
- [yogeshojha/MiBand3](https://github.com/yogeshojha/MiBand3)
