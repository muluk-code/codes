#!/bin/bash


echo "Direcciones Encontradas"
salida= ifconfig |grep 'Direc. inet'
echo $salida
echo "Dispositivos"
macd= ifconfig |grep 'Link encap'
echo $macd
