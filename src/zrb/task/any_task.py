from typing import (
    Any, Callable, Iterable, List, Mapping, Optional, Union, TypeVar
)
from abc import ABC, abstractmethod
from ..task_env.env_file import EnvFile
from ..task_env.env import Env
from ..task_input.base_input import BaseInput

TAnyTask = TypeVar('TAnyTask', bound='AnyTask')


class AnyTask(ABC):
    '''
    Task class specification.
    In order to create a new Task class, you have to implements all methods.
    You can do this by extending BaseTask.

    Currently we don't see any advantage to break this interface into
    multiple interfaces since AnyTask is considered atomic.
    '''
    @abstractmethod
    async def run(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    async def check(self) -> bool:
        pass

    @abstractmethod
    def to_function(
        self, env_prefix: str = '', raise_error: bool = True
    ) -> Callable[..., Any]:
        pass

    @abstractmethod
    def add_upstreams(self, *upstreams: TAnyTask):
        pass

    @abstractmethod
    def get_icon(self) -> str:
        pass

    @abstractmethod
    def get_color(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cmd_name(self) -> str:
        pass

    @abstractmethod
    def get_env_files(self) -> List[EnvFile]:
        pass

    @abstractmethod
    def get_envs(self) -> List[Env]:
        pass

    @abstractmethod
    def get_checkers(self) -> Iterable[TAnyTask]:
        pass

    @abstractmethod
    def get_upstreams(self) -> Iterable[TAnyTask]:
        pass

    @abstractmethod
    def get_all_inputs(self) -> Iterable[BaseInput]:
        pass

    @abstractmethod
    def log_debug(self, message: Any):
        pass

    @abstractmethod
    def log_warn(self, message: Any):
        pass

    @abstractmethod
    def log_info(self, message: Any):
        pass

    @abstractmethod
    def log_error(self, message: Any):
        pass

    @abstractmethod
    def log_critical(self, message: Any):
        pass

    @abstractmethod
    def print_out(self, message: Any):
        pass

    @abstractmethod
    def print_err(self, message: Any):
        pass

    @abstractmethod
    def print_out_dark(self, message: Any):
        pass

    @abstractmethod
    def get_input_map(self) -> Mapping[str, Any]:
        pass

    @abstractmethod
    def get_env_map(self) -> Mapping[str, Any]:
        pass

    @abstractmethod
    def render_any(
        self, val: Any, data: Optional[Mapping[str, Any]] = None
    ) -> Any:
        pass

    @abstractmethod
    def render_float(
        self, val: Union[str, float], data: Optional[Mapping[str, Any]] = None
    ) -> float:
        pass

    @abstractmethod
    def render_int(
        self, val: Union[str, int], data: Optional[Mapping[str, Any]] = None
    ) -> int:
        pass

    @abstractmethod
    def render_bool(
        self, val: Union[str, bool], data: Optional[Mapping[str, Any]] = None
    ) -> bool:
        pass

    @abstractmethod
    def render_str(
        self, val: str, data: Optional[Mapping[str, Any]] = None
    ) -> str:
        pass

    @abstractmethod
    def render_file(
        self, location: str, data: Optional[Mapping[str, Any]] = None
    ) -> str:
        pass