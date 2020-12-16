#!/bin/bash
mkdir /opt/ipnb3/share/jupyter/kernels/pyspark
cp /vagrant/helpers/kernel.json /opt/ipnb3/share/jupyter/kernels/pyspark/
cp /opt/spark/kernel-icons/pyspark-icon-64x64.png /opt/ipnb3/share/jupyter/kernels/pyspark/
cp /opt/spark/kernel-icons/pyspark-icon-32x32.png /opt/ipnb3/share/jupyter/kernels/pyspark/
