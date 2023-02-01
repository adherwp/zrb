from typing import Any, List, Optional, Union
from typeguard import typechecked
from .base_task import BaseTask
from ..task_env.env import Env
from ..task_group.group import Group
from ..task_input.base_input import BaseInput

import socket
import asyncio


@typechecked
class PortChecker(BaseTask):

    def __init__(
        self,
        name: str = 'http_checker',
        group: Optional[Group] = None,
        inputs: List[BaseInput] = [],
        envs: List[Env] = [],
        icon: Optional[str] = None,
        color: Optional[str] = None,
        description: str = '',
        host: str = 'localhost',
        port: Union[int, str] = 80,
        timeout: Union[int, str] = 5,
        upstreams: List[BaseTask] = [],
        checkers: List[BaseTask] = [],
        checking_interval: float = 0.3,
        retry: int = 2,
        retry_interval: float = 1,
    ):
        BaseTask.__init__(
            self,
            name=name,
            group=group,
            inputs=inputs,
            envs=envs,
            icon=icon,
            color=color,
            description=description,
            upstreams=upstreams,
            checkers=checkers,
            checking_interval=checking_interval,
            retry=retry,
            retry_interval=retry_interval
        )
        self.host = host
        self.port = port
        self.timeout = timeout

    async def run(self, **kwargs: Any):
        host = self.render_str(self.host)
        port = self.render_int(self.port)
        timeout = self.render_int(self.timeout)
        while not self._check_port(host, port, timeout):
            await asyncio.sleep(self.checking_interval)

    def _check_port(
        self, host: str, port: int, url: str, timeout: int
    ) -> bool:
        label = self._get_label(host, port, url)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            if result == 0:
                self.print_out(f'{label} (OK)')
                return True
        self.log_debug(f'{label} (Not OK)')
        return False

    def _get_label(self, host: str, port: int) -> str:
        return f'Checking {host}:{port}'