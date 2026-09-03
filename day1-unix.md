---
layout: page
title: "Day 1: The UNIX Shell"
parent: Home
nav_order: 2
has_children: true
has_toc: false
---

# Day 1: The UNIX Shell
{: .no_toc }

**Tuesday, September 8**

---

## Schedule

| Time | Activity |
|------|----------|
| 9:00 – 10:00 | Enable UVA HPC access ([Setup]({% link setup.md %})) |
| 10:00 – 10:15 | Log onto UVA HPC — first look |
| 10:15 – 11:00 | Presentation: Introduction to UNIX |
| 11:00 – 11:45 | Shell Activity: Lessons 1–3 *(2 points)* |
| 1:00 – 4:00 | Shell Activity: Lessons 4–7 |
{: .schedule-table }

---

## Learning Objectives

By the end of today you will be able to:

- Explain what the UNIX shell is and when to use it
- Navigate the filesystem using `pwd`, `ls`, `cd`
- Create, copy, move, and delete files and directories
- Combine commands with pipes (`|`) and redirect output (`>`, `>>`)
- Write simple shell scripts and loops to automate repetitive tasks
- Use `grep` and `find` to search files

---

## On UVA HPC

All shell work today is done on UVA HPC. Connect via [Open OnDemand](https://ood.hpc.virginia.edu) → **`>_ Open in Terminal`**.

When the terminal opens you will see a prompt like:

```
[mst3k@udc-ba37-36c1 ~]$
```

where `mst3k` is your UVA computing ID and `udc-ba37-36c1` is the login node you landed on. The `~` means you are in your home directory (`/home/<computing_id>`).

### Copy the lesson data

Before starting the lessons, copy the data files to your home directory:

```bash
cp -r /standard/bims6000/shell-lesson-data ~/
```

Confirm the folder `shell-lesson-data` is there:

```bash
ls
```

```output
ondemand  privatemodules  public_html  shell-lesson-data
```

---

## Lessons

Work through the lessons in order. Each builds on the previous one.

| # | Lesson | Estimated Time |
|---|--------|---------------|
| 1 | [Introducing the Shell]({% link day1/01-intro.md %}) | 5 min |
| 2 | [Navigating Files and Directories]({% link day1/02-filedir.md %}) | 40 min |
| 3 | [Working With Files and Directories]({% link day1/03-create.md %}) | 35 min |
| 4 | [Pipes and Filters]({% link day1/04-pipefilter.md %}) | 35 min |
| 5 | [Loops]({% link day1/05-loop.md %}) | 50 min |
| 6 | [Shell Scripts]({% link day1/06-script.md %}) | 35 min |
| 7 | [Finding Things]({% link day1/07-find.md %}) | 25 min |
{: .schedule-table }

---

## Going further

If you want to challenge yourself before Wednesday, the [Extra UNIX Shell Material](https://carpentries-incubator.github.io/shell-extras/) from The Carpentries Incubator covers working remotely, transferring files, and aliases — all directly relevant to using UVA HPC.

> **A note on external resources:** this lesson was not written specifically for UVA. Some commands, paths, and setup steps will differ from what you've seen today. Treat it as a starting point rather than a recipe — read critically and adapt where needed.
