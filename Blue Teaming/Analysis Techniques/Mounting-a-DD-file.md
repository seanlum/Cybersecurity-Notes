# Mounting a DD image file
https://superuser.com/questions/117136/how-can-i-mount-a-partition-from-dd-created-image-of-a-block-device-e-g-hdd-u

## Example
Replace loop0 with the loop device that was used by losetup. You can also specify the loop device if I'm not mistaken.
```
losetup --partscan --find --show disk.img

mount /dev/loop0 /mnt
```