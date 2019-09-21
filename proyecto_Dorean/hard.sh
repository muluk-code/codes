#!/bin/bash
echo "Informacion de Hardware:"
echo "Memoria:"
salida= cat /proc/meminfo | grep 'MemTotal:'
echo $salida
salida= cat /proc/meminfo | grep 'MemFree:'
echo $salida
salida= cat /proc/meminfo | grep 'MemAvailable:'
echo $salida
salida= cat /proc/meminfo | grep 'Active:'
echo $salida
salida= cat /proc/meminfo | grep 'Inactive:'
echo $salida
salida= cat /proc/meminfo | grep 'Cached:'
echo $salida
echo "SWAP:"
salida= cat /proc/meminfo | grep 'SwapTotal:'
echo $salida
salida= cat /proc/meminfo | grep 'SwapCached:'
echo $salida
salida= cat /proc/meminfo | grep 'SwapFree:'
echo $salida
echo "Procesador:"
salida= cat /proc/cpuinfo | grep 'model name'
echo $salida
salida= cat /proc/cpuinfo | grep 'cpu MHz'
echo $salida
salida= cat /proc/cpuinfo | grep 'cache size'
echo $salida
salida= cat /proc/cpuinfo | grep 'cpu cores'
echo $salida
echo "Particiones Montadas"
salida= df -h
echo salida