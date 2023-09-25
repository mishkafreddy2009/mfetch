#!/usr/bin/env python

import platform


class MinimalFetch():
    def get_ascii(self):
        self.ascii_logo = f"""
       __   _
     _(  )_( )_ {" "*4}distro: {self.distro_name}
    (_   _    _){" "*4}uptime: {int(self.uptime_minutes)} min
   / /(_) (__)
  / / / / / /
 / / / / / /
        """

    def get_uptime(self):
        with open('/proc/uptime', 'r') as f:
            self.uptime_minutes = float(f.readline().split()[0]) // 60

    def get_distro(self):
        self.distro_name = list(platform.freedesktop_os_release().values())[0].lower()

    def output(self):
        print(self.ascii_logo)


def get_fetch():
    mf = MinimalFetch()
    mf.get_distro()
    mf.get_uptime()
    mf.get_ascii()

    mf.output()

def main():
    get_fetch()

if __name__ == "__main__":
    main()
