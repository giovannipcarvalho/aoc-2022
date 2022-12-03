#!/usr/bin/env bash

# usage: ./download.sh 1
# downloads input for day 1 as `input.txt` in the current folder
# SESSION environment variable must be set to the advent of code session cookie

set -eu

. ../.env

curl \
	-A "giovannipcarvalho via curl" \
	-H "cookie: session=${SESSION}" \
	-sSLo input.txt \
	https://adventofcode.com/2022/day/$1/input
