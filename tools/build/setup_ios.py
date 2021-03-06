#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import os
import sys
import shutil
import commands
import fileinput
import traceback
from shutil import copytree
from optparse import OptionParser

SCRIPT_PATH = os.path.realpath(__file__)
CONST_PATH = os.path.dirname(SCRIPT_PATH)
submodule_cmd = "git submodule update --init --recursive"

# Clone the project ios-extensions-crosswalk
def clone_submodule(tag=None):
    print "Cloning into submodule repos..."
    tpstatus = commands.getstatusoutput(submodule_cmd)
    if tpstatus[0] == 0:
        print "Clone into submodule repos done!"
        if tag:
            tagstatus = commands.getstatusoutput(
                "git checkout %s" % tag)
            print "Checking out %s" % tag
            if tagstatus[0] == 0:
                print "The branch is %s" % tag
            else:
                print "Please check if the tag is exist"
                print tagstatus[1]
        else:
            print "The project ios-extensions-crosswalk default "\
            "branch is master"
    else:
        print "Clone into the submodule failed!"
        print tpstatus[1]

# Clone project mobileSpec-crosswalk
def clone_mobilespec(tag=None):
    try:
        os.chdir(CONST_PATH)
        clone_url = "https://git.coding.net/jondong/mobileSpec-crosswalk.git"
        msstatus = commands.getstatusoutput("git clone %s" % clone_url)
        print "Cloning into mobileSpec..."
        if msstatus[0] == 0:
            print "Clone into mobileSpec done!"
            os.chdir("mobileSpec-crosswalk")
            clone_submodule(tag=None)
            print "Copying the project ios-extensions-crosswalk to the same "\
                    "path with mobileSpec-crosswalk"
            os.chdir(CONST_PATH)
            try:
                shutil.copytree(CONST_PATH + "/mobileSpec-crosswalk/" \
                    "ios-extensions-crosswalk", CONST_PATH + "/ios-extensions-crosswalk")
            except:
                print traceback.print_exc()
            if os.path.exists(CONST_PATH + "/ios-extensions-crosswalk"):
                print "Copy the project ios-extensions-crosswalk done!"
            else:
                print "Copy the project ios-extensions-crosswalk failed!"
        else:
            print "Clone mobileSpec failed"
            print msstatus[1]
            sys.exit(1)
    except Exception as e:
        print e, "Clone into mobileSpec-crosswalk failed!"
        sys.exit(1)

#Clone project HexGL-iOS
def clone_hexgl(tag=None):
    os.chdir(CONST_PATH)
    hexgl_url = "https://github.com/otcshare/HexGL-iOS.git"
    hexgl_status = commands.getstatusoutput("git clone %s" % hexgl_url)
    print "Cloning into HexGL..."
    if hexgl_status[0] == 0:
        print "Clone into HexGL done!"

    else:
        print "Clone into HexGL failed"
        print hexgl_status[1]

def main():
    try:
        global dest, uuid
        usage = "Usage: ./%prog -d 'platform=iOS Simulator,"\
        "name=iPhone 6,OS=8.3'"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-d",
            "--dest",
            dest = "destination",
            help = 'specify the destination that you want to use,' \
                   'the options should be within double quotations,' \
                   'e.g. "platform=iOS Simulator,name=iPhone 6;OS=8.3",' \
                   '"platform=iOS,name=iPad Air"'
        )
        opts_parser.add_option(
            "-u",
            "--uuid",
            dest = "deviceuuid",
            help = "specify the uuid of the test devices"
        )
        opts_parser.add_option(
            "-t",
            "--tag",
            dest = "tag",
            help = "specify the tag that you want to checkout, " \
            "default branch is master"
        )

        if len(sys.argv) == 1:
            sys.argv.append("-h")

        (PARAMETERS, args) = opts_parser.parse_args()
        os.chdir(CONST_PATH)
        clone_mobilespec(PARAMETERS.tag)
        dest = PARAMETERS.destination
        #print 'dest', dest
        uuid = PARAMETERS.deviceuuid
        #print 'uuid', uuid

    except Exception as e:
        print("Get wrong options: %s, exit ..." % e)
        sys.exit(1)

if __name__ == '__main__':
    main()
