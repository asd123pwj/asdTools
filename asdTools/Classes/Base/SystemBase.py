from asdTools.Classes.Base.RewriteBase import RewriteBase
import platform
import socket


class SystemBase(RewriteBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def check_Windows(self) -> bool:
        plat = platform.system().lower()
        if plat == 'windows':
            return True
        else:
            return False

    def check_Linux(self) -> bool:
        plat = platform.system().lower()
        if plat == 'linux':
            return True
        else:
            return False

    def get_hostname(self):
        hostname = socket.gethostname()
        return hostname
