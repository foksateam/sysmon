# sysmon
Simple system monitoring

Use this command for pull latest version of sysmon container:
docker push foksateam/sysmon:latest

For execute scripts in container use next parameters:
docker run --pid=host --rm -ti foksateam/sysmon [COMMAND]

Available options:
 cpuinfo - this parameter show cpu times info \n
 memifo - this parameter show memory info \n
 swapinfo - this parameter show swap info \n
 procinfo - this parameter show running procesess in host system\n
 help - use this for show this menu\n

Additianal:
--rm - use this option for delete container after execute script in container
--pid=host - use this if you want to see processes running on host system within container

Also if you want you can build container using Dockerfile, for in push all files from this repository into one folder an run command:
docker build -t <Container name> .
and then run container with parameters listed above
