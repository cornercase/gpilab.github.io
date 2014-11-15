#!/bin/bash

INPUT=$1
OUTPUT=$2

rm -f $OUTPUT
stylus -I /opt/local/lib/node_modules/ < $INPUT > $OUTPUT


