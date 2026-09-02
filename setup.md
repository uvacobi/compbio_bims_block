---
layout: page
title: "Setup: Accessing UVA HPC"
parent: Home
nav_order: 0
---

# Setup: Accessing UVA HPC
{: .no_toc }

Complete this setup **before Day 1** (Tuesday, September 8).

<details open markdown="1">
<summary>Table of Contents</summary>
- TOC
{:toc}
</details>

---

## 1. Watch the Connecting to HPC Video

Visit the UVA RC page: [Connecting and Logging On To HPC](https://learning.rc.virginia.edu/notes/hpc-intro/connecting_to_the_system/connecting_logging_on/)

Watch the short video. You will see three connection methods — we recommend **Open OnDemand** for this course.

---

## 2. Recommended: Connect via Open OnDemand

Open OnDemand gives you point-and-click access to UVA HPC through your web browser — no additional software required.

1. Go to [ood.hpc.virginia.edu](https://ood.hpc.virginia.edu)
2. Log in with your **UVA computing ID** and **Netbadge password**
3. Once logged in, click **`>_ Open in Terminal`** in the upper left of the screen
4. A UNIX terminal opens in your browser — you are now on UVA HPC

<div class="carpentries-callout" markdown="1">
**UVA Computing ID**

Your UVA computing ID is the prefix of your UVA email address. For example, if your email is `mst3k@virginia.edu`, your computing ID is `mst3k`.
</div>

---

## 3. Alternative: SSH Access

If you prefer a terminal-based connection or Open OnDemand is unavailable, you can connect via SSH.

### Windows

Install [MobaXterm](https://mobaxterm.mobatek.net/) (free Home Edition). Use it to SSH to:

```
login.hpc.virginia.edu
```

with your UVA computing ID.

### macOS / Linux

Open **Terminal** (macOS: `Utilities → Terminal`) and type:

```bash
ssh <your_computing_id>@login.hpc.virginia.edu
```

For example:
```bash
ssh mst3k@login.hpc.virginia.edu
```

Enter your UVA Netbadge/eServices password when prompted.

---

## 4. Alternative: FastX

A third option, FastX, is documented on the [Connecting to HPC](https://learning.rc.virginia.edu/notes/hpc-intro/connecting_to_the_system/connecting_logging_on/) page. This provides a graphical desktop on UVA HPC.

---

## 5. Verify Your Access

Once connected (by any method), you should see a shell prompt like:

```
[mst3k@udc-ba37-36c1 ~]$
```

Type `pwd` and press Enter — you should see your home directory path (e.g. `/home/mst3k`). If you see this, you are ready for Day 1.
