# Cmd task


You can define a Cmd task by using `CmdTask` class.

```python
from zrb import CmdTask, StrInput, Env, runner

say_hello = CmdTask(
    name='say-hello',
    inputs=[
        StrInput(name='name')
    ],
    envs=[
        Env(name='SOME_ENV')
    ],
    cmd='echo {{input.name}}'
)
runner.register(say_hello)
```

If you need a multi-line command, you can also define the command as a list:

```python
from zrb import CmdTask, StrInput, Env, runner

say_hello = CmdTask(
    name='say-hello',
    inputs=[
        StrInput(name='name')
    ],
    envs=[
        Env(name='SOME_ENV')
    ],
    cmd=[
        'echo {{input.name}}',
        'echo Yeay!!!'
    ]
)
runner.register(say_hello)
```

However, if your command is too long, you can also load it from another file:


```python
from zrb import CmdTask, StrInput, Env, runner

say_hello = CmdTask(
    name='say-hello',
    inputs=[
        StrInput(name='name')
    ],
    envs=[
        Env(name='SOME_ENV')
    ],
    cmd_path='hello_script.sh'
)
runner.register(say_hello)
```


You can then run the task by invoking:

```
zrb say-hello --name=John
```
