#!/bin/bash

echo "Waiting Postgres to launch on 5432..."

while ! nc -z db 5432; do   
    sleep 1
  done

  echo "Postgres launched"