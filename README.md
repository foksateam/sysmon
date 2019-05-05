# sysmon
## Simple system monitoring

## Using Docker Hub
Use this command for pull latest version of sysmon container:
```JS
docker push foksateam/sysmon:latest
```

For execute scripts in container use next parameters:
```JS
docker run --pid=host --rm -ti foksateam/sysmon [COMMAND]
```

Available [COMMAND] options:
* cpuinfo - this parameter show cpu times info
* memifo - this parameter show memory info
* swapinfo - this parameter show swap info
* procinfo - this parameter show running procesess in host system
* help - use this for show this menu 

### Additianal:
* --rm - use this option for delete container after execute script in container
* --pid=host - use this if you want to see processes running on host system within container

## Build from Dockerfile
Also if you want you can build container using Dockerfile, for in push all files from this repository into one folder an run command:
```JS
docker build -t <Container name> .
```
and then run container with parameters listed above
