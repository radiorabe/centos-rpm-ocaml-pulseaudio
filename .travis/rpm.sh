#!/bin/bash
#
# RPM build wrapper for ocaml-pulseaudio, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"

dnf config-manager --set-disabled epel

chown root:root ocaml-pulseaudio.spec

build-rpm-package.sh ocaml-pulseaudio.spec
