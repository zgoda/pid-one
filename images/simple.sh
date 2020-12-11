set -euo pipefail

cnt=$(buildah from "docker.io/library/python:3.8-slim-buster")

buildah copy -q ${cnt} src/mypid.py /
buildah copy -q ${cnt} scripts/entrypoint-simple.sh /

buildah config --cmd '[ "/entrypoint-simple.sh", "mypid.py" ]' ${cnt}

buildah commit -q --rm ${cnt} "quay.io/zgoda/test"
