---
layout: project
title: "Persistent University Grade Tracker"
date: Early 2026
categories: ["software-development", "academic-tools"]
tags: ["C Programming", "File I/O", "Data Structures"]
duration: "3 Weeks"
image: "/assets/images/projects/c-grade-tracker/cover.jpg"
thumbnail: "/assets/images/projects/c-grade-tracker/cover.jpg"
---

<img src="{{ '/assets/images/projects/c-grade-tracker/cover.jpg' | relative_url }}" alt="Project Cover" style="width: 250px; height: auto; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** Terminal Application<br>
**Duration:** 3 Weeks<br>
**Team:** Solo<br>
**My Role:** Software Engineer

Engineered a lightweight, terminal-based University Grade Tracker written in C that utilizes persistent file storage to manage and calculate semester GPAs.

## Problem Statement
Needed a fast, low-overhead tool to track module grades and calculate cumulative GPAs over multiple semesters without relying on heavy external databases or GUI applications.

## Objectives
* Implement persistent data storage
* Calculate accurate GPA metrics
* Create a robust command-line interface

## Engineering Process
Struct Definition -> Memory Management -> File I/O Implementation -> CLI Interface

## Technical Details
Leveraged C structures to map out semester and module data. Implemented standard C file I/O operations to ensure data persisted accurately between application executions.

## Design Decisions
Chose a fundamental text/binary file storage approach over an external database to keep the application lightweight, fast, and completely self-contained.

## Tools & Software
* C
* GCC Compiler
* Terminal

## Engineering Skills Demonstrated
* Memory Management
* File Systems
* Terminal CLI Design

## Challenges
Handling raw memory pointers and ensuring file streams were properly managed and closed to prevent memory leaks and data corruption.

## Results
Deployed a highly responsive CLI tool that successfully reads, writes, and calculates academic standing with zero data loss between sessions.

## Key Learning
Deepened understanding of low-level memory management, pointers, and direct file manipulation in standard C.
