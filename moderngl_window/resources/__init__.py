from pathlib import Path
from typing import Union

from moderngl_window.conf import settings
from moderngl_window.exceptions import ImproperlyConfigured

from moderngl_window.resources.programs import programs  # noqa
from moderngl_window.resources.textures import textures  # noqa
# from moderngl_window.resources.tracks import tracks  # noqa
from moderngl_window.resources.scenes import scenes  # noqa
from moderngl_window.resources.data import data  # noqa


def register_dir(path: Union[Path, str]):
    """Adds a resource directory for all resource types

    Args:
        path (Union[Path, str]): Directory path
    """
    register_data_dir(path)
    register_program_dir(path)
    register_scene_dir(path)
    register_texture_dir(path)


def register_program_dir(path: Union[Path, str]):
    """Adds a resource directory for all resource types

    Args:
        path (Union[Path, str]): Directory path
    """
    _append_unique_path(path, settings.PROGRAM_DIRS)


def register_texture_dir(path: Union[Path, str]):
    """Adds a resource directory for all resource types

    Args:
        path (Union[Path, str]): Directory path
    """
    _append_unique_path(path, settings.TEXTURE_DIRS)


def register_scene_dir(path: Union[Path, str]):
    """Adds a resource directory for all resource types

    Args:
        path (Union[Path, str]): Directory path
    """
    _append_unique_path(path, settings.SCENE_DIRS)


def register_data_dir(path: Union[Path, str]):
    """Adds a resource directory for all resource types

    Args:
        path (Union[Path, str]): Directory path
    """
    _append_unique_path(path, settings.DATA_DIRS)


def _append_unique_path(path: Union[Path, str], dest: list):
    path = Path(path)
    if not path.is_absolute():
        raise ImproperlyConfigured("Search path must be absolute: {}".format(path))

    for resource_path in dest:
        if Path(resource_path).samefile(path):
            break
    else:
        dest.append(Path(path).absolute())
