#!/usr/bin/python
# coding=utf-8
# zhangrj http://www.icoder.top/

import os
import json

# Disk Discovery
disk_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getdisk|grep -E 'Bus.*Enclosure.*Disk'").read().splitlines()
disk_dic_list = []

for diskname in disk_list:
	disk_dic = {}
	disk_dic['{#DISKNAME}'] = diskname
	disk_dic_list.append(disk_dic)

disk_json = json.dumps(disk_dic_list, separators=(',', ':'))

diskjson_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_disk_discovery -o '" + disk_json + "'"
os.system(diskjson_cmd)

# Power Discovery
powerA_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -vsca|grep -Eo 'Bus.*Enclosure.*Power.*State'").read().splitlines()
powerB_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -vscb|grep -Eo 'Bus.*Enclosure.*Power.*State'").read().splitlines()
power_list = powerA_list + powerB_list
power_dic_list = []

for powername in power_list:
	power_dic = {}
	power_dic['{#POWERNAME}'] = powername
	power_dic_list.append(power_dic)

power_json = json.dumps(power_dic_list, separators=(',', ':'))

power_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_power_discovery -o '" + power_json + "'"
os.system(power_cmd)

# LCC Discovery
lccA_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -lcca|grep -Eo 'Bus.*Enclosure.*LCC.*State'").read().splitlines()
lccB_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -lccb|grep -Eo 'Bus.*Enclosure.*LCC.*State'").read().splitlines()
lcc_list = lccA_list + lccB_list
lcc_dic_list = []

for lccname in lcc_list:
	lcc_dic = {}
	lcc_dic['{#LCCNAME}'] = lccname
	lcc_dic_list.append(lcc_dic)

lcc_json = json.dumps(lcc_dic_list, separators=(',', ':'))
lcc_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_lcc_discovery -o '" + lcc_json + "'"
os.system(lcc_cmd)

# SP Discovery
spa_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -spa|grep -Eo 'SP.*State'").read().splitlines()
spb_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -spb|grep -Eo 'SP.*State'").read().splitlines()
sp_list = spa_list + spb_list
sp_dic_list = []

for spname in sp_list:
	sp_dic = {}
	sp_dic['{#SPNAME}'] = spname
	sp_dic_list.append(sp_dic)

sp_json = json.dumps(sp_dic_list, separators=(',', ':'))
sp_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_sp_discovery -o '" + sp_json + "'"
os.system(sp_cmd)

# SPS Discovery
spsa_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -spsa|grep -Eo 'Bus.*Enclosure.*SPS.*State'").read().splitlines()
spsb_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -spsb|grep -Eo 'Bus.*Enclosure.*SPS.*State'").read().splitlines()
sps_list = spsa_list + spsb_list
sps_dic_list = []

for spsname in sps_list:
	sps_dic = {}
	sps_dic['{#SPSNAME}'] = spsname
	sps_dic_list.append(sps_dic)

sps_json = json.dumps(sps_dic_list, separators=(',', ':'))
sps_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_sps_discovery -o '" + sps_json + "'"
os.system(sps_cmd)

# SPS Cable Discovery
spsa_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -cablingspsa|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'").read().splitlines()
spsb_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -cablingspsb|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'").read().splitlines()
sps_cable_list = spsa_cable_list + spsb_cable_list
sps_cable_dic_list = []

for spscable_name in sps_cable_list:
	sps_cable_dic = {}
	sps_cable_dic['{#SPSCABLENAME}'] = spscable_name
	sps_cable_dic_list.append(sps_cable_dic)

sps_cable_json = json.dumps(sps_cable_dic_list, separators=(',', ':'))
sps_cable_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_spscable_discovery -o '" + sps_cable_json + "'"
os.system(sps_cable_cmd)

# CPU Discovery
cpua_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -cpua|grep -Eo 'Bus.*Enclosure.*CPU.*State'").read().splitlines()
cpub_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -cpub|grep -Eo 'Bus.*Enclosure.*CPU.*State'").read().splitlines()
cpu_list = cpua_list + cpub_list
cpu_dic_list = []

for cpu_name in cpu_list:
	cpu_dic = {}
	cpu_dic['{#CPUNAME}'] = cpu_name
	cpu_dic_list.append(cpu_dic)

cpu_json = json.dumps(cpu_dic_list, separators=(',', ':'))
cpu_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_cpu_discovery -o '" + cpu_json + "'"
os.system(cpu_cmd)

# DIMM Discovery
dimma_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -dimma|grep -Eo 'Bus.*Enclosure.*DIMM.*State'").read().splitlines()
dimmb_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -dimmb|grep -Eo 'Bus.*Enclosure.*DIMM.*State'").read().splitlines()
dimm_list = dimma_list + dimmb_list
dimm_dic_list = []

for dimm_name in dimm_list:
	dimm_dic = {}
	dimm_dic['{#DIMMNAME}'] = dimm_name
	dimm_dic_list.append(dimm_dic)

dimm_json = json.dumps(dimm_dic_list, separators=(',', ':'))
dimm_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_dimm_discovery -o '" + dimm_json + "'"
os.system(dimm_cmd)

# I/O Discovery
ioa_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -ioa|grep -Eo 'Bus.*Enclosure.*I/O.*State'").read().splitlines()
iob_list = os.popen("/opt/Navisphere/bin/naviseccli -h EMC_manage_ip getcrus -iob|grep -Eo 'Bus.*Enclosure.*I/O.*State'").read().splitlines()
io_list = ioa_list + iob_list
io_dic_list = []

for io_name in io_list:
	io_dic = {}
	io_dic['{#IONAME}'] = io_name
	io_dic_list.append(io_dic)

io_json = json.dumps(io_dic_list, separators=(',', ':'))
io_cmd = "/usr/bin/zabbix_sender -z zabbix_server_ip -s EMC_manage_ip -k emc_io_discovery -o '" + io_json + "'"
os.system(io_cmd)