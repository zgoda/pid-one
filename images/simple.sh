set -euo pipefail

cnt=$(buildah from "docker.io/library/python:3.8-slim-buster")

buildah copy ${cnt} src/mypid.py /
buildah copy ${cnt} scripts/entrypoint-simple.sh /

buildah config --cmd '[ "/entrypoint-simple.sh", "mypid.py" ]' ${cnt}

buildah commit --rm ${cnt} "quay.io/zgoda/test"
