#!/bin/bash

virt-install --connect qemu:///system --virt-type kvm --name Odin \

--location=#/pathfile/iso \

--os-variant # os \

--disk size=200 --memory=1024 \ #lenth disk & memory

--graphics none \

--console pty,target_type=seriel \

--extra-args="console=ttys0" --debug