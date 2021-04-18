# Getting Started With Intel Galileo (Gen 1) On Linux (And Windows) In 2021

## WORD OF ADVICE: Don't do this. There are many newer boards that will serve you better than an Intel Galileo. This is for people who have an Intel Galileo laying around, and just want to tinker.
## Due to issues with old versions of Java, how Intel links tools builds, etc. it took several hours to work through all the roadblocks I ran into.
## You have been warned.

&nbsp;

## Why Linux and Windows?
Exposure. I live and breathe Windows, so I recently purchased a laptop and installed Linux on it so I can become better versed in other ecosystems, ways of doing things, etc. I wanted to this purely on Linux; however, there was so many problems I eventually switched to Windows for part of this.

&nbsp;

## OSes Used
Pop!_OS 20.20

Windows 10

&nbsp;

## These are the resources I used to get started

1) Intel Getting Started Guide: https://www.intel.com/content/www/us/en/support/articles/000005702/boards-and-kits/intel-galileo-boards.html

1) Intel Firmware Update Downloads: https://downloadcenter.intel.com/download/26417/Intel-Galileo-Firmware-Updater-and-Drivers

2) Intel Firmware Update Documentation: https://www.intel.com/content/www/us/en/support/articles/000006258/boards-and-kits/intel-galileo-boards.html

3) 3rd Party Galileo Getting Started Guide: https://learn.sparkfun.com/tutorials/galileo-getting-started-guide/updating-firmware

4) Arduino IDE Downloads: https://www.arduino.cc/en/main/OldSoftwareReleases

&nbsp;

## These are the auxiliary resources I used to get past problems.

* https://learn.sparkfun.com/tutorials/galileo-getting-started-guide/all

* https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/

&nbsp;

## Steps

1) Unbox your Intel Galileo and plug it in. You should see the power light turn on, then see an LED next to the Client USB port turn on. This means USB can be plugged in, and interface to a host computer.

2) **ON WINDOWS**: Install Arduino IDE version **1.8.5**. There are many versions, 1.8.5 is the one I could get to work with my Galileo. https://www.arduino.cc/en/main/OldSoftwareReleases

    **You will need to install all the USB drivers to get your Galileo interfacing with your host computer.**

3) **ON WINDOWS**: Connect your Galileo to your host computer by inserting a USB cable into the Client USB port on your Galileo and plugging the other end into your host computer.

4) **ON WINDOWS**: Launch Arduino IDE

    1) Go to Tools -> Board -> Boards Manager and install the i586 package.
    2) Close the package manager and go to Tools -> Board and select "Intel Galileo"
    3) Go to Tools -> Port and you should see at least one available COM port. If there is only one, that's your Galileo (select it). If there is more than one, you'll have to dig through Device Manager a little bit to figure out what is what (then select the appropriate port).
    4) Close Arduino IDE

    If you got this far, it means that your Galileo and Host can communicate with each other.

5) **ON WINDOWS**: Install Java version **1.8.\*** AKA Java 8. This is used by the Intel firmware updater.

    **In the end I had to uninstall other versions of Java and OpenJDK to get subsequent steps to work.**

6) **ON WINDOWS**: Download and run Intel Firmware Updater https://downloadcenter.intel.com/download/26417/Intel-Galileo-Firmware-Updater-and-Drivers

    1) Make sure the correct COM port is selected (you may have to dig through device manager to confirm you're connected to your Galileo)
    2) The "Current Board Firmware" will likely have a weird version number (ex: 738)
    3) The "Update Firmware Version" should say "1.1.0" (the last version Intel provided)
    4) Click "Update Firmware". The update process may take a few minutes.

7) **ON WINDOWS**: Make sure the Arduino can be programmed

    1) Launch Arduino IDE
    2) Make sure that the board and port are configured correctly (see 4.2, and 4.3 above)
    3) Open the Blink example at File -> Examples -> 01.Basics -> Blink. This will open a new window.
    4) Click the Verify button (Checkmark in a circle) to make sure the Blink example can compile.
    5) Click the Upload button (Right arrow in a circle), and wait for the transfer to complete.

    If everything is working correctly you should see an LED on your Galileo start to blink.

**If you don't want to use Linux, you stop here, and use your Arduino IDE with your Galileo.** If you want to use Linux, continue on.

8) Install Arduino IDE https://www.arduino.cc/en/software

9) Install Intel Packages In Arduino IDE (**NOTE: THIS WILL FAIL BUT DO IT ANYWAY**)

    1) Go to Tools -> Board -> Boards Manager and install the i586 package. This may break on you. Simply continue.
    2) Close Arduino IDE
    3) Install this fix for Intel's weird linking. https://github.com/majenkotech/IntelFixes/blob/master/fixgalileo.sh
    4) Open Arduino IDE and reinstall the i586 package
    5) Close Arduino IDE

10) Plug your Galileo into you Linux host computer, then from your terminal run `ls /dev | grep ttyACM`. If only one entry appears, then that is your Galileo's tty connection. If it doesn't show up, you might need to wait a several seconds for it show up, in which case you'll need to run `ls /dev | grep ttyACM` again. Most likely the Galileo will appear as ttyACM0.

11) Get the group that your ttyACM connection is a part of, and add your account to that group.

    1) Run 'ls -l /dev/ttyACM0` (replacing ttyACM0 with your connection). In the middle of the result, you will see a group name. In my case, it was "dialout".
    2) Add your user account to the tty group like so `sudo usermod -a -G THE_GROUP_NAME YOUR_USER_NAME` replacing THE_GROUP_NAME with your tty group name, and YOUR_USER_NAME with your user account name (can be found with the `whoami` command).
    3) Sign out of your account
    4) Sign back in
    5) Confirm you're part of the correct group by running `groups` from the terminal. If it doesn't show up in that list, try restarting your computer and re-running through these steps.

12) Connect your Galileo to Arduino IDE

    1) Launch Arduino IDE
    2) From Tools -> Board -> Arduino i586 Boards, select "Intel Galileo"
    3) From Tools -> Port, select your tty Port (ex: /dev/ttyACOM0)

13) Confirm your Galileo can be programmed

    1) Open the Blink example at File -> Examples -> 01.Basics -> Blink. This will open a new window.
    2) Click the Verify button (Checkmark in a circle) to make sure the Blink example can compile.
    3) Click the Upload button (Right arrow in a circle), and wait for the transfer to complete.
