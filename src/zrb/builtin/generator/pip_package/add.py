from typing import Any
from ..._group import project_add_group
from ....task.decorator import python_task
from ....task.task import Task
from ....task.resource_maker import ResourceMaker
from ....runner import runner
from .._common.task_input import (
    project_dir_input, package_name_input, package_description_input,
    package_homepage_input, package_bug_tracker_input,
    package_author_name_input, package_author_email_input
)
from .._common.helper import (
    validate_existing_project_dir, validate_inexisting_automation
)
from .._common.task_factory import create_register_module

import os

current_dir = os.path.dirname(__file__)


###############################################################################
# Task Definitions
###############################################################################


@python_task(
    name='validate',
    inputs=[
        project_dir_input,
        package_name_input
    ]
)
async def validate(*args: Any, **kwargs: Any):
    project_dir = kwargs.get('project_dir')
    validate_existing_project_dir(project_dir)
    package_name = kwargs.get('package_name')
    validate_inexisting_automation(project_dir, package_name)


copy_resource = ResourceMaker(
    name='copy-resource',
    inputs=[
        project_dir_input,
        package_name_input,
        package_description_input,
        package_homepage_input,
        package_bug_tracker_input,
        package_author_name_input,
        package_author_email_input
    ],
    upstreams=[validate],
    replacements={
        'zrbPackageName': '{{input.package_name}}',
        'zrbPackageDescription': '{{input.package_description}}',
        'zrbPackageHomepage': '{{input.package_homepage}}',
        'zrbPackageBugTracker': '{{input.package_bug_tracker}}',
        'zrbPackageAuthorName': '{{input.package_author_name}}',
        'zrbPackageAuthorEmail': '{{input.package_author_email}}'
    },
    template_path=os.path.join(current_dir, 'template'),
    destination_path='{{ input.project_dir }}',
    excludes=[
        '*/__pycache__',
    ]
)

register_module = create_register_module(
    module_path='_automate.{{util.to_snake_case(input.package_name)}}.local',
    alias='{{util.to_snake_case(input.package_name)}}_local',
    inputs=[package_name_input],
    upstreams=[copy_resource]
)


@python_task(
    name='pip-package',
    group=project_add_group,
    upstreams=[register_module],
    runner=runner
)
async def add_python_task(*args: Any, **kwargs: Any):
    task: Task = kwargs.get('_task')
    task.print_out('Success')
