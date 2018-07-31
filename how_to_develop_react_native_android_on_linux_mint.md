## Notes

Developing Android apps with React Native on Linux sucks.

## Pre-Requisites

- Android Developer Kit
- Java (openjdk?)

```
# if openjdk
# java.security.InvalidAlgorithmParameterException: the trustAnchors parameter must be non-empty 
$ sudo rm /etc/ssl/certs/java/cacerts
$ sudo update-ca-certificates -f

# Could not determine java version from ‘10.0.1’
# https://discuss.gradle.org/t/could-not-determine-java-version-from-9-0-1/24457/8
# https://askubuntu.com/questions/932083/how-do-i-upgrade-gradle
# copy gradlew from android-studio folder (somewhere in /opt or /usr/lib) to android directory
$ sudo add-apt-repository ppa:cwchien/gradle
$ sudo apt-get update
$ sudo apt upgrade gradle
```

```
$ npm install -g react-native-cli
$ react-init my_project
$ cd my_project
$ adb devices
$ react-native run-android
```


OR...

```
$ create-react-native-app my_app
$ cd my_app
$ touch .watchmanconfig
# https://github.com/guard/listen/wiki/Increasing-the-amount-of-inotify-watchers
$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

# In one terminal...
$ npm start android

# In another terminal
$ react-native run-android
```

