#! /bin/bash

set -euo pipefail

cnt=$(buildah from "docker.io/library/python:3.8-slim-buster")

buildah copy -q ${cnt} src/mypid.py /
buildah copy -q ${cnt} scripts/entrypoint-exec.sh /

buildah config --cmd '[ "/entrypoint-exec.sh", "mypid.py" ]' ${cnt}

buildah commit --rm ${cnt} "quay.io/zgoda/test"
