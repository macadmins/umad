# UMAD (macadmin's Slack #umad)
[U]niversal
[M]DM
[A]pproval
[D]ialog

## Embedded Python
As of v2.0, UMAD now uses its own embedded python (currently v3.8). This is due to Apple's upcoming removal of Python2.

`FoundationPlist` has been replaced by Python 3's version of `plistlib`

Nibbler has been updated to support python 3.

### Building embedded python framework

To reduce the size of the git repository, you **must** create your own Python. To do this, simply run the `./build_python_framework` script within the repository.

This process was tested on Catalina only.

```
./build_python_framework

Cloning relocatable-python tool from github...
Cloning into '/tmp/relocatable-python-git'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 78 (delta 12), reused 19 (delta 9), pack-reused 50
Unpacking objects: 100% (78/78), done.
Downloading https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg...

...

Done!
Customized, relocatable framework is at /Library/umad/Python.framework
Moving Python.framework to umad munki-pkg payload folder
Taking ownership of the file to not break git
```

## Purpose
A Professional Tool to help users with getting pre-existing devices enrolled into MDM.

## Screenshots

### DEP
![Screenshot DEP](/images/ss_dep.png?raw=true)

### Manual
![Screenshot Manual](/images/ss_manual.png?raw=true)

### UAMDM
![Screenshot UAMDM](/images/ss_uamdm.png?raw=true)

### Simplified Diagram
![Simplified Diagram](/images/umad_diagram.png?raw=true)

### Notes
You will need to use [munki-pkg](https://github.com/munki/munki-pkg) to build this package.

Because of the way git works, umad will not contain the `Logs` folder required for the postinstall to complete.
In order to create a properly working package, you will need to run the following command:
`munkipkg --sync /path/to/cloned_repo/mdm/umad`

## OS Support v1
The following operating system and versions have been tested.
- 10.10.0 [Note 1](https://github.com/AnotherToolAppleShouldHaveProvided/umad/issues/11), 10.10.5 - [Note 2](https://github.com/AnotherToolAppleShouldHaveProvided/umad/issues/10)
- 10.11.0, 10.11.6
- 10.12.0, 10.12.6 (10.12 is very unreliable with DEP nagging)
- 10.13.0 10.13.3, 10.13.6
- 10.14.0
- 10.15

## OS Support v2 (embedded python)
The following operating system and versions have been tested with the embedded python.
- 10.14
- 10.15

## Getting started
To start, you can use the default settings in `/Library/LaunchAgent/com.anothertoolappleshouldhaveprovided.umad.plist`

Essentially every component of the UI is customizable, using the above LaunchAgent.  
* Create your .pkg with munki-pkg and install on your target workstation.
* Open terminal.
<i>example</i>

`/Library/Application Support/umad/Resources/umad --cutoffdate 2018-9-7-17:00
`
<i>sets the cutoff date to September 7th at 5pm</i>

### Cutoff date
Cut off date in UTC.

```xml
<string>--cutoffdate</string>
<string>2018-12-31-17:00</string>
```

### Cut off date warning
This is the number, in days, of when to start the initial UI warning. When this set of days passes, the user will be required to hit an "I Understand" button, followed by the "Close" button to exit out of the UI.

```xml
<string>--cutoffdatewarning</string>
<string>14</string>
```

### Due date text
This is the bolded portion of the UI towards the top under the ["titletext".](#title-text)

```xml
<string>--duedatetext</string>
<string>MDM Enrollment is required by 12/31/2018 (No Restart Required)</string>
```

### DEP failure text
If a user has a DEP capable device, but they are past the enrollment window, they will have an option to manually enroll.

This is the first set of text above the enrollment button.

```xml
<string>--depfailuretext</string>
<string>Not getting this notification?</string>
```

### DEP failure subtext
If a user has a DEP capable device, but they are past the enrollment window, they will have an option to manually enroll.

This is the second set of text above the enrollment button.

```xml
<string>--depfailuresubtext</string>
<string>You can also enroll manually below:</string>
```

### Enable enrollment button
Always show the manual enrollment button, DEP or not.

```xml
<string>--enableenrollmentbutton</string>
```

### Honor DND settings
If a device is DEP capable, umad will not honor DoNotDisturb settings so the nag can actually appear.

If the admin wants to honor DoNotDisturb for DEP devices, use this feature.

Non-DEP devices will honor the users DND settings

```xml
<string>--honordndsettings</string>
```

### Logo path
You can replace the included company_logo.png with your own company_logo.png or you can configure a custom Path
with the following string:

```xml
<string>--logopath</string>
<string>/Some/Custom/Path/company_logo.png</string>
```

### Manual enrollment text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the bolded text that takes place of the DEP or UAMDM screenshot.

```xml
<string>--manualenrollmenttext</string>
<string>Manual Enrollment Required</string>
```

### Manual enrollment h1 text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the first set of text above the enrollment button.

```xml
<string>--manualenrollh1text</string>
<string>Want this box to go away?</string>
```

### Manual enrollment h2 text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the second set of text above the enrollment button.

```xml
<string>--manualenrollh2text</string>
<string>Click on the Manual Enrollment button below.</string>
```

### Manual enrollment URL
Configure the Manual Enrollment button with a custom URL.
```xml
<string>--manualenrollmenturl</string>
<string>https://apple.com</string>
```

### More info URL
When you see the Manual Enrollment button, you can customize a URL directing the users to more information.
```xml
<string>--moreinfourl</string>
<string>https://google.com</string>
```

### Nag screenshot path
You can modify the LaunchAgent adding your custom path or just replace the included nag_ss.png with your own .png.
(remember to name the file nag_ss.png if you are not using a custom path)
```xml
<string>--nagsspath</string>
<string>/Some/Custom/Path/nag_ss.png</string>
```

### No timer
Use this setting if you <b>DO NOT</b> want to restore the umad GUI to the front of a user's window.

```xml
<string>--notimer</string>
```

### Paragraph 1 text
This is the text for the first paragraph. 160 character limit.
```xml
<string>--paragraph1</string>
<string>If you do not enroll into MDM you will lose the ability to connect to Wi-Fi, VPN and Managed Software Center.</string>
```

### Paragraph 2 text
This is the text for the second paragraph. 160 character limit.
```xml
<string>--paragraph2</string>
<string>To enroll, just look for the below notification, and click Details. Once prompted, log in with your username and password.</string>
```

### Paragraph 2 text
This is the text for the third paragraph. 160 character limit.
```xml
<string>--paragraph3</string>
<string>To enroll, just look for the below notification, and click Details. Once prompted, log in with your OneLogin username and password.</string>
```

### Profile identifier
This is the profile identifier for < 10.13 machines to check for enrollment. Should you not set this value, umad will attempt to look for a profile installed on the machine with the _PayloadType_ of `com.apple.mdm`

```xml
<string>--profileidentifier</string>
<string>B68ABF1E-70E2-43B0-8300-AE65F9AFA330</string>
```

To get this value, run the following command on a computer with your MDM profile installed: `profiles -C -o stdout-xml`

Look for the MDM profile and notate the identifier. Some MDMs may use a UUID for this value.

Some examples:
```xml
<dict>
	<key>ProfileDescription</key>
	<string>MDM profile</string>
	<key>ProfileDisplayName</key>
	<string>MDM Profile</string>
	<key>ProfileIdentifier</key>
	<string>220cad8d-c273-422f-afcb-9740857b38a0</string>
</dict>
```

```xml
<dict>
	<key>ProfileDescription</key>
	<string>MDM profile</string>
	<key>ProfileDisplayName</key>
	<string>MDM Profile</string>
	<key>ProfileIdentifier</key>
	<string>com.awesome.mdm.profile</string>
</dict>
```

### Sub-title text
This is the text right under the main title.
```xml
<string>--subtitletext</string>
<string>A friendly reminder from your local IT team</string>
```

### System Preferences H1 text
Should the user have a 10.13.4+ device that is not User Approved MDM, they will be notified that they need to approve the MDM.

This is the first set of text above the system preferences button.
```xml
<string>--sysprefsh1text</string>
<string>Want this box to go away?</string>
```

### System Preferences H2 text
Should the user have a 10.13.4+ device that is not User Approved MDM, they will be notified that they need to approve the MDM.

This is the second set of text above the system preferences button.
```xml
<string>--sysprefsh2text</string>
<string>Open System Preferences and approve Device Management.</string>
```

### Title text
This is the main, bolded text at the very top.
```xml
<string>--titletext</string>
<string>MDM Enrollment</string>
```

### Timer Day 1
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is one day or less, this timer becomes active.
```xml
<string>--timerday1</string>
<string>600</string>
```

### Timer Day 3
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is three days or less from current date.
```xml
<string>--timerday3</string>
<string>7200</string>
```

### Timer Elapsed
After the user interacts with umad GUI, (such as clicking the "I understand" button) timer elapsed controls when the UI
will display again.

This will occur indefinitely until the MDM is enrolled.
```xml
<string>--timerelapsed</string>
<string>10</string>
```

### Timer Final
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

This is when the MDM cutoff date is one hour or less
```xml
<string>--timerfinal</string>
<string>60</string>
```

### Timer Initial
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is over three days.
```xml
<string>--timerinital</string>
<string>14400</string>
```

### Timer MDM
The time, in seconds, to check if the device is enrolled into MDM.

```xml
<string>--timermdm</string>
<string>5</string>
```

### User Approved MDM paragraph 1 text
This is the text for the first paragraph on the user Approved MDM UI.
```xml
<string>--uamdmparagraph1</string>
<string>Thank you for enrolling your device into MDM. We sincerely appreciate you doing this in a timely manner.</string>
```

### User Approved MDM paragraph 2 text
This is the text for the second paragraph on the user Approved MDM UI.
```xml
<string>--uamdmparagraph2</string>
<string>Unfortunately, your device has been detected as only partially enrolled into our system.</string>
```

### User Approved MDM paragraph 3 text
This is the text for the third paragraph on the user Approved MDM UI.
```xml
<string>--uamdmparagraph3</string>
<string>Please go to System Preferences -> Profiles, click on the Device Enrollment profile and click on the approve button.</string>
```

### User Approved MDM screenshot path
You can customize the uamdm screenshot path. Option 2, just replace the included uamdm_ss.png with your own .png.  Make sure you name the .png the same as the original and place it back into `umad/Resources/`  .
```xml
<string>--uasspath</string>
<string>/Some/Custom/Path/uamdm_ss.png</string>
```

## Tips, Tricks, and Troubleshooting

* <b><i>I made changes to the default LaunchAgent and now the UI isn't appearing?</b></i>

	Make sure you unload, and reload the LaunchAgent after making changes.

* <b><i>Where is the logging located?</b></i>

	`/Library/Application Support/umad/umad.log`

* <b><i>Why isn't the log file there?</b></i>

	Remember to unload and reload the LaunchAgent.


## Credits
This tool would not be possible without [nibbler](https://github.com/pudquick/nibbler), written by [Michael Lynn](https://twitter.com/mikeymikey)
