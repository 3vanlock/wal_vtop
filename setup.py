"""wal_vtop - setup.py"""
import setuptools

try:
    import wal_vtop
except (ImportError):
    print("error: wal_vtop requires Python 3.5 or greater.")
    quit(1)

VERSION = wal_vtop.VERSION
DOWNLOAD = "https://github.com/elock37/wal_vtop/archive/%s.tar.gz" % VERSION


setuptools.setup(
    name="wal_vtop",
    version=VERSION,
    author="Evan Lock",
    author_email="elock37@gmail.com",
    description=" Automate vtop theme creation from generated pywal colors",
    license="MIT",
    url="https://github.com/elock37/wal_vtop",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires="pywal >= 0.6.7",
    scripts=['wal_vtop.py'],
    entry_points={
        "console_scripts": ["wal-vtop=wal_vtop:main"]
    },
    python_requires=">=3.5",
    include_package_data=True
)
