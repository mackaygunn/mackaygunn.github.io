---
layout: project
title: "ASD Speech Recognition Acoustic Analysis & Feature Engineering"
date: July 2026
categories: ["machine-learning", "data-engineering", "healthcare-research"]
tags: ["Python", "Scikit-Learn", "Data Pipeline", "Feature Engineering", "Matplotlib"]
duration: "3 Months"
image: "/assets/images/projects/asd-speech-acoustic-analysis/cover.png"
thumbnail: "/assets/images/projects/asd-speech-acoustic-analysis/cover.png"
---

<img src="{{ '/assets/images/projects/asd-speech-acoustic-analysis/cover.png' | relative_url }}" alt="Project Cover" style="width: 250px; height: auto; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** Machine Learning Research<br>
**Duration:** 3 Months<br>
**Team:** Independent Researcher (Supervised by Dr. Nushara)<br>
**My Role:** Machine Learning Researcher / Data Engineer

Developed a robust data pipeline and performed advanced acoustic feature engineering to identify clinically valid markers for an Autism Spectrum Disorder (ASD) speech recognition model. The project statistically isolated neurodivergent speech patterns from language-barrier confounding variables using a modified pronunciation dataset.

## Problem Statement
The objective was to identify the most accurate acoustic markers for training an ASD speech recognition model. The primary challenge was that the available dataset (speechocean762) was originally designed for language-pronunciation grading, meaning standard metrics like 'accuracy' acted as confounding variables that measured a speaker's English fluency rather than neurodivergent speech traits.

## Objectives
* Engineer a demographically balanced, bias-free dataset from raw Kaldi-formatted audio logs.
* Design a secure Python data pipeline to prevent data leakage between training and testing sets.
* Isolate clinically valid ASD acoustic proxies by eliminating language-barrier confounding variables.
* Visually prove class separation using statistical graphing techniques.

## Engineering Process
Data Extraction & Parsing -> 4-Way Random Undersampling -> Pipeline Development -> Feature Importance Analysis -> Statistical Visualization

## Technical Details
The project involved parsing nested JSON scoring metrics from 2,500 raw utterances. A 4-way random undersampling algorithm with a locked pseudo-random seed was implemented to neutralize severe gender and class demographic biases. This resulted in a mathematically perfect 1,044-utterance training set and a rigidly isolated 1,456-utterance testing set. Feature importance was evaluated using Scikit-Learn Random Forest classifications and strict statistical variance analysis.

## Design Decisions
A critical scientific decision was made to actively exclude 'Accuracy' and 'Completeness' scores from the final model feature selection. Although these features presented the largest mathematical variance, clinical domain knowledge proved they were confounding variables measuring non-native accents rather than true ASD traits. Consequently, Prosody and Fluency were selected as the primary, scientifically valid training features.

## Tools & Software
* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* JSON Data Parsing

## Engineering Skills Demonstrated
* Data Pipeline Architecture
* Bias Mitigation (Undersampling)
* Statistical Variance Analysis
* Target Leakage Prevention
* Data Visualization

## Challenges
The main challenge was identifying and proving the existence of confounding variables within the scoring dataset. Initial mathematical evaluations suggested 'Accuracy' was the best feature, which required implementing strict clinical constraints to force the algorithm to evaluate only valid ASD proxies rather than language proficiency.

## Results
Successfully engineered a mathematically defensible, bias-free dataset and statistically proved that Prosody and Fluency are the strongest non-confounding predictors for ASD classification. Automated Matplotlib scripts were generated to visually validate this class separation for academic presentation.

## Key Learning
I learned how to critically evaluate machine learning feature importance not just through pure mathematical output, but through the lens of clinical domain knowledge, successfully identifying how confounding variables can ruin a model's real-world validity.

<div style="text-align: center; margin: 3rem 0;">
  <a href="https://github.com/mackaygunn/Python-Projects/tree/4fae5c71438d80b2d04a29012273faf26cb23db3/ASD%20speech%20analysis" target="_blank" class="btn btn-secondary" style="display: inline-flex; align-items: center; gap: 10px; background: #24292e; color: #fff; border: none; padding: 0.8rem 1.5rem;">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
    View Source Code
  </a>
</div>

## Gallery

### System Integration & Prototyping

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 2rem; text-align: center;">
  <div>
    <img src="{{ '/assets/images/projects/asd-speech-acoustic-analysis/clinical_feature_comparison.png' | relative_url }}" alt="Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>Grouped bar chart with error bars demonstrating clinically valid feature separation between Typical and Atypical utterances.</em></p>
  </div>
  <div>
    <img src="{{ '/assets/images/projects/asd-speech-acoustic-analysis/feature_comparison_boxplot.png' | relative_url }}" alt="Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>Boxplot visual proving the statistical overlap and variance of the isolated acoustic features.</em></p>
  </div>
</div>
