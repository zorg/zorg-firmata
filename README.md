# Zorg Firmata

[![Package Version](https://img.shields.io/pypi/v/zorg-firmata.svg)](https://pypi.python.org/pypi/zorg-firmata/)
[![Requirements Status](https://requires.io/github/zorg/zorg-firmata/requirements.svg?branch=master)](https://requires.io/github/zorg/zorg-firmata/requirements/?branch=master)
[![Build Status](https://travis-ci.org/zorg/zorg-firmata.svg?branch=master)](https://travis-ci.org/zorg/zorg-firmata)
[![Code Climate](https://codeclimate.com/github/zorg/zorg-firmata/badges/gpa.svg)](https://codeclimate.com/github/zorg/zorg-firmata)
[![Coverage Status](https://coveralls.io/repos/github/zorg/zorg-firmata/badge.svg?branch=master)](https://coveralls.io/github/zorg/zorg-firmata?branch=master)

## What is Firmata?

> Firmata is a protocol for communicating with microcontrollers from software
> on a computer (or smartphone/tablet, etc). The protocol can be implemented
> in firmware on any microcontroller architecture as well as software on any
> computer software package (see list of client libraries below).
> ~ [Firmata Protocol Documentation](https://github.com/firmata/protocol)

## Installation

You can install this library on your machine using PIP.

```
pip install zorg-firmata
```

## Setup

To use this library with your microcontroller, you will need to load the
Standard Firmata software onto it first. See [Uploading StandardFirmata To Arduino](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-StandardFirmata-To-Arduino) for an example of how to do this.

## Examples

Several examples for using the `zorg-firmata` module are available on GitHub.
https://github.com/zorg/zorg-firmata/tree/master/examples

## Notes

This module wraps the [PyMata](https://github.com/MrYsLab/PyMata) library to
provide Firmata support within the Zorg robotics framework.
