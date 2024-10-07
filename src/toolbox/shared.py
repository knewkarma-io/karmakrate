import os
from platform import python_version, platform

from api import Api, SORT_CRITERION, TIMEFRAME, TIME_FORMAT
from knewkarma.meta import about, version
from toolbox.terminal_utils import Message, Style

__all__ = [
    "about",
    "api",
    "console",
    "OUTPUT_PARENT_DIR",
    "notify",
    "style",
    "SORT_CRITERION",
    "TIMEFRAME",
    "TIME_FORMAT",
    "version",
]

api = Api(
    headers={
        "User-Agent": f"{about.name.replace(' ', '-')}/{version.release} "
        f"(Python {python_version} on {platform}; +{about.documentation})"
    },
)

message = Message
style = Style

OUTPUT_PARENT_DIR: str = os.path.expanduser(os.path.join("~", "knewkarma"))
