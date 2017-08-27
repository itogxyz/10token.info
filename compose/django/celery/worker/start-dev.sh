#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

celery -A itogxyz.taskapp worker -l INFO
