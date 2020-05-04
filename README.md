# bnw

Free and easy to use Python library to add some basic effects to images

## Overview

Using this module you can add some simple effects to image:
- black & white mode
- sepia mode
- negative mode

## Installation

You can install bnw with pip

```
$ pip install bnw
```

## Basic Usage

Import and initialization.
```
from bnw import BlackWhite

bnw = BlackWhite()
```
### Basic methods

Every method has two arguments: path to image which you want to edit (`in_path`) and path to the place where you want to save edited image (`out_path`). By default out path equals `None`, so you don't have to specify it if you just want to replace an image.

-   `to_bnw(in_path, out_path=None)` converts image to black and white mode
-   `to_sepia(in_path, out_path=None)` converts image to sepia mode
-   `to_negative(in_path, out_path=None)` converts image to sepia mode
