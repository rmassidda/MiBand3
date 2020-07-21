from auth import MiBand3
import argparse
import sys

def perr(*arg):
    print(arg, file=sys.stderr)

commands = ['init', 'time', 'info', 'steps', 'battery', 'hearth']

parser = argparse.ArgumentParser(description='CLI to interact with Mi Band 3 wrist band')
parser.add_argument('--mac',help='MAC address of the band',required=True)
parser.add_argument('cmd',help='Operation required',choices=commands,nargs=1)
args = parser.parse_args()

mac = args.mac
cmd = args.cmd[0]

# Instance of MiBand3
band = MiBand3(mac, debug=True)
band.setSecurityLevel(level = "medium")

# Initialize or authenticate
if cmd == 'init':
    if band.initialize():
        perr("Initialized...")
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()

if cmd == 'battery':
    print('Battery:', band.get_battery_info())
elif cmd == 'steps':
    print('Steps:', band.get_steps())
elif cmd == 'time':
    print('Time:', band.get_current_time())
elif cmd == 'info':
    print('Hardware revision:',band.get_hrdw_revision())
    print('Serial:',band.get_serial())
    print('Soft revision:',band.get_revision())
elif cmd == 'hearth':
    try:
        band.start_raw_data_realtime(heart_measure_callback=lambda e: print('BPM1:',e),
                heart_raw_callback=lambda e:print('BMP2:',e),
                accel_raw_callback=lambda e:print('ACCE:',e))
    except KeyboardInterrupt:
        band.stop_realtime()

band.disconnect()
