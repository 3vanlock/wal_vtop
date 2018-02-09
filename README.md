# wal_vtop

Automate [vtop](https://github.com/MrRio/vtop) theme creation from generated [pywal](https://github.com/dylanaraps/pywal) colors

## About

`wal_vtop` is a small Python utility meant to work with `wal` by reading colors generated from a JSON file and translating them into a JSON-based `vtop` theme file.

## Install

```bash
git clone `https://github.com/elock37/wal_vtop.git`
cd wal_vtop
pip install .
```

### Requirements

* [python3](https://www.python.org/)

    Tested with Python 3.6.4. Uses standard sys calls so should function across all Python 3.

* [pywal](https://github.com/dylanaraps/pywal)

## Use

**Be sure you've run `wal` at least once to generate colors.json file.**

Simply invoke `wal-vtop`
