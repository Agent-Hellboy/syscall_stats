# syscall_stats

-- Used to get the stat of system calls used by a binary in linux/unix  

## Prerequisites

Should be an unix machine to get the stat.
Keep in mind debian does not support strace.

## using 

run python3 util.py

```
prince@prince:~/syscall_stats$ python3 util.py 
enter the name of binary ls

output:
systemcall name execve 		number of calls 1
systemcall name brk 		number of calls 3
systemcall name access 		number of calls 8
systemcall name openat 		number of calls 9
systemcall name fstat 		number of calls 10
systemcall name mmap 		number of calls 17
systemcall name close 		number of calls 11
systemcall name read 		number of calls 7
systemcall name mprotect 		number of calls 12
systemcall name arch_prctl 		number of calls 1
systemcall name munmap 		number of calls 1
systemcall name set_tid_address 		number of calls 1
systemcall name set_robust_list 		number of calls 1
systemcall name rt_sigaction 		number of calls 2
systemcall name rt_sigprocmask 		number of calls 1
systemcall name prlimit64 		number of calls 1
systemcall name statfs 		number of calls 2
systemcall name ioctl 		number of calls 2
systemcall name getdents 		number of calls 2
systemcall name write 		number of calls 1
systemcall name exit_group 		number of calls 1




```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
