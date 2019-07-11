# Docker Volume Utilisation

This script checks the utilisation of Docker Volumes created via vSphere Storage and outputs details in JSON for use with telegraf

Ross A. Stewart - July 2019

## Configuration

Set the name of the vSphere datastore the Docker volumes reside on in the variables and configuration section of the script.

The script must be run with root privaleges, this can be achieved on systems which utilise sudo by adding the following line to /etc/sudoers

            telegraf ALL=(root) NOPASSWD: /etc/telegraf/scripts/docker-vol-usage.py

Enable collection of metrics with telegraf by adding the following to telegraf.conf

            # Docker volume utilisation
            [[inputs.exec]]
              commands = [ "sudo /etc/telegraf/scripts/docker-vol-usage.py" ]
              timeout = "5s"
              name_override = "docker_volumes"
              name_suffix = ""
              data_format = "json"
              tag_keys = [ "volume_name" ]
