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
#         Yun, Liu<yunx.liu@intel.com>

import unittest
import os
import comm
import zipfile
import shutil
from xml.etree import ElementTree
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_package_basic(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "stable")
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("target android", output[0])
        self.assertNotIn("candle", output[0])
        self.assertNotIn("light", output[0])
        self.assertIn(version, output[0])

    def test_create_package_missing_icon_startUrl(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_stable(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=stable " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "stable")
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn(version, output[0])

    def test_create_package_beta(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=beta " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "beta")
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn(version, output[0])

    def test_create_package_canary(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=canary " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "canary")
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn(version, output[0])

    def test_create_package_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkVersion + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_pathToRelease(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_package_release(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --release=true " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_crosswalkdir(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        crosswalkdir = zipfile.ZipFile(comm.crosswalkzip,'r')
        for file in crosswalkdir.namelist():
            crosswalkdir.extract(file, r'.')
        crosswalkdir.close()
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip[:comm.crosswalkzip.index(".zip")] + "/ " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        shutil.rmtree(comm.crosswalkzip[:comm.crosswalkzip.index(".zip")])
        self.assertEquals(return_code, 0)

    def test_create_package_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " --manifest=org.xwalk.test " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        with open(comm.ConstPath + "/../testapp/start_url/manifest.json") as json_file:
            data = json.load(json_file)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(return_code, 0)
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")

    def test_create_package_reading_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " --manifest '{ \"xwalk_package_id\": \"org.xwalk.test\", \"start_url\": \"start.html\" }' " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        with open(comm.ConstPath + "/../testapp/start_url/manifest.json") as json_file:
            data = json.load(json_file)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(return_code, 0)
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")

    def test_create_package_keep(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " --keep " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("app", os.listdir(projectDir))
        self.assertIn("prj", os.listdir(projectDir))

def test_create_package_k(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android" + comm.ANDROID_MODE + " -k " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("app", os.listdir(projectDir))
        self.assertIn("prj", os.listdir(projectDir))

if __name__ == '__main__':
    unittest.main()
