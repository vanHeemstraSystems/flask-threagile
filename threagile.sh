#!/bin/bash
sudo chmod a+rwx -R "$(pwd)"
docker run -it -v "$(pwd)":/app/work threagile/threagile "$@" /bin/bash
