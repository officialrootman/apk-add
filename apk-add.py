import os

packages = [
    "python",
    "python2",
    "python3",
    "git",
    "curl",
    "vim",
    "nano",
    "htop",
    "wget",
    "bash",
    "openssh",
    "zip",
    "unzip",
    "make",
    "gcc",
    "g++",
    "libc-dev",
    "linux-headers",
    "ca-certificates",
    "openssl",
    "perl",
    "ruby",
    "nodejs",
    "npm"
]

for package in packages:
    os.system(f"apk add {package}")