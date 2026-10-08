name = "witr"
version = "0.3.4"
description = "Why is this running? Process ancestry and diagnostics"
tools = ["witr"]


def commands():
    env.PATH.prepend("{root}/payload/bin")
