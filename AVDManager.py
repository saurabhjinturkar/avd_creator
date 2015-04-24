import pexpect

class AVDManager():

    def create_avd(self, avd_name, target, customize_profile, configuration):

        android_tool_loc = '/home/saurabh/Downloads/android-sdk-linux/tools/android create avd'
        android_process_name = android_tool_loc + ' -n ' + str(avd_name) + ' -t ' + str(target)
        child = pexpect.spawn(android_process_name)

        base_log_location = '/home/saurabh/.android/avd/'
        log_location = base_log_location + str(avd_name) + '.log'
        fout = open(log_location,'wb')
        child.logfile = fout

        # configuration = {'hw.ramSize':'1024'}

        child.expect('Do you wish to create a custom hardware profile .*')
        child.sendline(customize_profile)

        index = child.expect(['avd.name.*', pexpect.EOF])

        if index == 1: 
            exit()

        child.sendline(configuration['avd.name'] if configuration.has_key('avd.name') is True  else '')

        child.expect('disk.cachePartition \[yes\]: *')
        child.sendline(configuration['disk.cachePartition'] if configuration.has_key('disk.cachePartition') is True else '')

        child.expect('disk.cachePartition.path \[\]:.*')
        child.sendline(configuration['disk.cachePartition.path'] if configuration.has_key('disk.cachePartition.path') is True else '')

        child.expect('disk.cachePartition.size.*')
        child.sendline(configuration['disk.cachePartition.size'] if configuration.has_key('disk.cachePartition.size') is True else '')

        child.expect('disk.dataPartition.initPath.*')
        child.sendline(configuration['disk.dataPartition.initPath'] if configuration.has_key('disk.dataPartition.initPath') is True else '')

        child.expect('disk.dataPartition.path.*')
        child.sendline(configuration['disk.dataPartition.path'] if configuration.has_key('disk.dataPartition.path') is True else '')

        child.expect('disk.dataPartition.size.*')
        child.sendline(configuration['disk.dataPartition.size'] if configuration.has_key('disk.dataPartition.size') is True else '')

        index = child.expect(['disk.ramdisk.path \[\]:', pexpect.TIMEOUT], timeout = 5)
        if index == 0:
            child.sendline(configuration['disk.ramdisk.path'] if configuration.has_key('disk.ramdisk.path') is True else '')

        child.expect('disk.snapStorage.path.*') 
        child.sendline(configuration['disk.snapStorage.path'] if configuration.has_key('disk.snapStorage.path') is True else '')

        child.expect('disk.systemPartition.initPath.*')
        child.sendline(configuration['disk.systemPartition.initPath'] if configuration.has_key('disk.systemPartition.initPath') is True else '')

        child.expect('disk.systemPartition.path.*')
        child.sendline(configuration['disk.systemPartition.path'] if configuration.has_key('disk.systemPartition.path') is True else '')

        child.expect('disk.systemPartition.size.*')
        child.sendline(configuration['disk.systemPartition.size'] if configuration.has_key('disk.systemPartition.size') is True else '')

        child.expect('hw.accelerometer \[yes\]:.*')
        child.sendline(configuration['hw.accelerometer'] if configuration.has_key('hw.accelerometer') is True else '')

        child.expect('hw.audioInput \[yes\]:.*')
        child.sendline(configuration['hw.audioInput'] if configuration.has_key('hw.audioInput') is True else '')

        child.expect('hw.audioOutput \[yes\]:.*')
        child.sendline(configuration['hw.audioOutput'] if configuration.has_key('hw.audioOutput') is True else '')

        child.expect('hw.battery \[yes\]:.*')
        child.sendline(configuration['hw.battery'] if configuration.has_key('hw.battery') is True else '')

        child.expect('hw.camera.back \[emulated\]:.*')
        child.sendline(configuration['hw.camera.back'] if configuration.has_key('hw.camera.back') is True else '')

        child.expect('hw.camera.front \[none\]:.*')
        child.sendline(configuration['hw.camera.front'] if configuration.has_key('hw.camera.front') is True else '')

        child.expect('hw.cpu.arch \[arm\]:.*')
        child.sendline(configuration['hw.cpu.arch'] if configuration.has_key('hw.cpu.arch') is True else '')

        child.expect('hw.cpu.model \[\]:.*')
        child.sendline(configuration['hw.cpu.model'] if configuration.has_key('hw.cpu.model') is True else '')

        child.expect('hw.dPad \[yes\]:.*')
        child.sendline(configuration['hw.dPad'] if configuration.has_key('hw.dPad') is True else '')

        child.expect('hw.gps \[yes\]:.*')
        child.sendline(configuration['hw.gps'] if configuration.has_key('hw.gps') is True else '')

        child.expect('hw.gpu.enabled \[no\]:.*')
        child.sendline(configuration['hw.gpu.enabled'] if configuration.has_key('hw.gpu.enabled') is True else '')

        child.expect('hw.gsmModem \[yes\]:.*')
        child.sendline(configuration['hw.gsmModem'] if configuration.has_key('hw.gsmModem') is True else '')

        child.expect('hw.initialOrientation \[portrait\]:.*')
        child.sendline(configuration['hw.initialOrientation'] if configuration.has_key('hw.initialOrientation') is True else '')

        child.expect('hw.keyboard \[no\]:.*')
        child.sendline(configuration['hw.keyboard'] if configuration.has_key('hw.keyboard') is True else '')

        child.expect('hw.keyboard.charmap \[qwerty2\]:.*')
        child.sendline(configuration['hw.keyboard.charmap'] if configuration.has_key('hw.keyboard.charmap') is True else '')

        child.expect('hw.keyboard.lid \[yes\]:.*')
        child.sendline(configuration['hw.keyboard.lid'] if configuration.has_key('hw.keyboard.lid') is True else '')

        child.expect('hw.lcd.backlight \[yes\]:.*')
        child.sendline(configuration['hw.lcd.backlight'] if configuration.has_key('hw.lcd.backlight') is True else '')

        child.expect('hw.lcd.density \[160\]:.*')
        child.sendline(configuration['hw.lcd.density'] if configuration.has_key('hw.lcd.density') is True else '')

        child.expect('hw.lcd.depth \[16\]:.*')
        child.sendline(configuration['hw.lcd.depth'] if configuration.has_key('hw.lcd.depth') is True else '')

        child.expect('hw.lcd.height \[640\]:.*')
        child.sendline(configuration['hw.lcd.height'] if configuration.has_key('hw.lcd.height') is True else '')

        child.expect('hw.lcd.width \[320\]:.*')
        child.sendline(configuration['hw.lcd.width'] if configuration.has_key('hw.lcd.width') is True else '')

        child.expect('hw.mainKeys \[yes\]:.*')
        child.sendline(configuration['hw.mainKeys'] if configuration.has_key('hw.mainKeys') is True else '')

        child.expect('hw.ramSize \[0\]:.*')
        child.sendline(configuration['hw.ramSize'] if configuration.has_key('hw.ramSize') is True else '')

        child.expect('hw.screen \[touch\]:.*')
        child.sendline(configuration['hw.screen'] if configuration.has_key('hw.screen') is True else '')

        child.expect('hw.sdCard \[yes\]:.*')
        child.sendline(configuration['hw.sdCard'] if configuration.has_key('hw.sdCard') is True else '')

        child.expect('hw.sdCard.path \[\]:.*')
        child.sendline(configuration['hw.sdCard.path'] if configuration.has_key('hw.sdCard.path') is True else '')

        child.expect('hw.sensors.magnetic_field \[yes\]:.*')
        child.sendline(configuration['hw.sensors.magnetic_field'] if configuration.has_key('hw.sensors.magnetic_field') is True else '')

        child.expect('hw.sensors.orientation \[yes\]:.*')
        child.sendline(configuration['hw.sensors.orientation'] if configuration.has_key('hw.sensors.orientation') is True else '')

        child.expect('hw.sensors.proximity \[yes\]:.*')
        child.sendline(configuration['hw.sensors.proximity'] if configuration.has_key('hw.sensors.proximity') is True else '')

        child.expect('hw.sensors.temperature \[yes\]:.*')
        child.sendline(configuration['hw.sensors.temperature'] if configuration.has_key('hw.sensors.temperature') is True else '')

        child.expect('hw.trackBall \[yes\]:.*')
        child.sendline(configuration['hw.trackBall'] if configuration.has_key('hw.trackBall') is True else '')

        child.expect('hw.useext4 \[yes\]:.*')
        child.sendline(configuration['hw.useext4'] if configuration.has_key('hw.useext4') is True else '')

        child.expect('kernel.newDeviceNaming \[autodetect.*\].*')
        child.sendline(configuration['kernel.newDeviceNaming'] if configuration.has_key('kernel.newDeviceNaming') is True else '')

        child.expect('kernel.parameters \[\]:.*')
        child.sendline(configuration['kernel.parameters'] if configuration.has_key('kernel.parameters') is True else '')

        child.expect('kernel.path \[\]:.*')
        child.sendline(configuration['kernel.path'] if configuration.has_key('kernel.path') is True else '')

        child.expect('kernel.supportsYaffs2 \[autodetect.*\].*')
        child.sendline(configuration['kernel.supportsYaffs2'] if configuration.has_key('kernel.supportsYaffs2') is True else '')

        child.expect('vm.heapSize \[0\]:.*')
        child.sendline(configuration['vm.heapSize'] if configuration.has_key('vm.heapSize') is True else '')

        child.interact()

manager = AVDManager()
manager.create_avd ('test345', 7, 'yes', {"vm.heapSize":"64",}) 
