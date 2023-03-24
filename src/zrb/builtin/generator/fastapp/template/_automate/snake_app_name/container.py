from zrb import DockerComposeTask, Env, HTTPChecker, runner
from zrb.builtin._group import project_group
from ._common import (
    RESOURCE_DIR,
    rabbitmq_checker, rabbitmq_management_checker,
    redpanda_console_checker, kafka_outside_checker,
    kafka_plaintext_checker, pandaproxy_outside_checker,
    pandaproxy_plaintext_checker,
    local_input, host_input, https_input, image_input,
    compose_app_broker_type_env, compose_app_host_port_env,
    compose_rabbitmq_host_port_env, compose_rabbitmq_management_host_port_env,
    compose_redpanda_console_host_port_env,
    compose_kafka_outside_host_port_env,
    compose_pandaproxy_outside_host_port_env,
    compose_kafka_plaintext_host_port_env,
    compose_pandaproxy_plaintext_host_port_env
)
from .image import build_snake_app_name_image

compose_env_prefix = 'CONTAINER_ENV_PREFIX'
compose_envs = [
    compose_app_broker_type_env,
    compose_app_host_port_env,
    compose_rabbitmq_host_port_env,
    compose_rabbitmq_management_host_port_env,
    compose_redpanda_console_host_port_env,
    compose_kafka_outside_host_port_env,
    compose_kafka_plaintext_host_port_env,
    compose_pandaproxy_outside_host_port_env,
    compose_pandaproxy_plaintext_host_port_env
]
compose_checkers = [
    HTTPChecker(
        name='check-kebab-app-name-monolith',
        host='{{input.snake_app_name_host}}',
        url='/readiness',
        port='{{env.get("HOST_PORT", "httpPort")}}',
        is_https='{{input.snake_app_name_https}}'
    ),
    rabbitmq_checker,
    rabbitmq_management_checker,
    kafka_outside_checker,
    kafka_plaintext_checker,
    redpanda_console_checker,
    pandaproxy_outside_checker,
    pandaproxy_plaintext_checker,
]


remove_snake_app_name_container = DockerComposeTask(
    icon='💨',
    name='remove-kebab-app-name-container',
    description='Rumove human readable app name container',
    group=project_group,
    cwd=RESOURCE_DIR,
    compose_cmd='down',
    compose_env_prefix=compose_env_prefix,
    envs=compose_envs,
)
runner.register(remove_snake_app_name_container)

start_snake_app_name_container = DockerComposeTask(
    icon='🐳',
    name='start-kebab-app-name-container',
    description='Start human readable app name container',
    group=project_group,
    inputs=[
        local_input,
        host_input,
        https_input,
        image_input,
    ],
    skip_execution='{{not input.local_snake_app_name}}',
    upstreams=[
        build_snake_app_name_image,
        remove_snake_app_name_container
    ],
    cwd=RESOURCE_DIR,
    compose_cmd='up',
    compose_env_prefix=compose_env_prefix,
    envs=compose_envs + [
        Env(
            name='COMPOSE_PROFILES',
            os_name='',
            default=' '.join([
                '{{',
                '",".join([',
                '  env.get("APP_BROKER_TYPE", "rabbitmq"),',
                '  "monolith"',
                '])',
                '}}'
            ])
        )
    ],
    checkers=[
        HTTPChecker(
            name='check-kebab-app-name-monolith',
            host='{{input.snake_app_name_host}}',
            url='/readiness',
            port='{{env.get("HOST_PORT", "httpPort")}}',
            is_https='{{input.snake_app_name_https}}'
        ),
        rabbitmq_checker,
        rabbitmq_management_checker,
        kafka_outside_checker,
        kafka_plaintext_checker,
        redpanda_console_checker,
        pandaproxy_outside_checker,
        pandaproxy_plaintext_checker,
    ]
)
runner.register(start_snake_app_name_container)

stop_snake_app_name_container = DockerComposeTask(
    icon='⛔',
    name='stop-kebab-app-name-container',
    description='Stop human readable app name container',
    group=project_group,
    cwd=RESOURCE_DIR,
    compose_cmd='stop',
    compose_env_prefix=compose_env_prefix,
    envs=compose_envs,
)
runner.register(stop_snake_app_name_container)
