# Vaccine-induced time- and age-dependent mucosal immunity to gastrointestinal parasite infection <!-- omit in toc -->

[DOI to be added upon publication]

Wei Liu<sup>1,†</sup>, Tom N. McNeilly<sup>2,†,*</sup>, Mairi Mitchell<sup>2</sup>, Stew T.G. Burgess<sup>2</sup>, Alasdair J. Nisbet<sup>2</sup>, Jacqueline B. Matthews<sup>2,3</sup>, and Simon A. Babayan<sup>1,\*</sup>

1. Institute of Biodiversity, Animal Health and Comparative Medicine, University of Glasgow, Glasgow, G12 8QQ, Scotland, UK,
2. The Moredun Research Institute, Pentlands Science Park, EH26 0PZ, Scotland, UK,
3. Roslin Technologies Limited, Roslin Innovation Centre, University of Edinburgh, Easter Bush, EH25 9RG, Scotland, UK

<sup>†</sup>These authors contributed equally to this work

\*To whom correspondence should be addressed; E-mail: simon.babayan@glasgow.ac.uk, tom.mcneilly@moredun.ac.uk

## Table of contents <!-- omit in toc -->

- [Supplementary data](#supplementary-data)
  - [multiqc_report_biopsy.html](#multiqc_report_biopsyhtml)
  - [ipa_3V_6V.ods](#ipa_3v_6vods)
  - [gene_cluster_masigpro.ods](#gene_cluster_masigproods)
- [Code](#code)
- [Raw transcriptomes](#raw-transcriptomes)
  - [Sequencing parameters](#sequencing-parameters)
  - [File & sample list](#file--sample-list)

## Supplementary data

### [multiqc_report_biopsy.html](Supplementary%20Data/multiqc_report_biopsy.html)

The quality control [MultiQC](https://multiqc.info) report of biopsy RNAseq samples based on the FASTQC data.

### [ipa_3V_6V.ods](Supplementary%20Data/ipa_3V_6V.ods)

Ingenuity Pathway analysis (IPA) results for all the WGCNA clusters shown in Fig 2.

### [gene_cluster_masigpro.ods](Supplementary%20Data/gene_cluster_masigpro.ods)

Differentially expressed gene list between the ageing groups. The expression levels are shown in Fig S5 C heatmap.

## Code

## Raw transcriptomes

Raw transcriptomes can be downloaded from Dryad [link to be added upon publication].

### Sequencing parameters

- RNAseq using nextSeq 500
- Organism and tissue type: *Ovis aries* abomasum
- Extraction method used: Qiagen RNeasy mini kit
- Suspension buffer used: RNAse free water
- read depth: 20M reads, paired-ends (named R1 and R2 in sequence files)

### File & sample list

Each filename follows the scheme:

`[sheepID][group][sampling week]_[sample run].fastq.gz`

| Sample ID | Age, Vaccine, Timepoint |
|:----------|:------------------------|
| 6565g1w1  | 3mo Vaccinated Week1    |
| 6615g1w1  | 3mo Vaccinated Week1    |
| 6622g1w1  | 3mo Vaccinated Week1    |
| 6642g1w1  | 3mo Vaccinated Week1    |
| 6917g1w1  | 3mo Vaccinated Week1    |
| 6925g1w1  | 3mo Vaccinated Week1    |
| 6937g1w1  | 3mo Vaccinated Week1    |
| 6588g2w1  | 3mo Control Week1       |
| 6625g2w1  | 3mo Control Week1       |
| 6626g2w1  | 3mo Control Week1       |
| 6634g2w1  | 3mo Control Week1       |
| 6915g2w1  | 3mo Control Week1       |
| 6931g2w1  | 3mo Control Week1       |
| 6935g2w1  | 3mo Control Week1       |
| 6940g2w1  | 3mo Control Week1       |
| 6565g1w2  | 3mo Vaccinated Week2    |
| 6615g1w2  | 3mo Vaccinated Week2    |
| 6622g1w2  | 3mo Vaccinated Week2    |
| 6642g1w2  | 3mo Vaccinated Week2    |
| 6917g1w2  | 3mo Vaccinated Week2    |
| 6925g1w2  | 3mo Vaccinated Week2    |
| 6937g1w2  | 3mo Vaccinated Week2    |
| 6588g2w2  | 3mo Control Week2       |
| 6625g2w2  | 3mo Control Week2       |
| 6626g2w2  | 3mo Control Week2       |
| 6634g2w2  | 3mo Control Week2       |
| 6915g2w2  | 3mo Control Week2       |
| 6931g2w2  | 3mo Control Week2       |
| 6935g2w2  | 3mo Control Week2       |
| 6940g2w2  | 3mo Control Week2       |
| 6565g1w3  | 3mo Vaccinated Week3    |
| 6615g1w3  | 3mo Vaccinated Week3    |
| 6622g1w3  | 3mo Vaccinated Week3    |
| 6642g1w3  | 3mo Vaccinated Week3    |
| 6917g1w3  | 3mo Vaccinated Week3    |
| 6925g1w3  | 3mo Vaccinated Week3    |
| 6937g1w3  | 3mo Vaccinated Week3    |
| 6588g2w3  | 3mo Control Week3       |
| 6625g2w3  | 3mo Control Week3       |
| 6626g2w3  | 3mo Control Week3       |
| 6634g2w3  | 3mo Control Week3       |
| 6915g2w3  | 3mo Control Week3       |
| 6931g2w3  | 3mo Control Week3       |
| 6935g2w3  | 3mo Control Week3       |
| 6940g2w3  | 3mo Control Week3       |
| 6565g1w4  | 3mo Vaccinated Week4    |
| 6615g1w4  | 3mo Vaccinated Week4    |
| 6622g1w4  | 3mo Vaccinated Week4    |
| 6642g1w4  | 3mo Vaccinated Week4    |
| 6917g1w4  | 3mo Vaccinated Week4    |
| 6925g1w4  | 3mo Vaccinated Week4    |
| 6937g1w4  | 3mo Vaccinated Week4    |
| 6588g2w4  | 3mo Control Week4       |
| 6625g2w4  | 3mo Control Week4       |
| 6626g2w4  | 3mo Control Week4       |
| 6634g2w4  | 3mo Control Week4       |
| 6915g2w4  | 3mo Control Week4       |
| 6931g2w4  | 3mo Control Week4       |
| 6935g2w4  | 3mo Control Week4       |
| 6940g2w4  | 3mo Control Week4       |
| 6565g1w5  | 3mo Vaccinated Week5    |
| 6615g1w5  | 3mo Vaccinated Week5    |
| 6622g1w5  | 3mo Vaccinated Week5    |
| 6642g1w5  | 3mo Vaccinated Week5    |
| 6917g1w5  | 3mo Vaccinated Week5    |
| 6925g1w5  | 3mo Vaccinated Week5    |
| 6937g1w5  | 3mo Vaccinated Week5    |
| 6588g2w5  | 3mo Control Week5       |
| 6625g2w5  | 3mo Control Week5       |
| 6626g2w5  | 3mo Control Week5       |
| 6634g2w5  | 3mo Control Week5       |
| 6915g2w5  | 3mo Control Week5       |
| 6931g2w5  | 3mo Control Week5       |
| 6935g2w5  | 3mo Control Week5       |
| 6940g2w5  | 3mo Control Week5       |
| 6565g1w7  | 3mo Vaccinated Week7    |
| 6615g1w7  | 3mo Vaccinated Week7    |
| 6622g1w7  | 3mo Vaccinated Week7    |
| 6642g1w7  | 3mo Vaccinated Week7    |
| 6917g1w7  | 3mo Vaccinated Week7    |
| 6925g1w7  | 3mo Vaccinated Week7    |
| 6937g1w7  | 3mo Vaccinated Week7    |
| 6588g2w7  | 3mo Control Week7       |
| 6625g2w7  | 3mo Control Week7       |
| 6626g2w7  | 3mo Control Week7       |
| 6634g2w7  | 3mo Control Week7       |
| 6915g2w7  | 3mo Control Week7       |
| 6931g2w7  | 3mo Control Week7       |
| 6935g2w7  | 3mo Control Week7       |
| 6940g2w7  | 3mo Control Week7       |
| 6576g3w1  | 6mo Vaccinated Week1    |
| 6647g3w1  | 6mo Vaccinated Week1    |
| 6652g3w1  | 6mo Vaccinated Week1    |
| 6905g3w1  | 6mo Vaccinated Week1    |
| 6910g3w1  | 6mo Vaccinated Week1    |
| 6911g3w1  | 6mo Vaccinated Week1    |
| 6928g3w1  | 6mo Vaccinated Week1    |
| 6595g4w1  | 6mo Control Week1       |
| 6635g4w1  | 6mo Control Week1       |
| 6639g4w1  | 6mo Control Week1       |
| 6653g4w1  | 6mo Control Week1       |
| 6902g4w1  | 6mo Control Week1       |
| 6923g4w1  | 6mo Control Week1       |
| 6934g4w1  | 6mo Control Week1       |
| 6939g4w1  | 6mo Control Week1       |
| 6576g3w2  | 6mo Vaccinated Week2    |
| 6647g3w2  | 6mo Vaccinated Week2    |
| 6652g3w2  | 6mo Vaccinated Week2    |
| 6905g3w2  | 6mo Vaccinated Week2    |
| 6910g3w2  | 6mo Vaccinated Week2    |
| 6911g3w2  | 6mo Vaccinated Week2    |
| 6928g3w2  | 6mo Vaccinated Week2    |
| 6595g4w2  | 6mo Control Week2       |
| 6635g4w2  | 6mo Control Week2       |
| 6639g4w2  | 6mo Control Week2       |
| 6653g4w2  | 6mo Control Week2       |
| 6902g4w2  | 6mo Control Week2       |
| 6923g4w2  | 6mo Control Week2       |
| 6934g4w2  | 6mo Control Week2       |
| 6939g4w2  | 6mo Control Week2       |
| 6576g3w3  | 6mo Vaccinated Week3    |
| 6647g3w3  | 6mo Vaccinated Week3    |
| 6652g3w3  | 6mo Vaccinated Week3    |
| 6905g3w3  | 6mo Vaccinated Week3    |
| 6910g3w3  | 6mo Vaccinated Week3    |
| 6911g3w3  | 6mo Vaccinated Week3    |
| 6928g3w3  | 6mo Vaccinated Week3    |
| 6595g4w3  | 6mo Control Week3       |
| 6635g4w3  | 6mo Control Week3       |
| 6639g4w3  | 6mo Control Week3       |
| 6653g4w3  | 6mo Control Week3       |
| 6902g4w3  | 6mo Control Week3       |
| 6923g4w3  | 6mo Control Week3       |
| 6934g4w3  | 6mo Control Week3       |
| 6939g4w3  | 6mo Control Week3       |
| 6576g3w4  | 6mo Vaccinated Week4    |
| 6647g3w4  | 6mo Vaccinated Week4    |
| 6652g3w4  | 6mo Vaccinated Week4    |
| 6905g3w4  | 6mo Vaccinated Week4    |
| 6910g3w4  | 6mo Vaccinated Week4    |
| 6911g3w4  | 6mo Vaccinated Week4    |
| 6928g3w4  | 6mo Vaccinated Week4    |
| 6595g4w4  | 6mo Control Week4       |
| 6635g4w4  | 6mo Control Week4       |
| 6639g4w4  | 6mo Control Week4       |
| 6653g4w4  | 6mo Control Week4       |
| 6902g4w4  | 6mo Control Week4       |
| 6923g4w4  | 6mo Control Week4       |
| 6934g4w4  | 6mo Control Week4       |
| 6939g4w4  | 6mo Control Week4       |
| 6576g3w5  | 6mo Vaccinated Week5    |
| 6647g3w5  | 6mo Vaccinated Week5    |
| 6652g3w5  | 6mo Vaccinated Week5    |
| 6905g3w5  | 6mo Vaccinated Week5    |
| 6910g3w5  | 6mo Vaccinated Week5    |
| 6911g3w5  | 6mo Vaccinated Week5    |
| 6928g3w5  | 6mo Vaccinated Week5    |
| 6595g4w5  | 6mo Control Week5       |
| 6635g4w5  | 6mo Control Week5       |
| 6639g4w5  | 6mo Control Week5       |
| 6653g4w5  | 6mo Control Week5       |
| 6902g4w5  | 6mo Control Week5       |
| 6923g4w5  | 6mo Control Week5       |
| 6934g4w5  | 6mo Control Week5       |
| 6939g4w5  | 6mo Control Week5       |
| 6576g3w7  | 6mo Vaccinated Week7    |
| 6647g3w7  | 6mo Vaccinated Week7    |
| 6652g3w7  | 6mo Vaccinated Week7    |
| 6905g3w7  | 6mo Vaccinated Week7    |
| 6910g3w7  | 6mo Vaccinated Week7    |
| 6911g3w7  | 6mo Vaccinated Week7    |
| 6928g3w7  | 6mo Vaccinated Week7    |
| 6595g4w7  | 6mo Control Week7       |
| 6635g4w7  | 6mo Control Week7       |
| 6639g4w7  | 6mo Control Week7       |
| 6653g4w7  | 6mo Control Week7       |
| 6902g4w7  | 6mo Control Week7       |
| 6923g4w7  | 6mo Control Week7       |
| 6934g4w7  | 6mo Control Week7       |
| 6939g4w7  | 6mo Control Week7       |
