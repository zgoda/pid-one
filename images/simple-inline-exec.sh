set -euo pipefail

cnt=$(buildah from "docker.io/library/python:3.8-slim-buster")

buildah copy ${cnt} src/mypid.py /

buildah config --cmd '[ "/usr/local/bin/python3", "/mypid.py" ]' ${cnt}

buildah commit --rm ${cnt} "quay.io/zgoda/test"
