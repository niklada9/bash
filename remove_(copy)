#!/bin/bash

for file in *; do
  if [[ "$file" == *копия* ]]; then
    mv -- "$file" "${file/ \(копия\)/_1}"
  fi
done

