# resmon-sensor
Repository for a sensor component, which is part of resmon product. 
This application can work on Linux and Windows.

**Info!** All path existing in this file are considered 
as being used in project/install root directory.

# Usage

## on Linux
```bash
./resmon-sensor [-h|--help] [-a|--address ADDRESS] [-i|--interval INTERVAL] [-b|--buffer BUFFER] [-n|--name NAME]
```
Options are descriped in [this sectionk](#options)

## on Windows
You can run this application by executing the following command:
```bash
python ./src/main.py [-h|--help] [-a|--address ADDRESS] [-i|--interval INTERVAL] [-b|--buffer BUFFER] [-n|--name NAME]
```
Options are descriped in [this sectionk](#options)

## Options
| Option                                       | Default value | Description                                       |
| ---------------------------------------------|:-------------:| -------------------------------------------------:|
| **-h**, **--help**                           | ---           | show help message and exit the application        |
| **-a _ADDRESS_**, **--address _ADDRESS_**    | ---           | Full server address with protocol and port        |
| **-i _INTERVAL_**, **--interval _INTERWAL_** | ---           | Measurement interval [sec]                        |
| **-b _BUFFER_**, **--buffer _BUFFER_**       | 10            | Messages buffer size                              |
| **-n _NAME_**, **--name _NAME_**             | ---           | User friendly identifier                          |

#Instalation

## on Linux
We provide single file `install-sensor.sh` which is used to install this application. It's enough that you just run it as following:
```bash
./install-sensor.sh [--quiet]
```
Later you have to accept unpacking files. It's automatically accepted if you choose option _--quiet_.
Application will be installed in the same place where script `install-sensor.sh`

## on Windows
1. Install Python 3.6
2. Install `pip` tool for Python in that version
3. Execute following command:
```bash
python -m pip install --trusted-host pypi.python.org --no-cache-dir -r requirements --user
```

#For developers

You can run some scripts to make your developing process faster and more comfortable.
All scripts can be executed in this way:
```bash
./scripts.sh SCRIPT_NAME
```
where `SCRIPT_NAME` can be as following:
* `build` - it prepares file _install-sensor.sh_ to use it later for installing this application
* `docgen` - it generates documentation and puts it into _./docs/_ directory
* `runtest` - it runs all tests available for this project

**Info!** If you need to use environment file manually, 
it is located in `./data` directory.

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