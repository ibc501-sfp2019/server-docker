#! /bin/bash

{
    while :
        do python ./world_code/manage.py snitch_activate
        sleep 5
        done
} &
 