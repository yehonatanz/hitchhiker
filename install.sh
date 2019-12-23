#!/bin/bash
LOGDIR=/var/log/hitchhiker
DIRPATH=$(dirname "$(readlink -f "$0")")
CRONTAB_FILE="$DIRPATH/hitchhiker.cron"

function main() {
    uid=`id -u`
    echo "Creating log dir at $LOGDIR"
    sudo mkdir -p "$LOGDIR"
    sudo chown $uid "$LOGDIR"
    echo "Installing crontab from $CRONTAB_FILE"
    crontab -u $uid "$CRONTAB_FILE"
    echo 'Done!'
}

main
