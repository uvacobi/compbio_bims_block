---
layout: page
title: "Day 4: RNA-seq Analysis"
parent: Home
nav_order: 5
has_children: true
has_toc: false
---

# Day 4: RNA-seq Analysis
{: .no_toc }

**Friday, September 11**

---

## Schedule

| Time | Activity |
|------|----------|
| 9:00 – 10:00 | [Introduction & QC with FastQC]({{ site.baseurl }}{% link day4/introduction.md %}) *(2 points)* |
| 10:00 – 11:00 | [Aligning Reads with STAR]({{ site.baseurl }}{% link day4/aligning.md %}) |
| 11:00 – 11:45 | [Quantifying Reads with featureCounts]({{ site.baseurl }}{% link day4/counting.md %}) |
| 1:30 – 2:15 | [Differential Expression with DESeq2]({{ site.baseurl }}{% link day4/diffexp.md %}) *(2 points)* |
| 2:15 – 3:00 | [Over-representation Analysis of GO Terms]({{ site.baseurl }}{% link day4/ora.md %}) |
| 3:00 – 3:45 | [Gene Set Enrichment using GSEA/MSigDB]({{ site.baseurl }}{% link day4/gsea.md %}) |
{: .schedule-table }

---

## Learning Objectives

After completing today's lessons you will be able to:

- Assess the quality of RNA-seq reads using FastQC
- Align RNA-seq reads to a reference genome using STAR
- Generate a count matrix with featureCounts
- Perform QC via PCA and sample clustering
- Run differential expression analysis with DESeq2
- Create volcano plots and heatmaps
- Interpret results through over-representation analysis (ORA) and GSEA

---

## Software Modules on UVA HPC

All tools are pre-installed as modules. Load them in your terminal session before running each step:

```bash
module load fastqc/0.12.1
module load star/2.7.11b
export PATH=/standard/bims6000/bin:$PATH  # adds featureCounts to your PATH
module load gcc/11.4.0 openmpi/4.1.4 R/4.4.1
```

To see all available versions of a tool:
```bash
module spider fastqc
```

---

## Dataset

We use published data from [Vogel et al. (2016)](https://doi.org/10.1111/nph.14036), comparing the response of *Arabidopsis thaliana* seedlings to three bacteria:

| Sample | Condition |
|--------|-----------|
| Mock | Control (no bacteria) |
| *Pseudomonas syringae* DC3000 | Known foliar pathogen |
| *Methylobacterium extorquens* PA1 | Commensal bacteria |
| *Sphingomonas melonis* Fr1 | Commensal bacteria |

Data are located on UVA HPC at `/standard/bims6000/data/`. The files you will use are:

**`/standard/bims6000/data/morning/`** — used during QC, alignment, and counting

| File | Description |
|------|-------------|
| `Arabidopsis_sample1/2/3/4.fq.gz` | Raw mRNA-seq reads in FASTQ format |
| `AtChromosome1.fa` | Chromosome 1 of the *A. thaliana* genome in FASTA format |
| `ath_annotation.gff3` | Genome annotation for chromosome 1 in GFF3 format; used to generate gene counts |
| `adapters.fasta` | Illumina adapter sequences for read trimming with Trimmomatic |

**`/standard/bims6000/data/afternoon/`** — pre-computed results for DESeq2, ORA, and GSEA

| File | Description |
|------|-------------|
| `raw_counts.csv` | Raw gene count matrix |
| `samples_to_conditions.csv` | Sample-to-condition correspondence |
| `differential_genes.csv` | Pre-computed DESeq2 differential expression results |

---

## Credits

RNA-seq materials adapted from the [Harvard Chan Bioinformatics Core](https://hbctraining.github.io/In-depth-NGS-Data-Analysis-Course) and [ScienceParkStudyGroup RNA-seq lesson](https://github.com/ScienceParkStudyGroup/rnaseq-lesson).
