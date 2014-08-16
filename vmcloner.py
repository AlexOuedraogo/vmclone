__author__ = 'Alex Ouedraogo'
#!/bin/python
import os, sys
import time

#variables
src_vm='/var/lib/libvirt/images/webtst.example.net.img'
dst_dir='/var/lib/libvirt/images/'
new_vm='webtst2.example.net.img'
domain='webtst.example.net'
mount_src_dir="/dev/mapper/"
mount_src_vol="vg_web001-LogVol00"
src_vm_ip='192.168.2.105'
mount_point="/mnt"
new_vm_ip='192.168.2.150'
path_to_ip='/etc/sysconfig/network/ifcfg-eth0'

# commands
cmd_sus="virsh suspend "+domain
cmd_res="virsh resume "+domain
#cmd_cop="rsync -avz " +src_vm+" "+dst_dir+ " "+new_vm
cmd_map="kpartx -a " +dst_dir+new_vm
cmd_umount="umount " +mount_point+ "> /dev/null 2>&1"
cmd_mount="mount "+mount_src_dir+mount_src_vol+" "+mount_point
cmd_set_ip="sed -i -e 's/"+src_vm_ip+"/"+new_vm_ip+ " "+path_to_ip
# suspend template OS while cloning
os.system(cmd_sus)
#os.system(cmd_cop)
time.sleep(5)
os.system(cmd_res)
os.system(cmd_map)
os.system(cmd_umount)
os.system(cmd_mount)

