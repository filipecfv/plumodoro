# Plumodoro

A light command line pomodoro with statistics

## "Installation"
- `git clone https://github.com/filipecfv/plumodoro`
- `pip install -r requirements.txt`
- `echo export PATH=$PATH:$(pwd)/src >> ~/.bashrc`

## Basic Usage
### Plumodoro

```
usage: plumodoro [-h] [-w] [-s] [-l]

A simple command line pomodoro

options:
  -h, --help            show this help message and exit
  -w, --work-time   Duration of work periods, in minutes (default: 25)
  -s, --short-rest  Duration of short rests, in minutes (default: 5)
  -l, --long-rest   Duration of long rests, in minutes (default: 15)

```

### Plumodoro-stats

```
usage: plumodoro-stats [-h] <subcommand> ...

Display statistics from plumodoro

positional arguments:
  <subcommand>
    table       Print a table with statistics
    plot        Plot a graph with statistics
    clear       Clear history file

options:
  -h, --help    show this help message and exit

```

#### Plumodoro-stats table

```
- Plumodoro-stats table
usage: plumodoro-stats table [-h] [-w]

options:
  -h, --help        show this help message and exit
  -w, --within  how many days within to print the table
```

- Example: 

```
$ plumodoro-stats table -w 5

Plumodoro table from within the last 5 days:
      Date  Pomodoros Work Hours
2023-04-29          1      01:30
2023-04-30          3      01:12
2023-05-01          5      02:00
2023-05-02          4      01:36
2023-05-03          0      00:00
```

#### Plumodoro-stats plot

```
usage: plumodoro-stats plot [-h] [-w]

options:
  -h, --help        show this help message and exit
  -w, --within  how many days within to plot the statistics
```

- Example `$ plumodoro-stats plot -w 6`

![](/demo/plumodoro_plot.png)
