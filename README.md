# resmon-sensor
Repository for a sensor component, which is part of ResMon software.
This application can work on Linux, Windows and Mac OS (in a similar way like on Linux).

**Info!** All path existing in this file are considered 
as being used in project/install root directory.

# Usage linux

## on Linux
```bash
./resmon-sensor [-h|--help] [-a|--address ADDRESS] [-i|--interval INTERVAL] [-b|--buffer BUFFER] [-n|--name NAME]
```
Options are described in [this section](#options)

## on Windows
You can run this application by executing the following command:
```bash
resmon-sensor-win [-h|--help] [-a|--address ADDRESS] [-i|--interval INTERVAL] [-b|--buffer BUFFER] [-n|--name NAME]
```
Options are described in [this section](#options)

## Options
| Option                                       | Default value | Description                                       |
| ---------------------------------------------|:-------------:| -------------------------------------------------:|
| **-h**, **--help**                           | ---           | show help message and exit the application        |
| **-a _ADDRESS_**, **--address _ADDRESS_**    | ---           | Full server address with protocol and port        |
| **-i _INTERVAL_**, **--interval _INTERWAL_** | ---           | Measurement interval [sec]                        |
| **-b _BUFFER_**, **--buffer _BUFFER_**       | 10            | Messages buffer size                              |
| **-n _NAME_**, **--name _NAME_**             | ---           | User friendly identifier                          |

# Instalation

## on Linux

We provide single file `install-sensor.sh` which is used to install this application. 
It's enough that you just run it as following:
```bash
./install-sensor.sh [--quiet]
```
Later you have to accept unpacking files. It's automatically accepted if you choose option _--quiet_.
Application will be installed in the same place where script `install-sensor.sh`

## on Windows

We are assuming that python (3.5 or later) and pip are already installed. 
It's enough that you just run the file `install-win.bat` which is provided by us:
```cmd
install-win [--quiet]
```
 
# For developers

**Info!** This instruction is written for developers who use Linux operating system.

You have to clone this repository. Then you can work with it and develop the application.
If you want to run it locally for testing, it doesn't need to create installer `install-sensor.sh` 

## Scripts

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
You can develop this application on [Docker](https://docs.docker.com). 
It can be used to testing it in a clear environment. 
At start you can make yourself sure that the file `install-sensor.sh` 
is created by _build_ script and that it has been executed 
after last changes in your code.

Then you can execute these two following commands:
```bash
docker build -t resmon-sensor .
```
and:
```bash
docker run -it resmon-sensor
```
Then you can run there this application.