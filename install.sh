#!/bin/bash
LOGDIR=/var/log/hitchhiker
DIRPATH=$(dirname "$(readlink -f "$0")")
CRONTAB_FILE="$DIRPATH/hitchhiker.cron"

function main() {
    user=`whoami`
    echo "Creating log dir at $LOGDIR"
    sudo mkdir -p "$LOGDIR"
    sudo chown $user "$LOGDIR"
    echo "Installing crontab from $CRONTAB_FILE"
    crontab -u $user "$CRONTAB_FILE"
    echo 'Done!'
}

main
