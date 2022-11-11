Title: Updating the firmware and BIOS on an HP MicroServer Gen8
Date: 2022-10-24
Tags: HP MicroServer Gen8
Summary_img: /images/iLO_trash.jpg
Summary: A simple markdown page to test formatting and template from.

[TOC]

<!-- SUMMARY -->
---

iLO is rad and all, but man, the information on how to update it is garbage. Here's another bag on the proverbial trash-heap. Maybe if you're lucky, you'll stumble upon it.

---

## iLO
So what is [iLO](https://en.wikipedia.org/wiki/HP_Integrated_Lights-Out)?
> _**Integrated Lights-Out**, or **iLO**, is a proprietary embedded server management technology by Hewlett-Packard Enterprise which provides out-of-band management facilities._


In english:
> You can connect to this device over the network and manage it remotely.

This means you can mount disks, faff around with network settings, or even brick it if you are really keen on having _fun_. How this works is usually by having a mini computer within your computer.

![Yo Dawg]({static}/images/yo_dawg.jpg)

Unfortunately, you also need to occasionally update it. Previously, I was running an old version - which in itself isn't that bad, but the virtual [KVM](https://en.wikipedia.org/wiki/KVM_switch) could only be used with a no-longer supported Java applet, or a .NET application.
Given that I spend most of my homelab time not in Windows, this was a pain. If we update to a newever version, we'll get access to a sweet HTML5 KVM, which I can run in a browser.

Absolute no-brainer.


## Preparation

## Firmware
Before we can rub that new feature over sweaty, tender bodies, we'll need to upgrade the Firmware.

  1. download file
  2. unpack file
  3. upload file

TODO - add details on how to confirm it has been updated


## BIOS
Since we've gone through the hassle of updating the iLO firmware, we may as well update the BIOS while we're at it.

  1. download file
  2. unpack file
  3. upload file

TODO - add details on how to confirm it has been updated

https://sbs20.com/posts/2021/hpe-msgen8-firmware/

( ˘ ͜ʖ ˘)