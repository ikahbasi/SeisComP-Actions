from obspy import UTCDateTime as utc
import time
import Config
import os

cfg = Config.cutout()


otime = utc('2023-01-01')
now = utc()

if (now-otime) < cfg.etime:
    sleep = cfg.etime - (now-otime)
    time.sleep(sleep)

stime = otime + cfg.stime
etime = otime + cfg.etime



if flag == '1':
    for network in cfg.networks:
        print(network)
        output_file = f'{cfg.output}/{EventID}_{network}.mseed'
        command = f'scart -dsvE -n {network} -t "{STA_time}~{END_time}" {cfg.archive} > {output_file}'
        os.system(command)