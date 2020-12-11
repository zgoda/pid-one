#! /bin/bash

set -euo pipefail

name="cnt1"

podman run --rm -ti --name ${name} "quay.io/zgoda/test"
