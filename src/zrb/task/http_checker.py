from typing import Any, List, Optional, Union
from typeguard import typechecked
from http.client import HTTPConnection, HTTPSConnection
from .base_task import BaseTask
from ..task_env.env import Env
from ..task_group.group import Group
from ..task_input.base_input import BaseInput

import asyncio


@typechecked
class HTTPChecker(BaseTask):

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
        method: str = 'HEAD',
        url: str = '/',
        is_https: bool = False,
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
        self.method = method
        self.url = url
        self.is_https = is_https

    async def run(self, **kwargs: Any):
        method = self.render_str(self.method)
        host = self.render_str(self.host)
        port = self.render_int(self.port)
        url = self.render_str(self.url)
        timeout = self.render_int(self.timeout)
        while not self._check_connection(method, host, port, url, timeout):
            await asyncio.sleep(self.checking_interval)

    def _check_connection(
        self, method: str, host: str, port: int, url: str, timeout: int
    ) -> bool:
        label = self._get_label(method, host, port, url)
        conn = self._get_connection(host, port, timeout)
        try:
            conn.request(method, url)
            res = conn.getresponse()
            if res.status < 300:
                self.log_info('Connection success')
                self.print_out(f'{label} {res.status} (OK)')
                return True
            self.log_debug(f'{label} {res.status} (Not OK)')
        except Exception:
            self.log_debug(f'{label} Connection error')
        finally:
            conn.close()
        return False

    def _get_label(self, method: str, host: str, port: int, url: str) -> str:
        protocol = 'https' if self.is_https else 'http'
        return f'{method} {protocol}://{host}:{port}{url}'

    def _get_connection(
        self, host: str, port: int, timeout: int
    ) -> Union[HTTPConnection, HTTPSConnection]:
        if self.is_https:
            return HTTPSConnection(host, port, timeout=timeout)
        return HTTPConnection(host, port, timeout=timeout)
