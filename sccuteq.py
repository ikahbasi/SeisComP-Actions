from obspy import UTCDateTime as utc
import time
import Config
import os

cfg = Config.cutout()

EventID = '2023abcd'
flag = '1'

otime = utc('2023-01-01')
now = utc()

if (now-otime) < cfg.etime:
    sleep = cfg.etime - (now-otime)
    time.sleep(sleep)

stime = otime + cfg.stime
etime = otime + cfg.etime

stime = stime.strftime("%Y-%m-%d %H:%M:%S")
etime = etime.strftime("%Y-%m-%d %H:%M:%S")

os.makedirs(cfg.outpath, exist_ok=True)

if flag == '1':
    for network in cfg.networks:
        print(network)
        output_file = f'{cfg.outpath}/{EventID}_{network}.mseed'
        command = f'scart -dsvE -n {network} -t "{stime}~{etime}" {cfg.archive} > {output_file}'
        os.system(command)