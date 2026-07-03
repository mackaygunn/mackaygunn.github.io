---
layout: project
title: "Distributed Cache System"
date: 2026-07-03
summary: "Designed and implemented a high-performance distributed cache system handling 10k requests per second."
thumbnail: "/assets/images/projects/distributed-cache/thumbnail.jpg"
tags: ["backend", "system-design", "go"]
---

## The Problem
Our main database was experiencing significant read contention during peak load, leading to latency spikes and degraded user experience. We needed a caching layer that was highly available, horizontally scalable, and supported consistent hashing.

## Design & Iteration
I designed a custom distributed cache using Go, leveraging consistent hashing to distribute keys evenly across a cluster of 5 nodes. We used a write-through strategy with an LRU eviction policy. 

- **Language:** Go
- **Architecture:** Peer-to-peer gossip protocol for node discovery
- **Data Structure:** Thread-safe sharded map for concurrent access

## Validation
After deployment, the cache achieved a 95% hit rate within the first week. Read latency on the main database dropped by 80%, and the system successfully scaled to handle 10k+ requests per second with sub-millisecond p99 latency.
