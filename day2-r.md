---
layout: page
title: "Day 2: Programming with R"
parent: Home
nav_order: 3
has_children: true
has_toc: false
---

# Day 2: Programming with R
{: .no_toc }

**Wednesday, September 9**

---

## Schedule

| Time | Activity |
|------|----------|
| 9:00 – 9:15 | Accessing R on UVA HPC |
| 9:15 – 10:00 | [Presentation: Introduction to R]({{ site.baseurl }}/assets/files/B3.5p_Day2_R.pdf) |
| 10:00 – 11:45 | R Activity: Lessons 1–5 *(2 points)* |
| 1:00 – 4:00 | R Activity: Lessons 6–8 |
{: .schedule-table }

---

## Learning Objectives

By the end of today you will be able to:

- Start an R session on UVA HPC via the terminal
- Understand R's basic data types and data structures
- Load, inspect, and subset data frames
- Work with factors (categorical variables)
- Install and use Bioconductor packages
- Wrangle data with `dplyr` (filter, select, mutate, summarise, group_by)
- Create publication-quality plots with `ggplot2`

---

## Accessing R on UVA HPC

R is available as a module on UVA HPC. Connect to the login node as you did in Day 1. R is launched with `module load gcc/11.4.0 openmpi/4.1.4 R/4.4.1` followed by `R`. Before starting the lessons, complete the full setup in the **Data Files on UVA HPC** section below.

---

## Data Files on UVA HPC

The lesson datasets are stored on the HPC at:

```
/standard/bims6000/genomics-r-intro/
```

Run all of these steps in order to set up your working directory and start R:

```bash
mkdir ~/day2
cp /standard/bims6000/genomics-r-intro/combined_tidy_vcf.csv ~/day2/
cd ~/day2
module load gcc/11.4.0 openmpi/4.1.4 R/4.4.1
export R_LIBS=/standard/bims6000/R:$R_LIBS
R
```

You will see the R startup message and a `>` prompt. Then set your working directory:

```r
setwd("~/day2")
```

To exit R at any time, type `q()` and press <KBD>Enter</KBD>. When asked whether to save the workspace, type `n`.

---

## Lessons

| # | Lesson | Estimated Time |
|---|--------|---------------|
| 1 | [Introduction to R]({% link day2/00-introduction.md %}) | 20 min |
| 2 | [R Basics]({% link day2/01-r-basics.md %}) | 40 min |
| 3 | [Working with Data]({% link day2/02-data-prelude.md %}) | 30 min |
| 4 | [Factors and Data Frames]({% link day2/03-basics-factors-dataframes.md %}) | 40 min |
| 5 | [Tidyverse for Data Wrangling]({% link day2/05-dplyr.md %}) | 40 min |
| 6 | [Visualization with ggplot2]({% link day2/06-data-visualization.md %}) | 40 min |
| 7 | [Getting Help with R]({% link day2/07-r-help.md %}) | 20 min |
{: .schedule-table }

---

## Going further

If you want more practice with R before Thursday, Lessons 1–3 of the [R for Reproducible Scientific Analysis](https://swcarpentry.github.io/r-novice-gapminder/) Carpentries lesson cover similar ground to today but with a different dataset — a useful way to reinforce what you've learned.

> **A note on external resources:** this lesson was not written specifically for UVA and uses RStudio rather than the terminal-based workflow we follow. The R concepts are the same, but you may encounter setup steps or interface references that don't apply here. Focus on the code and concepts rather than following the setup instructions.
