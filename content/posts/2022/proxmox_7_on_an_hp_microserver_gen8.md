Title: Proxmox 7 on an HP MicroServer Gen8
Date: 2022-10-19
Tags: HP MicroServer Gen8, Proxmox
Summary_img: images/proxmox_why.png
Summary: How to install Proxmox VE 7.2 on an HP MicroServer Gen8.

<!-- SUMMARY -->
---

So you've decided you want to install Proxmox VE 7.2 on your MicroServer. Well, buckle up buckaroo, because do I have a walkthrough for you!

---

## Situation
 
I've got a MicroServer sitting unused. Previously it had ESXi 6.0 installed, and was where I was hosting my personal documentation,
OpenVPN, a backup Pi-hole, and some other random crap that I don't really remember. But, I've since migrated all that to another server, so the MicroServer was
just gather dust.

Having recently finished running network cables to the loungeroom, it seems now is a good time to recycle some old unused 2TB HDD's and turn it into a dedicated NAS + Plex experiment.
And for the hell of it, let's put Proxmox on this thing. I've never used it before, so why not? How hard can it be?

May as well use latest while we're at it, which was v7.2 at time of writing.

## Solution

Don't do it. Just don't. I burned an entire day dealing with random fucking issues. Something to do with them upgrading the kernel and it introducing some bugs. Just install v7.1.
Worked first time.

( ཀ ʖ̯ ཀ)
