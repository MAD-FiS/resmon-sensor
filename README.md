# resmon-sensor
Repository for a sensor component, which is part of resmon product.

# Usage

```bash
./resmon-sensor [-h] [-c CONFIG] [-l LIMIT] [--register] [-v]
```

### Options
| Option                                       | Default value | Description                                       |
| ---------------------------------------------|:-------------:| -------------------------------------------------:|
| **-h**, **--help**                           | ---           | show help message and exit the application        |
| **-a _ADDRESS_**, **--address _ADDRESS_**    | ---           | Full server address with protocol and port        |
| **-i _INTERVAL_**, **--interval _INTERWAL_** | ---           | Measurement interval [sec]                        |
| **-b _BUFFER_**, **--buffer _BUFFER_**       | 10            | Messages buffer size                              |
| **-n _NAME_**, **--name _NAME_**             | ---           | User friendly identifier                          |

#Instalation
We provide single file `install.sh` which is used to install this application. It's enough that you just run it as following:
```bash
./install.sh [--quiet]
```
Later you have to accept unpacking files. It's automatically accepted if you choose option _--quiet_.
Application will be installed in the same place where script `install.sh`

#For developers

You can run some scripts to make your developing process faster and more comfortable.
All scripts can be executed in this way:
```bash
./scripts.sh SCRIPT_NAME
```
where `SCRIPT_NAME` can be as following:
* `build` - it prepares file _install.sh_ to use it later for installing this application
* `docgen` - it generates documentation and puts it into _./docs/_ directory
* `runtest` - it runs all tests available for this project

## Deployment on Docker
You can develop this application on [Docker](https://docs.docker.com). It can be used to testing it in a clear environment. 
At start you can make yourself sure that the file `install.sh` is created by _build_ script.

Then you can execute these two following commands:
```bash
docker build -t resmon-sensor .
```
and:
```bash
docker run -it resmon-sensor
```
Then you can run there this application.
