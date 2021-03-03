# Decrypting the Apple Accessory Protocol

The AAP (Apple Accessory Protocol) is a L2CAP based protocol used by apple to allow communication between e.g. their headphones and their iOS or macOS line. The fun in parsing the protocol is that it includes the magic pairing key, in-ear detection and accurate battery information, configuring the headphones, ...

The decryption of their protocol would be the first step in creating a linux bluez protocol defintion for it, enabling linux users to use the Apple with all their advanced configurations.

## The protocol defintion
The protocol is defined in the [Kaitai Language](https://doc.kaitai.io/user_guide.html). This can either be edited in the browser, or using a combination of your favorite text editor and the ksv in the terminal. 

