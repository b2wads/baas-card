#!/usr/bin/env bash

project_name="card"

docker build -t registry.pe.hmg.asgard.b2w.io/baas/${project_name} . \
&& docker push registry.pe.hmg.asgard.b2w.io/baas/${project_name}
