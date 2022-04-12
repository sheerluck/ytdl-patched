#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yt_dlp

BASH_COMPLETION_FILE = "youtube-dl.bash-completion"
BASH_COMPLETION_TEMPLATE = "devscripts/bash-completion.in"


def build_completion(opt_parser):
    opts_flag = []
    for group in opt_parser.option_groups:
        for option in group.option_list:
            # for every long flag
            opts_flag.append(option.get_opt_string())
    with open(BASH_COMPLETION_TEMPLATE) as f:
        template = f.read()
    with open(BASH_COMPLETION_FILE, "w") as f:
        # just using the special char
        filled_template = template.replace("{{flags}}", " ".join(opts_flag))
        f.write(filled_template)


parser = yt_dlp.parseOpts()[0]
build_completion(parser)
