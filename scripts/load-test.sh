#!/bin/bash

while true
do
  for i in $(seq 1 20)
  do
    curl -s -X POST http://sklearn-iris-predictor-default.default.svc.cluster.local/v1/models/1:predict \
    -H "Content-Type: application/json" \
    -d '{"instances": [[5.1,3.5,1.4,0.2]]}' &
  done
  wait
done
