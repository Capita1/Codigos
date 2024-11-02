#!/bin/bash
while :; do
	text="$(playerctl metadata --format " 󰐎 {{ artist }} - {{ title }} - {{ album }}")󰝤"
	for (( i = 0; i < "${#text}"; i++ )); do
		printf "\r%s" "${text:$i:15}"
		sleep 0.2
	done
done