from sys import platform as _sys_platform

class Windows_Platform:
    def systeminfo(self):
        return "hello from windows"

class Linux_Platform:
    def systeminfo(self):
        return "hello from linux"

class Platform_Factory:
    def get_factory(self):
        if _sys_platform in ('win32', 'cygwin'):
            return Windows_Platform()
        elif _sys_platform == 'darwin':
            pass
        elif _sys_platform.startswith('linux'):
            return Linux_Platform()
        elif _sys_platform.startswith('freebsd'):
            return Linux_Platform()
        pass


if __name__ == "__main__":
    # plat = Platform_Factory().get_factory()
    # print(plat.systeminfo())
    testlist = ["http://www.baidu.com","http://yahoo.com"]

    str1 = ','.join(['https://{}:12379/'.format(i.strip()) for i in testlist if i.strip()])

    print(str1)