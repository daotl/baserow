#!/bin/sh
set -a
source ./.env
set +a

mkdir -p ${VOLUMES_ROOT}/postgres \
         ${VOLUMES_ROOT}/media \
         ${VOLUMES_ROOT}/caddy_data \
         ${VOLUMES_ROOT}/caddy_config
