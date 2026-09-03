---
layout: page
title: "Day 3: UNIX and R Review"
parent: Home
nav_order: 4
has_toc: false
---

# Day 3: UNIX and R Review
{: .no_toc }

**Thursday, September 10**

---

## Schedule

| Time | Activity |
|------|----------|
| 9:00 – 10:30 | UNIX questions and review |
| 10:30 – 11:45 | [Presentation: Basic R]({{ site.baseurl }}/assets/files/B3.5p_Bekiranov_Day3_5.pdf) |
| 1:00 – 2:30 | R questions and review |
| 2:30 – 3:45 | [Presentation: Tidyverse in R]({{ site.baseurl }}/assets/files/B3.5p_Ratan_Day3_5.pdf) |
{: .schedule-table }

---

## Morning: UNIX Review

Today's morning session is open Q&A and review — bring your questions from Day 1 and the shell-extras assignment.

Common sticking points we'll cover:

- File permissions and `chmod`
- Environment variables and `$PATH`
- Writing reusable shell scripts with arguments (`$1`, `$2`, …)
- `ssh` key-based authentication for passwordless UVA HPC login
- Transferring files with `scp` and `rsync`

---

## Afternoon: R and Tidyverse

### Basic R Review

Dr. Bekiranov will review core R concepts with emphasis on what you will need for RNA-seq analysis:

- Data types, vectors, lists, data frames
- Subsetting with `[`, `[[`, `$`
- Functions and control flow
- Reading and writing files

### Tidyverse Deep Dive

Dr. Ratan will cover the Tidyverse toolkit in depth:

- The pipe operator `|>` and readable data pipelines
- `dplyr`: `filter()`, `select()`, `mutate()`, `group_by()`, `summarise()`
- `tidyr`: reshaping data with `pivot_longer()` and `pivot_wider()`
- `ggplot2`: building plots layer by layer

#### Key Tidyverse commands reference

```r
library(tidyverse)

# Filter rows
df |> filter(condition > 0)

# Select columns
df |> select(gene, sample, count)

# Add/transform columns
df |> mutate(log2count = log2(count + 1))

# Summarise by group
df |>
  group_by(condition) |>
  summarise(mean_count = mean(count))

# Reshape: wide → long
df |> pivot_longer(cols = starts_with("sample"),
                   names_to = "sample",
                   values_to = "count")

# Basic ggplot
ggplot(df, aes(x = condition, y = log2count, fill = condition)) +
  geom_boxplot() +
  theme_bw()
```

---

## Using AI in Computational Biology

AI assistants — ChatGPT, Claude, GitHub Copilot, and others — are increasingly used in bioinformatics. This is worth thinking about deliberately rather than stumbling into.

### What AI is genuinely good at

- Writing boilerplate code: shell loops, file parsing, ggplot templates
- Explaining what a function does or why an error occurred
- Translating between languages (e.g., "rewrite this Python in R")
- Suggesting approaches when you're stuck on where to start

You have already been doing the work that makes AI useful to you. When you paste a shell error or a broken `dplyr` pipeline into an AI assistant, you now have enough context to judge whether the suggested fix makes sense. That judgment is not replaceable.

### Where AI fails quietly

AI-generated code often *looks* right but isn't. Common failure modes:

- **Plausible but wrong syntax** — shell quoting, variable scoping, and pipe behavior have subtle rules AI frequently gets wrong
- **Hallucinated function arguments** — tidyverse functions have specific argument names; AI often confuses them across versions
- **Stale knowledge** — HPC module names, package APIs, and best practices change; AI training data does not

The UNIX and R work you have done this week is exactly the kind of thing AI gets subtly wrong. You now have the experience to catch those mistakes. Someone who has never touched the shell or R cannot.

### A practical stance

Use AI as a **coding collaborator, not an oracle**. Treat its output the way you'd treat code from a colleague who is smart but hasn't used your specific system: read it, understand it, test it. If you can't tell whether the code is correct, that is a signal to go back to the fundamentals — not to ask the AI again.

> **Try it:** Take one of the shell loops or `dplyr` pipelines you wrote this week and paste it into an AI with the question "what does this do?". Then ask it to write a similar one from scratch. Does it match what you'd write? Does it get the details right?

---

## Going further

To hit the ground running on Friday, have a look at the [Day 4: RNA-seq Analysis]({% link day4-rnaseq.md %}) overview and skim the Introduction & QC lesson. You don't need to understand everything — arriving with a sense of the workflow and the dataset will make Friday's hands-on time much more productive.
