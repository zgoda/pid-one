#! /bin/bash

set -euo pipefail

cnt=$(buildah from "docker.io/library/python:3.8-slim-buster")

buildah copy ${cnt} src/with_atexit.py /
buildah copy ${cnt} scripts/entrypoint-exec.sh /

buildah config --cmd '[ "/entrypoint-exec.sh", "/with_atexit.py" ]' ${cnt}

buildah commit --rm ${cnt} "quay.io/zgoda/test"
