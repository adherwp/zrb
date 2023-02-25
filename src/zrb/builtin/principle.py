from typing import Any
from ._group import principle_show_group
from ..task.task import Task
from ..runner import runner

# Common definitions


def _show_solid(*args: Any, **kwargs: Any):
    task: Task = kwargs['_task']
    task.print_out('S - Single Responsibility Principle')
    task.print_out('O - Open/Closed Principle')
    task.print_out('L - Liskov’s Substitution Principle')
    task.print_out('I - Interface Segregation Principle')
    task.print_out('D - Dependency Inversion Principle')


def _show_yagni(*args: Any, **kwargs: Any):
    task: Task = kwargs['_task']
    task.print_out('Y - You')
    task.print_out('A - Aren\'t')
    task.print_out('G - Gonna')
    task.print_out('N - Need')
    task.print_out('I - It')


def _show_dry(*args: Any, **kwargs: Any):
    task: Task = kwargs['_task']
    task.print_out('D - Don\'t')
    task.print_out('R - Repeat')
    task.print_out('Y - Yourself')


def _show_kiss(*args: Any, **kwargs: Any):
    task: Task = kwargs['_task']
    task.print_out('K - Keep')
    task.print_out('I - It')
    task.print_out('S - Simple')
    task.print_out('S - Stupid')


def _show_pancasila(*args: Any, **kwargs: Any):
    task: Task = kwargs['_task']
    task.print_out('1. Ketuhanan Yang Maha Esa')
    task.print_out('2. Kemanusiaan yang adil dan beradab')
    task.print_out('3. Persatuan Indonesia')
    task.print_out(' '.join([
        '4. Kerakyatan yang dipimpin oleh hikmat kebijaksanaan',
        'dalam permusyawaratan/perwakilan'
    ]))
    task.print_out('5. Keadilan sosial bagi seluruh rakyat Indonesia')


# Task definitions

show_solid_principle = Task(
    name='solid',
    group=principle_show_group,
    run=_show_solid,
    description='Show SOLID principle',
)
runner.register(show_solid_principle)

show_yagni_principle = Task(
    name='yagni',
    group=principle_show_group,
    run=_show_yagni,
    description='Show YAGNI principle',
)
runner.register(show_yagni_principle)

show_dry_principle = Task(
    name='dry',
    group=principle_show_group,
    run=_show_dry,
    description='Show dry principle',
)
runner.register(show_dry_principle)

show_kiss_principle = Task(
    name='kiss',
    group=principle_show_group,
    run=_show_kiss,
    description='Show kiss principle',
)
runner.register(show_kiss_principle)

show_pancasila = Task(
    icon="🦅",
    name='pancasila',
    group=principle_show_group,
    run=_show_pancasila,
    description='Show pancasila',
)
runner.register(show_pancasila)
