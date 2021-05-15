#!/usr/bin/env bash

process_name=$1

for pid in $(pidof $process_name); do
renice 19 $pid;
done
