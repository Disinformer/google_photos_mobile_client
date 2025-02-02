#### Forked from original repo https://github.com/xob0t/gphotos_mobile_client

## Added features:
- Argument `--path` now is optional and may be provided by env `SOURCE_PATH`
- Use argument `--run-in-loop` to watch for source path in cycle.
- Use argument `--attempt-timeout` or env `ATTEMPT_TIMEOUT` to set interval in seconds between path processing. Default value is 30

## Install with git and pip:

```bash
pip install git+https://github.com/Disinformer/gphotos_mobile_client@feat/run-in-loop
```

---
## Docker usage
Main target of this fork is use this app as background process.
Now it's possible to run app in docker container. For more convenient management `docker-compose` is preferred.

Example of docker compose file: ``docker-compose.yml``
```shell
services:
  gp-uploader:
    container_name: gp-uploader
    restart: always
    image: disinformer/google-photos-unlim-uploader:latest
    environment:
      GP_AUTH_DATA: <your google credential string intercepted by HTTPToolKit>
      SOURCE_PATH: /media_to_upload
      ATTEMPT_TIMEOUT: 60
    volumes:
      - <source path to your files>:/media_to_upload
    entrypoint:
      - gp-upload 
      - --run-in-loop
      - --recursive
      - --delete-from-host
```
_Attention!_ Remove last line (`--delete-from-host`) if you do not want to delete source files. 

To run attached: `docker-compose up`
To run in background: `docker-compose -d up`
To stop: `docker-compose stop`
To stop and remove containers: `docker-compose down`


You may upload to more than one account in parallel. Config services in a single `docker-compose.yml`:
```shell
services:
  gp-uploader-1:
    container_name: gp-uploader-account-one
    restart: always
    image: disinformer/google-photos-unlim-uploader:latest
    environment:
      GP_AUTH_DATA: <google account one credential>
      SOURCE_PATH: /media_to_upload
      ATTEMPT_TIMEOUT: 60
    volumes:
      - <path for account one>:/media_to_upload
    entrypoint:
      - gp-upload 
      - --run-in-loop
      - --recursive
      
  gp-uploader-2:
    container_name: gp-uploader-account-two
    restart: always
    image: disinformer/google-photos-unlim-uploader:latest
    environment:
      GP_AUTH_DATA: <google account two credential>
      SOURCE_PATH: /media_to_upload
      ATTEMPT_TIMEOUT: 60
    volumes:
      - <path for account two>:/media_to_upload
    entrypoint:
      - gp-upload 
      - --run-in-loop
      - --recursive
```
Or use separate files with content from the first example: `docker-compose-one.yml` & `docker-compose-two.yml`
To run independently add `-f` and `-p`: `docker-compose -f docker-compose-one.yaml -p one up`



---
For other details about client application follow to original repo https://github.com/xob0t/gphotos_mobile_client

