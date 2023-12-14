🔖 [Table of Contents](README.md)

<div align="center">
  <img src="_images/emoji/checkered_flag.png">
  <p>
    <sub>
      Let's get started
    </sub>
  </p>
</div>

# Getting Started

Welcome to Zrb's getting started guide. We will cover everything you need to know to work with Zrb. In this Getting Started Guide, you will learn about:

- [Installing Zrb](#installing-zrb)
- [Running a Task](#running-a-task)
  - [How Tasks are Organized](#how-tasks-are-organized)
  - [Getting Available Tasks/Task Groups](#getting-available-taskstask-groups)
  - [Using Interactive Mode](#using-interactive-mode)
- [Creating a Project](#creating-a-project)
  - [Using `project.sh`](#using-projectsh)
- [Creating a Task](#creating-a-task)
  - [Scaffolding a Task](#scaffolding-a-task)
  - [Updating Task definition](#updating-task-definition)
- [Understanding The Code](#understanding-the-code)
    - [Task Definition](#task-definition)
      - [Creating a Task Using Task Classes](#creating-a-task-using-task-classes)
      - [Creating a Task Using Python Decorator](#creating-a-task-using-python-decorator)
      - [Task Parameters](#task-parameters)
    - [Task Dependencies](#task-dependencies)
    - [Task Inputs](#task-inputs)
    - [Task Environments](#task-environments)
    - [Switching Environment](#switching-environment)
- [Creating a Long-Running Task](#creating-a-long-running-task)

This guide assumes you have some familiarity with CLI and Python.

# Installing Zrb

<div align="center">
  <img src="_images/emoji/wrench.png">
  <p>
    <sub>
      Installation: Let's put this into your machine.
    </sub>
  </p>
</div>

Before working with Zrb, you must ensure you have Zrb installed on your system.

If you are working on a new computer, the following command will help you install Zrb and Pyenv:

```bash
# On a new computer
curl https://raw.githubusercontent.com/state-alchemists/zrb/main/install.sh | bash
```

If you already have your own Python Ecosystem (i.e., [Pyenv](https://github.com/pyenv/pyenv), [Conda](https://docs.conda.io/en/latest), or Venv), you can install Zrb as a Python package using the Pip command.

```bash
# On a computer with its own Python ecosystem.
pip install zrb
```

Alternatively, you can also install Zrb as a container. Please see the [installation guide](./installation.md) for more detailed instructions.


# Running a Task


<div align="center">
  <img src="_images/emoji/runner.png">
  <p>
    <sub>
      <a href="https://www.youtube.com/watch?v=2wVPyo_hnWw" target="blank">Run! run! run!</a>
    </sub>
  </p>
</div>

Zrb comes with some built-in task definitions. To run a Zrb task, you need to follow the following pattern:

```bash
zrb [task-groups...] <task-name> [task-parameters...]
```

Let's see the following example:

```bash
 zrb base64 encode --text "non-credential-string"
       │      │    └──────────────┬─────────────┘                            
       │      │                   │ 
       ▼      │                   ▼
   task-group │            task-parameter
              │
              ▼
          task-name
```

You will see how Zrb encoded `non-credential-string` into `bm9uLWNyZWRlbnRpYWwtc3RyaW5n`.

```
Support zrb growth and development!
☕ Donate at: https://stalchmst.com/donation
🐙 Submit issues/PR at: https://github.com/state-alchemists/zrb
🐤 Follow us at: https://twitter.com/zarubastalchmst
🤖 ○ ◷ 2023-11-10 09:08:33.183 ❁ 35276 → 1/1 🍎    zrb base64 encode • Completed in 0.051436424255371094 seconds
bm9uLWNyZWRlbnRpYWwtc3RyaW5n
To run again: zrb base64 encode --text "non-credential-string"
```

Like any CLI program, when you run a Zrb task, you get two kinds of outputs:

- `Standard Error (stdout)`: Contains logs, error messages, and other information.
- `Standard Output (stderr)`: Contains the output of the program.

In our previous example, Zrb will put `bm9uLWNyZWRlbnRpYWwtc3RyaW5n` into `Standard Output` and everything else into `Standard Error`. You will need this information if you want to [integrate Zrb with other tools](tutorials/integration-with-other-tools.md)

> __⚠️ WARNING:__ Base64 is a encoding algorithm that allows you to transform any characters into an alphabet which consists of Latin letters, digits, plus, and slash.
>
> Anyone can easily decode a base64-encoded string. __Never use it to encrypt your password or any important credentials!__

## How Tasks are Organized

<div align="center">
  <img src="_images/emoji/file_cabinet.png">
  <p>
    <sub>
      Put related Tasks under the same Group for better discoverability.
    </sub>
  </p>
</div>

Hierarchically speaking, you can think of Task Groups as directories and Tasks as files.

That means that a Task Group might contain:

- Other Task Groups
- One or more Tasks

```
zrb
├── base64
│   ├── decode
│   └── encode
├── devtool
│   ├── install
│   │   ├── aws
│   │   ├── docker
│   │   ├── gcloud
│   │   ├── ...
│   │   └── zsh
├── env
│   └── get
├── eval
├── explain
│   ├── dry-principle
│   ├── kiss-principle
│   ├── solid-principle
│   ├── ...
│   └── zen-of-python
├── git
├── ...
└── watch-changes
```

When you type `zrb` in your terminal, you will see top-level Tasks and Task Groups. You can then type the Task Group or the Task until you find what you need.

Let's try it.

```bash
zrb
```

```
Usage: zrb [OPTIONS] COMMAND [ARGS]...

                bb
   zzzzz rr rr  bb
     zz  rrr  r bbbbbb
    zz   rr     bb   bb
   zzzzz rr     bbbbbb   0.1.0
   _ _ . .  . _ .  _ . . .

Super framework for your super app.

☕ Donate at: https://stalchmst.com/donation
🐙 Submit issues/PR at: https://github.com/state-alchemists/zrb
🐤 Follow us at: https://twitter.com/zarubastalchmst

Options:
  --help  Show this message and exit.

Commands:
  base64         Base64 operations
  coba           coba
  devtool        Developer tools management
  env            Environment variable management
  eval           Evaluate Python expression
  explain        Explain things
  git            Git related commands
  md5            MD5 operations
  process        Process related commands
  project        Project management
  say            Say anything, https://www.youtube.com/watch?v=MbPr1oHO4Hw
  schedule       Show message/run command periodically
  ubuntu         Ubuntu related commands
  update         Update zrb
  version        Get Zrb version
  watch-changes  Watch changes and show message/run command
```

You see that Zrb has many Tasks and Task Groups. Now, let's take a look at `base64` Group.

```bash
zrb base64
```

```
Usage: zrb base64 [OPTIONS] COMMAND [ARGS]...

  Base64 operations

Options:
  --help  Show this message and exit.

Commands:
  decode  Decode a base64 encoded text
  encode  Encode a text using base64 algorithm
```

You will find two tasks (i.e., `decode` and `encode`) under the `base64` group.

## Using Interactive Mode

<div align="center">
  <img src="_images/emoji/speech_balloon.png">
  <p>
    <sub>
      Most life issues are just communication problems in disguise.
    </sub>
  </p>
</div>

You have seen how you can set the Task Parameters by using CLI options as follows:

```bash
zrb base64 encode --text "non-credential-string"
```

The CLI Options are optional. You can run the task without specifying the options. When you do so, Zrb will activate the interactive mode so that you can supply the parameter values on the run.

Let's try it.

```bash
zrb base64 encode
```

```
Text []: non-credential-string
Support zrb growth and development!
☕ Donate at: https://stalchmst.com/donation
🐙 Submit issues/PR at: https://github.com/state-alchemists/zrb
🐤 Follow us at: https://twitter.com/zarubastalchmst
🤖 ○ ◷ 2023-11-10 09:10:58.805 ❁ 35867 → 1/1 🍈    zrb base64 encode • Completed in 0.053427934646606445 seconds
bm9uLWNyZWRlbnRpYWwtc3RyaW5n
To run again: zrb base64 encode --text "non-credential-string"
```

> __📝 NOTE:__ You can disable the interactive mode by setting `ZRB_SHOW_PROMPT` to `0` or `false`. Please refer to [configuration section](./configurations.md) for more information.
>
> When prompts are disabled, Zrb will automatically use task-parameter's default values.

That's it. That's all you need to know to work with Zrb.

In the rest of this section, you will learn about Zrb project and how to make your own Zrb Tasks.

# Creating a project

<div align="center">
  <img src="_images/emoji/building_construction.png">
  <p>
    <sub>
      A project is like a fridge light; it only works when you open it to check.
    </sub>
  </p>
</div>

You probably want to organize your jobs under multiple projects to keep them separated.

At its basic, a project is a directory containing a single file named `zrb_init.py`. This setup is probably sufficient for a simple hello-world project.

To make something more than a simple hello-world, you better use `zrb project create` command.

```bash
zrb project create --project-dir my-project --project-name my-project
```

Once invoked, you will see a project named `my-project`. Let's see what this project looks like:

```bash
cd my-project
ls -al
```

```
total 52
drwxr-xr-x  6 gofrendi gofrendi 4096 Nov 12 07:52 .
drwxr-xr-x 14 gofrendi gofrendi 4096 Nov 12 07:52 ..
drwxr-xr-x  7 gofrendi gofrendi 4096 Nov 12 07:52 .git
drwxr-xr-x  3 gofrendi gofrendi 4096 Nov 12 07:52 .github
-rw-r--r--  1 gofrendi gofrendi   27 Nov 12 07:52 .gitignore
-rw-r--r--  1 gofrendi gofrendi    7 Nov 12 07:52 .python-version
-rw-r--r--  1 gofrendi gofrendi 1937 Nov 12 07:52 README.md
drwxr-xr-x  3 gofrendi gofrendi 4096 Nov 12 07:52 _automate
-rwxr-xr-x  1 gofrendi gofrendi 1507 Nov 12 07:52 project.sh
-rw-r--r--  1 gofrendi gofrendi   13 Nov 12 07:52 requirements.txt
drwxr-xr-x  2 gofrendi gofrendi 4096 Nov 12 07:52 src
-rw-r--r--  1 gofrendi gofrendi  118 Nov 12 07:52 template.env
-rw-r--r--  1 gofrendi gofrendi   54 Nov 12 07:52 zrb_init.py
```

Every Zrb project has a file named `zrb_init.py` under the top-level directory. This file is your entry point to define your Task definitions.

By convention, a project usually contains two sub-directories:

- ___automate__: This folder contains all your automation scripts and task definitions
- __src__: This folder contains all your resources like Docker compose file, helm charts, and source code.

Moreover, Zrb provides some built-in Tasks under `project` Task Group. As always, you can invoke `zrb project` to see those tasks.

## Using `project.sh`

When you create a project using `zrb project create` command, you will find a file named `project.sh`. This script file helps you to load the virtual environment, install requirements, and activate shell completion.

To use the script, you need to invoke the following command:

```bash
source project.sh
```

Anytime you start working on your project, you should load `project.sh`.

# Creating a Task

<div align="center">
  <img src="_images/emoji/clipboard.png">
  <p>
    <sub>
      Finishing a task: 10% skill, 90% not getting distracted by the internet.
    </sub>
  </p>
</div>

Tasks are your most negligible unit of job definition.

Zrb has multiple Task Types, including `CmdTask`, `python_task`, `DockerComposeTask`, `RecurringTask`, `ResourceMaker`, etc.

Typically, a Zrb Task has multiple settings:

- Retry mechanism
- Task Upstreams
- Task Environment and Environment File
- Task Input/Parameter 
- Readiness Checker

In this Getting-Started tutorial, we will only cover a few Task Types.

## Use Case

Let's start with a use case:

- We want to serve a single HTML file
- The HTML file contains some information from environment variables and user inputs.
- Zrb should generate the HTML file based on a single HTML template.
- Whenever the HTML template is modified, Zrb should re-generate the HTML file.

We can break down the requirements into some tasks.

```
        🥬                      🧑‍🍳               🥗
Prepare Resources ────► Monitor and Rebuild ────► Serve
```

## Implementation





---

A Task is the smallest unit of job definition. You can link your tasks together to form a more complex workflow.

Zrb has a powerful command to create tasks under a project. Let's re-create the tasks we make in our [README.md](../README.md).

The goal of the tasks is to download any public CSV dataset and provide the statistical properties of the dataset. To do that, you need to:

- Ensure that you have Pandas installed on your machine
- Ensure that you have downloaded the dataset
- Run the Python script to get the statistical properties of the dataset

```
       🐼
Install Pandas ─────┐           📊
                    ├──► Show Statistics
Download Datasets ──┘
       ⬇️
```

## Scaffolding a Task

Zrb has a powerful command to scaffold your project. To do so, you need to invoke the following command:

> __⚠️ WARNING:__ Make sure you have activate your virtual environment, either by invoking `source project.sh` or `source .venv/bin/activate`.

```bash
zrb project add python-task --project-dir "." --task-name "show-stats"
```

Once you invoke the command, Zrb will make a file named `_automate/show_stats.py`

```python
from typing import Any, Mapping
from zrb import Task, python_task, runner
from zrb.builtin.group import project_group

###############################################################################
# Task Definitions
###############################################################################


@python_task(
    name='show-stats',
    description='show stats',
    group=project_group,
    runner=runner
)
async def show_stats(*args: Any, **kwargs: Any) -> Any:
    task: Task = kwargs.get('_task')
    env_map: Mapping[str, str] = task.get_env_map()
    input_map: Mapping[str, str] = task.get_input_map()
    task.print_out(f'Env map: {env_map}')
    task.print_out(f'Input map: {input_map}')
    return 'ok'
```

We will modify the task later to match our use case, but first let's check on `zrb_init.py`. You will notice how Zrb automatically imports `_automate/show_stats.py` into `zrb_init.py`.

```python
import _automate._project as _project
import _automate.show_stats as show_stats
assert _project
assert show_stats
```

This modification allows Zrb to load `show-stats` so that you can access it from the CLI

```
zrb project show-stats
```

## Updating Task Definition

To make sure things work flawlessly, you will need to import some things:

```python
from zrb import runner, Parallel, CmdTask, python_task, StrInput
```

First of all, you need a `runner` so you can make your tasks available from the CLI. You also need `Parallel` to define task dependency. Next, you also need `CmdTask` and `python_task` decorator to define your tasks. Finally, you need `StrInput` to define task input.

Now, let's start with task definitions. We will need three task definitions:

- download-dataset
- install-pandas
- show-stats

First, we define `install-pandas`.

```python
# 🐼 Define a task named `install-pandas` to install pandas.
# If this task failed, we want Zrb to retry it again 4 times at most.
install_pandas = CmdTask(
    name='install-pandas',
    group=project_group,
    cmd='pip install pandas',
    retry=4
)
```

We use `CmdTask` to define `install-pandas`. We want it to be grouped under `project_group`, so that we can access the task using `zrb project install-pandas`. We also define `retry=4` so that when the task fails, Zrb will retry it again four times at most.

Once `install-pandas` has been defined, you can continue with `download-dataset` definition.

```python
DEFAULT_URL = 'https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv'

# ⬇️ Define a task named `download-dataset` to download dataset.
# This task has an input named `url`.
# The input will be accessible by using Jinja template: `{{input.url}}`
# If this task failed, we want Zrb to retry it again 4 times at most
download_dataset = CmdTask(
    name='download-dataset',
    group=project_group,
    inputs=[
        StrInput(name='url', default=DEFAULT_URL)
    ],
    cmd='wget -O dataset.csv {{input.url}}',
    retry=4
)
```

Our `download-dataset` definition is pretty much similar to `install-pandas` definition. However, since we want our user to be able to define the `url` of the dataset, we add an input named `url`. To access the value of the input, we can use Jinja template `{{input.url}}`.

> __⚠️ WARNING:__ By convention, task and input name should be written in __kebab-case__ (i.e, separated with `-`), while everything else (e.g., variable name, jinja template for input value, etc) should be written in __snake_case__ (i.e, separated with `_`).

We also need to modify our `show-stats` definition. Unlike `install-pandas` and `download-dataset`, `show-stats` is better written in Python. Thus, we use a `python_task` decorator instead. The decorator will transform `show_stats` function into a Zrb task. That means you cannot run `show_stats` as a regular Python function.

```python
# 📊 Define a task named `show-stat` to show the statistics properties of the dataset.
# @python_task` decorator turns a function into a Zrb Task (i.e., `show_stat` is now a Zrb Task).
# If this task failed, we don't want to retry
@python_task(
    name='show-stats',
    group=project_group,
    retry=0
)
def show_stats(*args, **kwargs):
    import pandas as pd
    df = pd.read_csv('dataset.csv')
    return df.describe()
```

Since `show_stats` depends on `download_dataset` and `install_pandas`, we can define the task dependencies as follows:

```python
# Define dependencies: `show_stat` depends on both, `download_dataset` and `install_pandas`
Parallel(download_dataset, install_pandas) >> show_stats
```

> __📝 NOTE:__ You can define the dependencies without using `Parallel`:
>
> ```python
> download_dataset >> show_stats
> install_pandas >> show_stats
> ```
>
> Or you can also use `upstreams` task definition.

Finally, we want `install_pandas`, `download_dataset`, and `show_stats` to be accessible from the CLI. Thus, we register the tasks as follows:

```python
# Register the tasks so that they are accessbie from the CLI
runner.register(install_pandas, download_dataset, show_stats)
```


<details>
<summary>Putting the code together</summary>

```python
from typing import Any
from zrb import runner, Parallel, CmdTask, python_task, StrInput
from zrb.builtin.group import project_group

DEFAULT_URL = 'https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv'

# 🐼 Define a task named `install-pandas` to install pandas.
# If this task failed, we want Zrb to retry it again 4 times at most.
install_pandas = CmdTask(
    name='install-pandas',
    group=project_group,
    cmd='pip install pandas',
    retry=4
)

# ⬇️ Define a task named `download-dataset` to download dataset.
# This task has an input named `url`.
# The input will be accessible by using Jinja template: `{{input.url}}`
# If this task failed, we want Zrb to retry it again 4 times at most
download_dataset = CmdTask(
    name='download-dataset',
    group=project_group,
    inputs=[
        StrInput(name='url', default=DEFAULT_URL)
    ],
    cmd='wget -O dataset.csv {{input.url}}',
    retry=4
)

# 📊 Define a task named `show-stat` to show the statistics properties of the dataset.
# @python_task` decorator turns a function into a Zrb Task (i.e., `show_stat` is now a Zrb Task).
# If this task failed, we don't want to retry
# We also want to register the task so that it is accessible from the CLI
@python_task(
    name='show-stats',
    group=project_group,
    retry=0
)
def show_stats(*args, **kwargs):
    import pandas as pd
    df = pd.read_csv('dataset.csv')
    return df.describe()

# Define dependencies: `show_stat` depends on both, `download_dataset` and `install_pandas`
Parallel(download_dataset, install_pandas) >> show_stats

# Register the tasks so that they are accessbie from the CLI
runner.register(install_pandas, download_dataset, show_stats)
```
</details>

To understand the code more, please visit [understanding the code section](#understanding-the-code).

## Running show-stats

Finally, you can show the statistics property of any public CSV dataset quickly.

```
zrb project show-stats
```

<details>
<summary>Show output</summary>

```
Url [https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv]:
🤖 ○ ◷ 2023-11-12 09:45:12.132 ❁ 43598 → 1/3 🐮 zrb project install-pandas • Run script: pip install pandas
🤖 ○ ◷ 2023-11-12 09:45:12.132 ❁ 43598 → 1/3 🐮 zrb project install-pandas • Working directory: /home/gofrendi/playground/my-project
🤖 ○ ◷ 2023-11-12 09:45:12.139 ❁ 43598 → 1/3 🍓 zrb project download-dataset • Run script: wget -O dataset.csv https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv
🤖 ○ ◷ 2023-11-12 09:45:12.139 ❁ 43598 → 1/3 🍓 zrb project download-dataset • Working directory: /home/gofrendi/playground/my-project
🤖 △ ◷ 2023-11-12 09:45:12.151 ❁ 43603 → 1/3 🍓 zrb project download-dataset • --2023-11-12 09:45:12--  https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv
🤖 △ ◷ 2023-11-12 09:45:12.218 ❁ 43603 → 1/3 🍓 zrb project download-dataset • Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.110.133, ...
🤖 △ ◷ 2023-11-12 09:45:12.246 ❁ 43603 → 1/3 🍓 zrb project download-dataset • Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
🤖 △ ◷ 2023-11-12 09:45:12.803 ❁ 43603 → 1/3 🍓 zrb project download-dataset • HTTP request sent, awaiting response... 200 OK
🤖 △ ◷ 2023-11-12 09:45:12.806 ❁ 43603 → 1/3 🍓 zrb project download-dataset • Length: 4606 (4.5K) [text/plain]
🤖 △ ◷ 2023-11-12 09:45:12.808 ❁ 43603 → 1/3 🍓 zrb project download-dataset • Saving to: ‘dataset.csv’
🤖 △ ◷ 2023-11-12 09:45:12.810 ❁ 43603 → 1/3 🍓 zrb project download-dataset •
🤖 △ ◷ 2023-11-12 09:45:12.812 ❁ 43603 → 1/3 🍓 zrb project download-dataset •      0K ....                                                  100% 1.39M=0.003s
🤖 △ ◷ 2023-11-12 09:45:12.814 ❁ 43603 → 1/3 🍓 zrb project download-dataset •
🤖 △ ◷ 2023-11-12 09:45:12.816 ❁ 43603 → 1/3 🍓 zrb project download-dataset • 2023-11-12 09:45:12 (1.39 MB/s) - ‘dataset.csv’ saved [4606/4606]
🤖 △ ◷ 2023-11-12 09:45:12.817 ❁ 43603 → 1/3 🍓 zrb project download-dataset •
🤖 ○ ◷ 2023-11-12 09:45:12.978 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: pandas in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (2.1.3)
🤖 ○ ◷ 2023-11-12 09:45:13.042 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: numpy<2,>=1.22.4 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from pandas) (1.26.1)
🤖 ○ ◷ 2023-11-12 09:45:13.044 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: python-dateutil>=2.8.2 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from pandas) (2.8.2)
🤖 ○ ◷ 2023-11-12 09:45:13.045 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: pytz>=2020.1 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from pandas) (2023.3.post1)
🤖 ○ ◷ 2023-11-12 09:45:13.047 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: tzdata>=2022.1 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from pandas) (2023.3)
🤖 ○ ◷ 2023-11-12 09:45:13.049 ❁ 43601 → 1/3 🐮 zrb project install-pandas • Requirement already satisfied: six>=1.5 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
Support zrb growth and development!
☕ Donate at: https://stalchmst.com/donation
🐙 Submit issues/PR at: https://github.com/state-alchemists/zrb
🐤 Follow us at: https://twitter.com/zarubastalchmst
🤖 ○ ◷ 2023-11-12 09:45:14.366 ❁ 43598 → 1/3 🍎 zrb project show-stats • Completed in 2.2365798950195312 seconds
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
To run again: zrb project show-stats --url "https://raw.githubusercontent.com/state-alchemists/datasets/main/iris.csv"
```
</details>

# Understanding The Code

## Task Definition

In general, there are two ways to define a task in Zrb.

- Using Task Classes (`CmdTask`, `DockerComposeTask`, `RemoteCmdTask`, `RsyncTask`, `ResourceMaker`, `FlowTask`, or `TriggeredTask`)
- Using Python Decorator (`@python_task`).

You can see that both `install_pandas` and `download_dataset` are instances of `CmdTask`, while `show_stats` is a decorated function.

### Creating a Task Using Task Classes

To define a task by using task classes, you need to follow this pattern:

```python
# importing zrb runner and the TaskClass
from zrb import runner, TaskClass

# Define a task, along with it's parameters
task_name = TaskClass(
    name='task-name',
    description='the description'
    # ... other task parameters
)

# regiter the task to zrb runner
runner.register(task_name)
```

> __💡 HINT:__ Check out [task-parameter section](#task-parameters) to see the commonly used parameters

There are several built-in task classes. Each with its specific use case:

- __CmdTask__: Run a CLI command/shell script.
- __DockerComposeTask__: Run any docker-compose related command (e.g., `docker compose up`, `docker compose down`, etc.)
- __RemoteCmdTask__: Run a CLI command/shell script on remote computers using SSH.
- __RSyncTask__: Copy file from/to remote computers using `rsync` command.
- __ResourceMaker__: Create resources (source code/documents) based on provided templates.
- __FlowTask__: Combine unrelated tasks into a single Workflow.
- __RecurringTask__: Create a long-running recurring task.

You can also create a custom task class as long as it fits `AnyTask` interface. The easiest way to ensure compatibility is by extending `BaseTask`. See our [tutorial](tutorials/extending-cmd-task.md) to see how we can create a new Task Class based on `CmdTask`.

### Creating a Task Using Python Decorator

To define a task by using Python decorator, you need to follow this pattern:

```python
# importing zrb runner and @python_task
from zrb import runner, python_task


# Decorate a function named `task_name`
@python_task(
    name='task-name',
    description='the description'
    # ... other task parameters
    runner=runner # register the task to zrb runner
)
def task_name(*args, **kwargs):
    pass

# Note that python_task decorator turn your function into a task. So `task_name` is now a task, not a function.
```

> __💡 HINT:__ Check out [task-parameter section](#task-parameters) to see the commonly used parameters

Using `@python_task` decorator is your best choice if you need to write complex logic in Python.


### Task Parameters

Each task has its specific parameter. However, the following parameters are typically available:

- __name__: The name of the task. When you invoke the task using the CLI, you need to use this name. By convention, the name should-be written in `kebab-case` (i.e., separated by `-`)
- __description__: The description of the task.
- __group__: The task group where the task belongs to
- __inputs__: Task inputs and their default values.
- __envs__: Task's environment variables.
- __env_files__: Task's environment files.
- __upstreams__: Upstreams of the task. You can provide `AnyTask` as upstream.
- __checkers__: List of checker tasks. You usually need this for long-running tasks.
- __runner__: Only available in `@python_task`, the valid value is `zrb.runner`.

You can apply task parameters to both Task classes and `@python_task` decorator.


# Task Dependencies

There are two ways to define task dependencies in Zrb.

- Using `>>` operator.
- Using `upstreams` parameter.

You can use `>>` operator as follows:

```python
task_1 = CmdTask(name='task-1')
task_2 = CmdTask(name='task-2')
task_3 = CmdTask(name='task-3')
task_4 = CmdTask(name='task-4')
task_5 = CmdTask(name='task-5')
task_6 = CmdTask(name='task-6')

task_1 >> Parallel(task_2, task_3) >> Parallel(task_4, task_5) >> task_6
```

Or you can use `upstreams` parameter as follows:

```python
task_1 = CmdTask(name='task-1')
task_2 = CmdTask(name='task-2', upstreams=[task_1])
task_3 = CmdTask(name='task-3', upstreams=[task_1])
task_4 = CmdTask(name='task-4', upstreams=[task_2, task_3])
task_5 = CmdTask(name='task-5', upstreams=[task_2, task_3])
task_6 = CmdTask(name='task-6', upstreams=[task_4, task_5])
```

## Task Inputs

You can define task inputs using `StrInput`, `BoolInput`, `ChoiceInput`, `FloatInput`, `IntInput`, or `PasswordInput`.
To create an input, you need to provide some parameters:

- __name__: The name of the input. By convention, this should be kebab-cased (required).
- __default__: The default value of the input (optional, default: `None`).
- __should_render__: Whether the input should be rendered as Jinja template or not (optional, default: `True`).

For example, here you have an input named `message` with `Hello World` as the default value:

```python
from zrb import StrInput

message = StrInput(name='message', default='Hello World')
```

When you run a task with task inputs, Zrb will prompt you to override the input values. You can press `enter` if you want to use the default values.

### Using Task Inputs on CmdTask

To access the values of your inputs from your `CmdTask`, you can use Jinja template `{{ input.input_name }}`. Notice that you should use `snake_case` instead of `kebab-case` to refer to the input. Let's see the following example:

```python
from zrb import runner, CmdTask, StrInput

hello_cmd = CmdTask(
    name='hello-cmd',
    inputs=[
        StrInput(name='your-name', default='World')
    ],
    # Notice, we use {{input.your_name}} not {{input.your-name}} !!!
    cmd='echo Hello {{input.your_name}}'
)
runner.register(hello_cmd)
```

You can then run the task by invoking:

```bash
zrb hello-cmd
# or
zrb hello-cmd --your-name "John Wick"
```

### Using Task Inputs on @python_task Decorator

As for `@python_task`, you can use `kwargs` dictionary to get the input.

```python
from zrb import runner, python_task, StrInput

@python_task(
    name='hello-py',
    inputs=[
        StrInput(name='your-name', default='World')
    ],
    runner=runner
)
def hello_py(*args, **kwargs):
    # Notice, we use `your_name` instead of `your-name` !!!
    name = kwargs.get('your_name')
    return f'Hello {name}'
```


You can then run the task by invoking:

```bash
zrb hello-py
# or
zrb hello-py --your-name "John Wick"
```

## Task Environments

Aside from input, you can also define the `Task`'s environment variables using `Env` and `EnvFile`.

### Env

You can use `Env` to define a single environment variable for your Tasks. Typically, a Task could take multiple `Env`.

To create an `Env`, you need to provide some parameters:

- __name__: Name of the environment variable (required).
- __os_name__: Name of OS environment (optional, default=`None`)
    - if set to `None`, Zrb will link the environment variable to the OS environment.
    - if set to an empty string (i.e., `''`), Zrb will not link the environment variable to the OS's environment.
    - if set to a non-empty string, Zrb will link the environment variable to the OS's environment corresponding to this value.
- __default__: Default value of the environment variable (optional, default: `None`).
- __should_render__: Whether the environment variable should be rendered as a Jinja template (optional, default: `True`).


```python
from zrb import Env

env = Env(name='MESSAGE')
```

### EnvFile

`EnvFile` loads an environment file and uses its values as Task's environment variables. Typically a Task could take multiple `EnvFile`.

To create an `EnvFile`, you need to provide some parameters:

- __env_file__: Name of the environment file (required).
- __prefix__: Custom prefix for environment's os_name (optional, default=`None`)
- __should_render__: Whether the environment variable should be rendered as a Jinja template (optional, default: `True`).

```python
from zrb import EnvFile
import os

PROJECT_ENV = os.path.join(os.path.dirname(__file__), 'project.env')
env_file = EnvFile(path=PROJECT_ENV)
```

### Using Env and EnvFile

To use `EnvFile` in your tasks. Let's first create an environment file named `project.env`:

```bash
# file-name: project.env
SERVER_HOST=localhost
```

### Using Env and EnvFile on CmdTask

To access the values of your inputs from your `CmdTask`, you can use Jinja template `{{ env.ENV_NAME }}`.

```python
from zrb import runner, CmdTask, Env, EnvFile
import os

PROJECT_ENV = os.path.join(os.path.dirname(__file__), 'project.env')

hello_cmd = CmdTask(
    name='hello-cmd',
    envs=[
        Env(name='MESSAGE', default='Hello world'),
    ],
    env_files=[
        EnvFile(path=PROJECT_ENV)
    ],
    cmd=[
        'echo Message: {{env.MESSAGE}}',
        'echo Host: {{env.SERVER_HOST}}',
    ]
)
runner.register(hello_cmd)
```

You can then run the task by invoking:

```bash
zrb hello-cmd
```

It will give you the following results:

```
Message: Hello world
Host: localhost
```

### Using Env and EnvFile on @python_task Decorator

As for `@python_task`, you cannot use `os.getenv` to access task's environment. Instead, you should get the `task` instance from `kwargs`` and invoke `task.get_env_map()`.

```python
from zrb import runner, AnyTask, python_task, Env, EnvFile
import os

PROJECT_ENV = os.path.join(os.path.dirname(__file__), 'project.env')


@python_task(
    name='hello-py',
    envs=[
        Env(name='MESSAGE', default='Hello world'),
    ],
    env_files=[
        EnvFile(path=PROJECT_ENV)
    ],
    runner=runner
)
def hello_py(*args, **kwargs):
    task: AnyTask = kwargs.get('_task')
    env_map = task.get_env_map()
    message = env_map.get('MESSAGE')
    server_host = env_map.get('SERVER_HOST')
    return '\n'.join([
        f'Message: {message}',
        f'Host: {server_host}'
    ])
```

You can then run the task by invoking:

```bash
zrb hello-cmd
```

It will give you the following results:

```
Message: Hello world
Host: localhost
```

## Switching Environment

Zrb has a feature named environment cascading. This feature helps you switch between multiple environments (e.g., dev, staging, production).

To switch between environments, you can use `ZRB_ENV`

Let's go back to our previous example and set some environment variables:


```bash
export DEV_MESSAGE="Test Hello World"
export PROD_MESSAGE="Hello, Client"
export PROD_SERVER_HOST=stalchmst.com

zrb hello-cmd
```

Without `ZRB_ENV`, when you run the following commands, you will get the same outputs:

```
Message: Hello world
Host: localhost
```

Since we don't have `MESSAGE` and `HOST` on OS's environment variable, Zrb will use the default values.

### Dev Environment

Now, let's try this again with `DEV` environment:

```bash
export DEV_MESSAGE="Test Hello World"
export PROD_MESSAGE="Hello, Client"
export PROD_SERVER_HOST=stalchmst.com
export ZRB_ENV=DEV

zrb hello-cmd
```

Now, it will get the the following outputs:

```
Message: Test Hello World
Host: localhost
```

You see that now Zrb loads use `DEV_MESSAGE` value instead of the default `Hello World`.

However, since Zrb cannot find `DEV_SERVER_HOST`, it use the default value `localhost`.

### Prod Environment

Now let's try again with `PROD` environment:

```bash
export DEV_MESSAGE="Test Hello World"
export PROD_MESSAGE="Hello, Client"
export PROD_SERVER_HOST=stalchmst.com
export ZRB_ENV=PROD

zrb hello-cmd
```

Now, since Zrb can find both `PROD_MESSAGE` and `PROD_SERVER_HOST`, Zrb will show the following output:

```
Message: Hello, Client
Host: stalchmst.com
```

# Creating a long-running task

Commonly, you can determine whether a task is successful/failed after the task is finished. However, some tasks might run forever, and you can only see whether the task is completed or failed by checking other behaviors. For example, a web server is successfully running if you can get the expected HTTP response from the server.

Zrb has some checking mechanisms to handle this use case.

Let's start by scaffolding a CmdTask named `run-jupyterlab`.

```bash
zrb project add cmd-task --project-dir "." --task-name "run-jupyterlab"
```

You will notice that Zrb automatically creates a file named `_automate/run_jupyterlab.py`

We will need to modify the file.


## Adding start-jupyterlab

We have a few requirements for `start-jupyterlab` task

- Before starting Jupyterlab, you need to make sure that Jupyterlab is already installed.
- Jupyterlab is considered completed once the port is accessible.
- Jupyterlab HTTP port should be `8080` by default, but users should be able to override the Jupyterlab HTTP port.

Now, let's modify `_automate/start_jupyterlab.py` into the following:

```python
from zrb import CmdTask, PortChecker, IntInput, runner
from zrb.builtin.group import project_group
import os


install_jupyterlab = CmdTask(
    name='install-jupyterlab',
    group=project_group,
    cmd='pip install jupyterlab'
)
runner.register(install_jupyterlab)


notebook_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'src'
)
run_jupyterlab = CmdTask(
    name='run-jupyterlab',
    description='run jupyterlab',
    group=project_group,
    upstreams=[install_jupyterlab],
    inputs=[
        IntInput(name='jupyterlab-port', default=8080),
    ],
    cmd=[
        'jupyter lab \\',
        '  --port {{input.jupyterlab_port}}',
        f'  --notebook-dir "{notebook_path}"'
    ],
    checkers=[
        PortChecker(name='check-jupyterlab', port='{{input.jupyterlab_port}}')
    ]
)
runner.register(run_jupyterlab)
```

You may notice that `run_jupyterlab` has a `PortChecker` on it. If the `PortChecker` can get TCP response, then `run_jupyterlab` is considered successful.
Let's run the task:

```bash
zrb project run-jupyterlab
```

<details>
<summary>Show output</summary>

```
Jupyterlab port [8080]: 
🤖 ○ ◷ 2023-11-12 10:26:32.759 ❁ 58728 → 1/3 🐨 zrb project install-jupyterlab • Run script: pip install jupyterlab
🤖 ○ ◷ 2023-11-12 10:26:32.759 ❁ 58728 → 1/3 🐨 zrb project install-jupyterlab • Working directory: /home/gofrendi/playground/my-project
🤖 ○ ◷ 2023-11-12 10:26:33.109 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: jupyterlab in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (4.0.8)
🤖 ○ ◷ 2023-11-12 10:26:33.149 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: async-lru>=1.0.0 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from jupyterlab) (2.0.4)
🤖 ○ ◷ 2023-11-12 10:26:33.151 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: ipykernel in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from jupyterlab) (6.26.0)
🤖 ○ ◷ 2023-11-12 10:26:33.153 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: jinja2>=3.0.3 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from jupyterlab) (3.1.2)
🤖 ○ ◷ 2023-11-12 10:26:33.156 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: jupyter-core in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from jupyterlab) (5.5.0)
🤖 ○ ◷ 2023-11-12 10:26:33.968 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: pycparser in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (2.21)
🤖 ○ ◷ 2023-11-12 10:26:34.041 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: arrow>=0.15.0 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (1.3.0)
🤖 ○ ◷ 2023-11-12 10:26:34.093 ❁ 58731 → 1/3 🐨 zrb project install-jupyterlab • Requirement already satisfied: types-python-dateutil>=2.8.10 in /home/gofrendi/zrb/.venv/lib/python3.10/site-packages (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (2.8.19.14)
🤖 ○ ◷ 2023-11-12 10:26:34.717 ❁ 58728 → 1/3 🐹 zrb project run-jupyterlab • Run script:
        0001 | jupyter lab \
        0002 |   --port 8080
        0003 |   --notebook-dir "/home/gofrendi/playground/my-project/src"
🤖 ○ ◷ 2023-11-12 10:26:34.717 ❁ 58728 → 1/3 🐹 zrb project run-jupyterlab • Working directory: /home/gofrendi/playground/my-project
🤖 △ ◷ 2023-11-12 10:26:35.693 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab • [I 2023-11-12 10:26:35.675 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
🤖 △ ◷ 2023-11-12 10:26:36.789 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab • [C 2023-11-12 10:26:36.788 ServerApp]
🤖 △ ◷ 2023-11-12 10:26:36.791 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •
🤖 △ ◷ 2023-11-12 10:26:36.793 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •     To access the server, open this file in a browser:
🤖 △ ◷ 2023-11-12 10:26:36.795 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •         file:///home/gofrendi/.local/share/jupyter/runtime/jpserver-58922-open.html
🤖 △ ◷ 2023-11-12 10:26:36.798 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •     Or copy and paste one of these URLs:
🤖 △ ◷ 2023-11-12 10:26:36.799 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •         http://localhost:8080/lab?token=58eecd6aa4a56445ecf8b8d8c2f2148d47a7ce8456ecd680
🤖 △ ◷ 2023-11-12 10:26:36.801 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab •         http://127.0.0.1:8080/lab?token=58eecd6aa4a56445ecf8b8d8c2f2148d47a7ce8456ecd680
🤖 ○ ◷ 2023-11-12 10:26:36.807 ❁ 58728 → 1/1 🐹     check-jupyterlab • Checking localhost:8080 (OK)
Support zrb growth and development!
☕ Donate at: https://stalchmst.com/donation
🐙 Submit issues/PR at: https://github.com/state-alchemists/zrb
🐤 Follow us at: https://twitter.com/zarubastalchmst
🤖 ○ ◷ 2023-11-12 10:26:36.807 ❁ 58920 → 1/3 🐹 zrb project run-jupyterlab • Completed in 4.050489664077759 seconds
```

</details>

Open up your browser on [http://localhost:8080](http://localhost:8080) to start working with the notebook.

# Now you are ready

We have covered everything you need to know to work with Zrb.

To learn more about tasks and other concepts, you can visit [Zrb concept section](concepts/README.md).

Also, do you know that you can make and deploy a CRUD application without even touching your IDE/text editor? Check out [our tutorials](tutorials/README.md) for more cool tricks.


🔖 [Table of Contents](README.md)