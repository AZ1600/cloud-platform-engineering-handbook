# Chapter 2 – Linux Fundamentals

> "Linux is not just an operating system. It is the foundation of modern cloud computing."

---

# Reading Time

⏱ 35–45 Minutes

# Difficulty

⭐☆☆☆☆ Beginner

---

# Learning Objectives

By the end of this chapter, you should be able to:

- Explain what Linux is.
- Understand why Linux dominates cloud computing.
- Describe the Linux architecture.
- Navigate the Linux file system.
- Manage files and directories.
- Understand Linux permissions.
- Manage users and groups.
- Monitor processes.
- Troubleshoot Linux systems.
- Connect Linux concepts to Docker, Kubernetes and AWS.
- Complete practical Linux administration tasks.
- Answer common Linux interview questions.

---

# 1. Introduction

Imagine trying to become a mechanic without understanding how an engine works.

You might learn how to drive a car, but the moment something goes wrong, you'll struggle to diagnose the problem.

Cloud Engineering works in the same way.

Many engineers learn AWS, Kubernetes, Terraform and Docker before learning Linux.

While they may know the commands, they often struggle when systems fail because they don't understand the operating system underneath.

Linux is the operating system that powers much of today's internet.

Every time you:

- Launch an EC2 instance
- Run a Docker container
- Deploy a Kubernetes Pod
- Start a FastAPI application

there is a very good chance Linux is managing everything behind the scenes.

Understanding Linux is one of the biggest steps towards becoming a confident Cloud or Platform Engineer.

---

# 💭 Engineering Story

When I built **PlatformPilot**, I always had multiple terminal windows open.

One terminal ran the FastAPI backend.

Another ran the React frontend.

Another executed Kubernetes commands.

At first I thought they were simply different commands.

Later I realised Linux was managing every process, every file, every network connection and every piece of memory.

Learning Linux completely changed how I debugged applications.

---

# 2. What Is Linux?

## Simple Explanation

Imagine a school.

Students attend lessons.

Teachers teach.

The principal makes sure everything runs smoothly.

Without the principal, everyone would do whatever they wanted.

An operating system works in a similar way.

Applications want to use:

- CPU
- Memory
- Storage
- Network

Linux acts as the manager.

It decides:

- Which program runs.
- How memory is used.
- Which files can be accessed.
- Which users have permission.
- How hardware is shared.

Without Linux, software cannot communicate effectively with the computer's hardware.

---

## Technical Definition

Linux is an open-source, Unix-like operating system built around the Linux kernel.

It manages:

- CPU scheduling
- Memory allocation
- Storage
- Networking
- Security
- Devices
- Processes
- File systems

Linux provides the environment where applications execute.

---

# 📖 Did You Know?

More than 90% of cloud workloads run on Linux-based operating systems.

Linux powers:

- AWS
- Azure
- Google Cloud
- Docker
- Kubernetes
- Android
- Most web servers
- Most supercomputers

---

# 3. A Brief History of Linux

Linux was created in 1991 by **Linus Torvalds**, a Finnish computer science student.

Originally, it was a personal project inspired by Unix.

Because Linux was open source, developers around the world began improving it.

Today it has become one of the most important operating systems ever created.

Millions of servers now rely on Linux every day.

---

# 4. Why Linux Matters

Cloud Engineers work with Linux almost every day.

Examples include:

- SSH into servers.
- Read application logs.
- Restart services.
- Configure networking.
- Deploy containers.
- Troubleshoot Kubernetes nodes.
- Monitor CPU and memory usage.
- Write automation scripts.

Understanding Linux makes all of these tasks easier.

---

# 5. Linux Distributions

Linux itself is only the kernel.

A Linux distribution combines the kernel with additional software to create a complete operating system.

Popular distributions include:

- Ubuntu
- Debian
- Fedora
- Red Hat Enterprise Linux
- Rocky Linux
- AlmaLinux
- Arch Linux
- Amazon Linux

As a Cloud Engineer, you will most commonly encounter:

- Ubuntu
- Amazon Linux
- Red Hat Enterprise Linux

---

# 6. Linux Architecture

```
Applications

↓

Shell

↓

Kernel

↓

Hardware
```

---

## Applications

Applications are programs users interact with.

Examples include:

- Chrome
- VS Code
- Docker
- Python
- FastAPI
- Kubernetes tools

---

## Shell

The shell is a command interpreter.

When you type:

```bash
ls
```

the shell sends the request to the Linux kernel.

Popular shells include:

- Bash
- Zsh
- Fish

---

## Kernel

The kernel is the heart of Linux.

It manages:

- CPU
- Memory
- Processes
- Hardware
- Storage
- Networking

Applications never communicate directly with hardware.

Everything passes through the kernel.

---

## Hardware

Hardware includes:

- CPU
- RAM
- SSD
- Network Card
- USB Devices

The kernel acts as the bridge between hardware and software.

---

# 7. The Linux File System

Unlike Windows, Linux begins from one location:

```
/
```

This is called the **Root Directory**.

Everything starts here.

```
/

├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

# Important Directories

## /home

Stores user files.

Example:

```
/home/olawale
```

---

## /etc

Contains configuration files.

Examples:

- SSH configuration
- Network configuration
- System settings

---

## /var

Stores logs and variable data.

Example:

```
/var/log
```

---

## /tmp

Temporary files.

Usually deleted automatically.

---

## /usr

Applications and shared libraries.

---

## /bin

Essential Linux commands.

Examples:

- ls
- cp
- mv
- cat

---

# 8. Navigating Linux

Current directory

```bash
pwd
```

List files

```bash
ls
```

Detailed list

```bash
ls -l
```

Hidden files

```bash
ls -la
```

Change directory

```bash
cd Documents
```

Go back

```bash
cd ..
```

Go home

```bash
cd ~
```

---

# 9. Working With Files

Create folder

```bash
mkdir projects
```

Create nested folders

```bash
mkdir -p platformpilot/backend
```

Create file

```bash
touch README.md
```

Copy

```bash
cp file.txt backup.txt
```

Move

```bash
mv old.txt new.txt
```

Delete

```bash
rm file.txt
```

Delete folder

```bash
rm -r project
```

⚠️ Linux has no recycle bin when using `rm`.

Be careful.

---

# 10. File Permissions

Example:

```
-rwxr-xr--
```

Meaning:

```
Owner

Group

Others
```

Permissions:

- r → Read
- w → Write
- x → Execute

Make a script executable

```bash
chmod +x deploy.sh
```

Change ownership

```bash
chown olawale deploy.sh
```

---

# 11. Users and Groups

Linux is a multi-user operating system.

Important users include:

- root
- regular users

Useful commands:

```bash
whoami
```

```bash
id
```

```bash
groups
```

---

# 12. Processes

Everything running on Linux is a process.

View processes

```bash
ps
```

Interactive monitor

```bash
top
```

or

```bash
htop
```

Kill process

```bash
kill PID
```

Force kill

```bash
kill -9 PID
```

---

# 13. Networking

Check IP

```bash
ip addr
```

Ping

```bash
ping google.com
```

Download data

```bash
curl https://example.com
```

SSH

```bash
ssh ubuntu@server-ip
```

Copy files

```bash
scp file.txt ubuntu@server:/home/ubuntu
```

---

# 14. Services

Linux uses services to run applications.

Examples:

- nginx
- docker
- ssh

Start

```bash
sudo systemctl start nginx
```

Stop

```bash
sudo systemctl stop nginx
```

Restart

```bash
sudo systemctl restart nginx
```

Status

```bash
systemctl status nginx
```

---

# 15. Logs

View logs

```bash
journalctl
```

Follow logs

```bash
journalctl -f
```

Application logs are often stored inside:

```
/var/log
```

---

# 16. Package Managers

Different Linux distributions use different package managers.

Ubuntu

```bash
sudo apt update
```

Amazon Linux

```bash
sudo yum update
```

or

```bash
sudo dnf update
```

---

# 17. Bash

Bash allows engineers to automate tasks.

Example

```bash
#!/bin/bash

echo "Hello Cloud Engineer!"
```

Automation is one of Bash's biggest strengths.

---

# 🌍 From Theory to Practice

Think about PlatformPilot.

When you started the backend using:

```bash
uvicorn app:app --reload
```

Linux:

- created a process
- allocated memory
- opened a network port
- monitored the application
- handled incoming requests

When React was started:

```bash
npm run dev
```

Linux created another process.

When Kubernetes was running,

Linux managed every Pod running on your machine.

---

# Best Practices

✅ Learn the terminal.

✅ Understand permissions.

✅ Read logs before restarting services.

✅ Avoid using root unnecessarily.

✅ Keep systems updated.

---

# Common Beginner Mistakes

❌ Memorising commands without understanding them.

❌ Using `sudo` for everything.

❌ Deleting files using `rm -rf` without checking.

❌ Ignoring logs during troubleshooting.

---

# Interview Questions

### What is Linux?

### What is the Linux Kernel?

### What is the difference between Bash and the Kernel?

### What does chmod do?

### Explain Linux file permissions.

### What is SSH?

### What is the purpose of `/etc`?

### What happens when you type a command into the terminal?

---

# Review Questions

1. Why is Linux important for Cloud Engineers?

2. What is the Kernel?

3. What does the Shell do?

4. Explain the Linux architecture.

5. What is stored inside `/var`?

6. What is stored inside `/etc`?

7. Why should engineers understand Linux permissions?

---

# Practical Labs

## Lab 1

Create this structure using Linux commands only.

```
projects/

platformpilot/

backend/

frontend/
```

---

## Lab 2

Find every Python file inside your home directory.

---

## Lab 3

Create a Bash script that prints your name.

---

## Lab 4

SSH into a Linux server.

---

## Lab 5

Read system logs using `journalctl`.

---

# Key Takeaways

After completing this chapter you should understand:

✅ Why Linux dominates cloud computing.

✅ Linux architecture.

✅ The Linux file system.

✅ Essential Linux commands.

✅ Permissions.

✅ Users.

✅ Processes.

✅ Networking.

✅ Services.

✅ Logs.

✅ Bash basics.

---

# Chapter Summary

Linux is the operating system that powers much of modern cloud computing.

Understanding Linux means understanding how applications interact with hardware, how processes are managed, how files are organised, and how cloud infrastructure operates beneath the surface.

Whether you are deploying a Kubernetes cluster, running Docker containers, managing AWS EC2 instances, or developing applications such as PlatformPilot, Linux provides the foundation on which these technologies are built.

Rather than memorising commands, focus on understanding why Linux works the way it does. This knowledge will make troubleshooting easier, improve your confidence as an engineer, and prepare you for more advanced topics.

---

# Next Chapter

In **Chapter 3 – Docker Fundamentals**, you will learn how containers changed software development forever.

You will understand:

- Containers
- Images
- Dockerfiles
- Volumes
- Networks
- Docker Compose
- Multi-stage builds
- Best practices
- PlatformPilot examples