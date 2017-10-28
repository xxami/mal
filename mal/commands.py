#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

"""These function serve as an entry point for the several subcommands
of mal. All they do is basically call the functions that do actual work
in the core module."""

# stdlib
import sys

# self-package
from mal import core
from mal import login as _login
from mal import setup


def search(mal, args):
    """Search MAL (not just the user) anime database."""
    type = 'anime' if not args.manga else 'manga'
    core.search(mal, args.anime_regex.lower(), type=type, full=args.extend)


def filter(mal, args):
    """Search and find an anime in the users list."""
    type = 'anime' if not args.manga else 'manga'
    core.find(mal, args.anime_regex.lower(), type=type, extra=args.extend, user=args.user)


def increase(mal, args):
    type = 'anime' if not args.manga else 'manga'
    core.progress_update(mal, args.anime_regex.lower(), args.count, type=type)


def decrease(mal, args):
    type = 'anime' if not args.manga else 'manga'
    core.progress_update(mal, args.anime_regex.lower(), -args.count, type=type)


def login(mal, args):
    """Creates login credentials so that next time the program is called
    it can log in right at the start without any problem."""
    _login.create_credentials()
    sys.exit(0)


def list(mal, args):
    """Show all the animes on the users list."""
    # . matches any character except line breaks
    # + matches one or more occurences of the previous character
    type = 'anime' if not args.manga else 'manga'
    core.find(mal, '.+', args.section, type=type, extra=args.extend, user=args.user)


def drop(mal, args):
    """Drop a anime from lists based in a regex expression"""
    core.drop(mal, args.anime_regex)


def stats(mal, args):
    type = 'anime' if not args.manga else 'manga'
    """Show the users anime watching statistics as presented on MAL."""
    core.stats(mal, args.user, type=type)


def add(mal, args):
    """Add an anime with a certain status to the list."""
    core.add(mal, args.anime_regex.lower(), status=args.status)


def config(mal, args):
    # Show the current config file
    setup.print_config()
