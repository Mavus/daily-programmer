#!/bin/bash
grep -v 'status.sh' $(ls ./*) | grep --color=auto 'TODO'
