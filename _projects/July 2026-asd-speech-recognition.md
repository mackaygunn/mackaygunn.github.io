---
layout: project
title: "ASD Speech Acoustic Analysis & Feature Engineering"
date: July 2026
categories: ["machine-learning", "data-science", "research"]
tags: ["Python", "Scikit-Learn", "Matplotlib", "Data Engineering"]
duration: "1 Semester"
image: "/assets/images/projects/asd-speech-recognition/cover.jpg"
thumbnail: "/assets/images/projects/asd-speech-recognition/cover.jpg"
---

<img src="{{ '/assets/images/projects/asd-speech-recognition/cover.jpg' | relative_url }}" alt="Project Cover" style="width: 250px; height: auto; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** Academic Research<br>
**Duration:** 1 Semester<br>
**Team:** Solo (Supervised by Dr. Nushara)<br>
**My Role:** Machine Learning Researcher / Data Engineer

Built a Python data pipeline using the speechocean762 dataset to isolate valid acoustic markers (prosody and fluency) for an ASD speech model while mitigating demographic and language-barrier biases.

## Problem Statement
Existing pronunciation datasets contained severe demographic biases and confounding language-barrier variables that prevented their direct use in clinical Autism Spectrum Disorder detection.

## Objectives
* Neutralize demographic biases via undersampling
* Extract and isolate clinically valid ASD proxies like prosody
* Prove class separation mathematically and visually

## Engineering Process
Data Extraction -> Undersampling -> Feature Engineering -> Statistical Variance Analysis -> Visualization

## Technical Details
Engineered a mathematically balanced 1,044-utterance training dataset from 2,500 raw Kaldi-formatted audio logs. Parsed nested JSON structures to extract sentence-level acoustic parameters.

## Design Decisions
Explicitly excluded 'Accuracy' and 'Completeness' scores as they were identified as confounding variables representing second-language proficiency rather than neurodivergence.

## Tools & Software
* Python
* NumPy
* Matplotlib
* Scikit-Learn

## Engineering Skills Demonstrated
* Data Pipeline Architecture
* Statistical Variance Analysis
* Bias Mitigation

## Challenges
Preventing data leakage between the balanced training set and the leftover testing set, and proving mathematically that the highest-scoring feature was actually a confounding variable.

## Results
Successfully isolated 1,456 unseen utterances as a pristine testing set and generated automated boxplots proving statistical separation of the typical and atypical classes.

## Key Learning
Learned the critical difference between mathematical performance and scientific validity, specifically how to identify and eliminate confounding variables in clinical datasets.

## Gallery

### System Integration & Prototyping

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 2rem; text-align: center;">
  <div>
    <img src="{{ '/assets/images/projects/asd-speech-recognition/clinical_feature_comparison.png' | relative_url }}" alt="Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>Statistical Feature Separation Bar Chart</em></p>
  </div>
</div>
