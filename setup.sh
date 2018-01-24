#!/bin/sh

sudo pip3 install pygeoip

wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz

gunzip GeoLiteCity.dat.gz

