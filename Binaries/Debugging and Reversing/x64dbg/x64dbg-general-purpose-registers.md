# Using x64dbg

x64dbg is a debugger for x86 and x64 binaries which conform to the PE standard. This debugger has a vast array of functionality and has many advantages for practical implementations like Debugging, Reverse-Engineering, and other related subjects. The general documentation is available at [help.x64dbg.com](https://help.x64dbg.com/)

## Scripts for x64dbg
- [x64dbg Scripts](https://github.com/x64dbg/Scripts/tree/master)

## Scripting in x64dbg
When writing scripts within x64dbg it seems practically anything that can go in a command function may go within a script.

## [General Purpose Registers](https://help.x64dbg.com/en/latest/commands/general-purpose/index.html)
### `inc` and `dec`
- The `inc` register is for incrementing registers and values by one. 
- The `dec` register is for decrementing registers and values by one.
#### example
```as
mov $value, 0x1         // assign a value of 1h
inc $value              // increment by 1h
cmp $value, 0x2         // compare against 2h
je continue_label       // if equal, go to continue_label

// continue_label instantiation
continue_label:
    dec $value, 0x1     // decrement by 1h 
    cmp $value, 0x1     // compare against 1h
    je exit             // if equal, go to exit

// end of program
exit:
```
### `add` and `sub`
- `add` is for adding values
- `sub` is for subtracting values 
#### Example
```as
mov $value, 0x1         // assign a $value of 1h
add $value, 0xA         // add 10 to $value
cmp $value, 0xB         // compare against 11
je continue_label       // if equal, go to continue_label

// instantiation of continue_label
continue_label:
	sub $value, 0xA     // subtract 10 from $value
	cmp $value, 0x1     // compare $value to 1h	
	je exit             // if equal, go to exit

// end of program
exit:
```

### `mul` and `mulhi`
- `mul` multiplies two 64-bit values and stores the lower half
- `mulhi` multiplies two 64-bit values and stores the upper half
#### Example
```as
mov $value, 0x1111111111111111				// 8 byte number, (64 bits)
mul $value, 0x11							// 1 byte number
cmp $value, 0x2222222222222221				// register with lower-half and copied upper half
je if_true									// if cmp was true
jne if_false								// if cmp was false
jmp next_label								// otherwise go to next_label anyway
// if_true label instantiation
if_true:
	msg "Value is 0x2222222222222221"		// Display message
	jmp next_label							// go to next_label
// if_false label instantiation
if_false:
	msg "Value is not 0x2222222222222221"	// Display message
	jmp next_label							// go to next_label
// next_label instantiation
next_label:
	mov $value, 0x1111111111111111			// assign an 8 byte number (64 bits)
	mulhi $value, 0x11						// 1 byte number 
	cmp $value, 0x1							// if all we got was the upper region
	je if_true_two							// if equal go to if_true_two
	jne if_false_two						// if not equal go to if_false_two
	jmp exit								// go to exit
// if_true_two label
if_true_two:
	msg "Value is 0x1"						// Display message
	jmp exit								// go to exit
// if_false_two label
if_false_two:
	msg "Value is not 0x1"					// Display message
	jmp exit								// go to exit
// end of program
exit:
```

### `div`
- `div` is for dividing 64-bit numbers
#### Example
```as
mov $value, 0x64			// assign 100 to $value
div $value, 0x2				// divide by 2
cmp $value, 0x32			// check if value is 50
je is_50					// if 50, go to if_50
jne is_not_50				// else, go to is_not_50
jmp exit					// otherwise, exit
// is_50 label instantiation
is_50:
	msg "Value is 50"		// display message
	jmp exit				// go to exit
// is_not_50 label instantiation
is_not_50:
	msg "Value is not 50"   // display message
	jmp exit				// go to exit
// exit label instantiation
exit:
```
### `and`, `or`, and `xor`
- `and` performs a binary AND, putting the value in arg1
- `or` performs a binary OR, putting the value in arg1
- `xor` performs a binary XOR, putting the value in arg1
#### Example
```as
mov $op,  0x1010
mov $op2, 0x1111
mov $op3, 0x0000
mov $value, $op						
xor $value, $op
msg "{$op} xor {$op} = {$value}"
mov $value, $op
or  $value, $op
msg "{$op} or {$op} = {$value}"
mov $value, $op2
and $value, $op3
msg "{$op2} and {$op3} = {$value}"
```

### `neg`
- Negates a 64-bit number
#### Example
```as
mov $max, 0xFFFFFFFFFFFFFFFF
mov $value, $max
neg $value
cmp $value, 0x1
msg '{$value}'
je is_true
jne is_false
jmp exit

is_true:
	msg "Value negated"
	jmp next
	
is_false:
	msg "Value not negated"
	jmp next

next:
	mov $value, 0x1
	neg $value
	msg '{$value}'
	cmp $value, $max
	je is_true_two
	jne is_false_two
	jmp exit
	
is_true_two:
	msg "Value negated (2)"
	jmp exit

is_false_two:
	msg "Value not negated (2)"
	jmp exit

exit:
```

## `not`
- Similar to negate, `not` takes a value and applies a binary NOT
```as
mov $full, 0xFFFFFFFFFFFFFFFF
mov $value, $full
not $value
cmp $value, 0x0
je is_true
jne is_false
jmp exit

is_true:
	msg "NOT {$full} = 0x0!"
	jmp next
	
is_false:
	msg "Value is {$full}."
	jmp next

next:
	mov $value, 0x0
	not $value
	cmp $value, $full
	je is_true_two
	jne is_false_two
	jmp exit
	
is_true_two:
	msg "NOT 0x0 = {$full}!"
	jmp exit

is_false_two:
	msg "Value is 0x0."
	jmp exit

exit:
```

### bswap
- inverts byte order of the first operation
#### Example
```as
mov $one, 0x1234567890ABCDEF
msg "$one = {$one}"
bswap $one
msg "$one after bswap = {$one}"
mov $two, 0xAABBCCDDABABABAB
msg "$two = {$two}"
bswap $two
msg "$two after bswap = {$two}"
mov $three, 0x1111111100000000
msg "$three = {$three}"
bswap $three
msg "$three after bswap = {$three}"
```
### `rol` and `ror`
- Binary ROL (rotate left) a  value
- Binary ROR (rotate right) a value
```as
mov $alt, 0x1
mov $a, 0x1111
mov $value, $a
msg "{$a} before rol {$alt}"
rol $value, $alt
msg "{$a} after rol {$alt} = {$value}"
mov $b, $value
rol $value, $alt
msg "{$b} after rol {$alt} = {$value}"
mov $c, $value
rol $value, $alt
msg "{$c} after rol {$alt} = {$value}"
mov $d, $value
ror $value, $alt
msg "{$d} after ror {$alt} = {$value}"
mov $e, $value
ror $value, $alt
msg "{$e} after ror {$alt} = {$value}"
mov $f, $value
ror $value, $alt
msg "{$f} after ror {$alt} = {$value}"
```
## `shl`, `sal`, and `shr`
```as
mov $signed, 0xFFFFFFFFFFFFFF00
mov $unsigned, 0x0000000FFFFFFFFF
mov $x, $signed
mov $y, $unsigned
// shift signed left
shl $x, $y
// $x is now 0
msg "{$signed} after shl of {$unsigned} = {$x}"
mov $a, 0x22
mov $b, 0xFF
// shift unsigned left
sal $a, $b
// $a is now 0
msg "0x22 sal 0xFF = {$a}"
mov $e, 0x80
mov $f, 0x22
// shift right
shr $e, $f
// $e is now 0
msg "0x80 after shr 0x22 = {$e}"
```

## [`popcnt`](https://help.x64dbg.com/en/latest/commands/general-purpose/popcnt.html) / [`lzcnt`](https://help.x64dbg.com/en/latest/commands/general-purpose/lzcnt.html)
See documentation for popcnt

