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

## Configuration File
Essentially every component of the UI is customizable, all through a JSON configuration file. An [example file](/example_config.json) is available within the code repository.

### Defined config file
To define a configuration file, use the `jsonurl` script parameter.
```bash
--jsonurl=https://fake.domain.com/path/to/config.json
```
```bash
--jsonurl=file:///path/to/local/config.json
```

### Default config file
If you prefer to deploy the configuration file to each client, it needs to be placed in the `Resources` directory and named `umad.json`. If this file exists, `jsonurl` does not need to be set.

## Preferences
A description of each preference is listed below.

### Cutoff date
Cut off date in UTC.

```json
"cut_off_date": "2018-12-31-00:00"
```

### Cut off date warning
This is the number, in days, of when to start the initial UI warning. When this set of days passes, the user will be required to hit an "I Understand" button, followed by the "Close" button to exit out of the UI.

```json
"cut_off_date_warning": 14
```

### Due date text
This is the bolded portion of the UI towards the top under the ["titletext".](#title-text)

```json
"due_date_text": "MDM Enrollment is required by 12/31/2018 (No Restart Required)"
```

### DEP failure text
If a user has a DEP capable device, but they are passed the enrollment window, they will have an option to manually enroll.

This is the first set of text above the enrollment button.

```json
"dep_failure_text": "Not getting this notification?"
```

### DEP failure subtext
If a user has a DEP capable device, but they are past the enrollment window, they will have an option to manually enroll.

This is the second set of text above the enrollment button.

```json
"dep_failure_subtext": "You can also enroll manually below:"
```

### Enable enrollment button
Always show the manual enrollment button, DEP or not.

```json
"enable_enrollment_button": true
```

### Honor DND settings
If a device is DEP capable, umad will not honor DoNotDisturb settings so the nag can actually appear.

If the admin wants to honor DoNotDisturb for DEP devices, use this feature.

Non-DEP devices will honor the users DND settings

```json
"honor_dnd_settings": true
```

### Logo path
You can replace the included company_logo.png with your own company_logo.png or you can configure a custom Path
with the following string:

```json
"logo_path": "/Some/Custom/Path/company_logo.png"
```

### Manual enrollment text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the bolded text that takes place of the DEP or UAMDM screenshot.

```json
"manual_enrollment_text": "Manual Enrollment Required"
```

### Manual enrollment h1 text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the first set of text above the enrollment button.

```json
"manualenroll_h1_text": "Want this box to go away?"
```

### Manual enrollment h2 text
If a user does not have a DEP capable device, they will have the option to manually enroll.
<i>Authentication may be required for manual enrollment.</i>

This is the second set of text above the enrollment button.

```json
"manualenroll_h2_text": "Click on the Manual Enrollment button below."
```

### Manual enrollment URL
Configure the Manual Enrollment button with a custom URL.
```json
"enrollment_url": "https://apple.com"
```

### More info URL
When you see the Manual Enrollment button, you can customize a URL directing the users to more information.
```json
"more_info_url": "https://google.com"
```

### Nag screenshot path
You can modify the LaunchAgent adding your custom path or just replace the included nag_ss.png with your own .png.
(remember to name the file nag_ss.png if you are not using a custom path)
```json
"nag_ss_path": "/Some/Custom/Path/nag_ss.png"
```

### No timer
Use this setting if you <b>DO NOT</b> want to restore the umad GUI to the front of a user's window.

```json
"no_timer": true
```

### Paragraph 1 text
This is the text for the first paragraph. 160 character limit.
```json
"paragraph1": "If you do not enroll into MDM you will lose the ability to connect to Wi-Fi, VPN and Managed Software Center."
```

### Paragraph 2 text
This is the text for the second paragraph. 160 character limit.
```json
"paragraph2": "To enroll, just look for the below notification, and click Details. Once prompted, log in with your username and password."
```

### Paragraph 2 text
This is the text for the third paragraph. 160 character limit.
```json
"paragraph3": "To enroll, just look for the below notification, and click Details. Once prompted, log in with your OneLogin username and password."
```

### Profile identifier
This is the profile identifier for < 10.13 machines to check for enrollment. Should you not set this value, umad will attempt to look for a profile installed on the machine with the _PayloadType_ of `com.apple.mdm`

```json
"profile_identifier": "B68ABF1E-70E2-43B0-8300-AE65F9AFA330"
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
```json
"subtitle_text": "A friendly reminder from your local IT team"
```

### System Preferences H1 text
Should the user have a 10.13.4+ device that is not User Approved MDM, they will be notified that they need to approve the MDM.

This is the first set of text above the system preferences button.
```json
"sysprefs_h1_text": "Want this box to go away?"
```

### System Preferences H2 text
Should the user have a 10.13.4+ device that is not User Approved MDM, they will be notified that they need to approve the MDM.

This is the second set of text above the system preferences button.
```json
"sysprefs_h2_text": "Open System Preferences and approve Device Management."
```

### Title text
This is the main, bolded text at the very top.
```json
"title_text": "MDM Enrollment"
```

### Timer Day 1
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is one day or less, this timer becomes active.
```json
"timer_day1": 600
```

### Timer Day 3
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is three days or less from current date.
```json
"timer_day3": 7200
```

### Timer Elapsed
After the user interacts with umad GUI, (such as clicking the "I understand" button) timer elapsed controls when the UI
will display again.

This will occur indefinitely until the MDM is enrolled.
```json
"timer_elapsed": 10
```

### Timer Final
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

This is when the MDM cutoff date is one hour or less
```json
"timer_final": 60
```

### Timer Initial
The time, in seconds, to restore the umad GUI to the front of a user's window. This will occur indefinitely until the UI is closed or MDM is enrolled.

When the MDM cutoff date is over three days.
```json
"timer_initial": 14400
```

### Timer MDM
The time, in seconds, to check if the device is enrolled into MDM.

```json
"timer_mdm": 5
```

### User Approved MDM paragraph 1 text
This is the text for the first paragraph on the user Approved MDM UI.
```json
"uamdm_paragraph1": "Thank you for enrolling your device into MDM. We sincerely appreciate you doing this in a timely manner."
```

### User Approved MDM paragraph 2 text
This is the text for the second paragraph on the user Approved MDM UI.
```json
"uamdm_paragraph2": "Unfortunately, your device has been detected as only partially enrolled into our system."
```

### User Approved MDM paragraph 3 text
This is the text for the third paragraph on the user Approved MDM UI.
```json
"uamdm_paragraph3": "Please go to System Preferences -> Profiles, click on the Device Enrollment profile and click on the approve button."
```

### User Approved MDM screenshot path
You can customize the uamdm screenshot path. Option 2, just replace the included uamdm_ss.png with your own .png.  Make sure you name the .png the same as the original and place it back into `umad/Resources/`  .
```json
"ua_ss_path": "/Some/Custom/Path/uamdm_ss.png"
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
