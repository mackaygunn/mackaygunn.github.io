---
layout: project
title: "Thermo-Electrical Food Compartment"
date: 2025-12-01
categories: [design-simulation, physical-projects]
tags: [Thermal-Engineering, SketchUp, Arduino, Systems-Design]
duration: "June - October 2025"
image: "/assets/images/projects/lunchbox/cover.jpg"
thumbnail: "/assets/images/projects/lunchbox/cover.jpg"
---

<img src="{{ '/assets/images/projects/lunchbox/cover.jpg' | relative_url }}" alt="Project Cover" style="width: 100%; max-width: 350px; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** Product Design • Embedded Systems • Thermal Engineering 
**Duration:** June 2025 – October 2025 
**Team:** 8 Members 
**My Role:** Mechanical Design & Electronic Systems Architecture

Designed and developed a portable self-heating lunch box that actively heats food while simultaneously cooling a secondary compartment using a Peltier thermoelectric module. My specific contribution focused on the electronic system architecture, embedded control logic using Arduino, and the mechanical integration of the thermal components.

## Problem Statement
Many students and workers carry home-cooked meals but lack access to heating facilities. Existing insulated lunch boxes only retain heat, while commercial electric options are bulky, expensive, and inefficient. The objective was to develop an affordable, portable (<1.5 kg) solution capable of actively heating food while maintaining a separate cooled section.

## Project Objectives
* Maintain food temperatures between 40–70°C.
* Actively heat food within a 20–30 minute window.
* Operate securely using rechargeable Lithium-ion battery systems.
* Ensure food safety via modular, washable, and food-grade materials.
* Optimize energy efficiency and minimize heat loss.

## Engineering Process
Research → User Requirement Analysis → Concept Generation & Evaluation Matrix → System Architecture → Thermal & Power Calculations → CAD Design → Prototype Development → Testing & Iteration.

## Technical Details & Architecture

### Electronic & Embedded Systems (My Core Contribution)
I led the electronic architecture and control logic for the thermal regulation.
* **Control Architecture:** Designed the embedded logic utilizing an Arduino-based controller to manage the heating and cooling cycles.
* **Sensor Integration:** Integrated digital temperature sensors and relay controls to create a closed-loop feedback system, ensuring the system shuts off automatically when target temperatures are reached.
* **Power Management:** Calculated battery sizing requirements and integrated safety interlocks for the Lithium-ion power source.

### Mechanical & Thermal Engineering
* **Thermal Management:** Utilized a Peltier TEC1-12706 module combined with an Aluminum heat sink to achieve dual heating and cooling capabilities.
* **Material Selection:** Specified Polyurethane insulation and Silicone rubber seals to maximize thermal retention, alongside Stainless Steel and Polypropylene for structural integrity and food safety.

## Design Decisions
A weighted engineering decision matrix was utilized to select the core heating technology. 
* **Peltier Module vs. Heating Coils:** The Peltier module was selected because it is significantly safer, lighter, consumes lower power, and allows for simultaneous heating and cooling within a compact footprint.

## Testing & Results
The final prototype underwent rigorous functional verification.
* Successfully heated food to target temperatures while maintaining the separate cooled compartment.
* Validated heating performance against temperature-vs-time success criteria. 
* The design met all key objectives relating to portability, thermal efficiency, and safety.

## Tools & Skills Demonstrated
* **Software:** SketchUp (CAD & Assembly Modeling), Arduino IDE, Microsoft Excel (Calculations).
* **Skills:** Embedded Systems, Control Engineering, Thermal Analysis, Rapid Prototyping, Requirement Engineering, Decision Matrix Evaluation.

## Gallery

### CAD Component Geometry
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 15px;">
  <img src="{{ '/assets/images/projects/lunchbox/cad-front.jpg' | relative_url }}" alt="Front View" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/lunchbox/cad-side.jpg' | relative_url }}" alt="Side View" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/lunchbox/cad-top.jpg' | relative_url }}" alt="Top View" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/lunchbox/cad-lid.jpg' | relative_url }}" alt="Lid Details" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/lunchbox/cad-dessert.jpg' | relative_url }}" alt="Dessert Compartment" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
</div>
*Caption: Orthographic profiles and individual component geometries of the lunch box casing.*

### System Integration & Prototyping

<div style="max-width: 400px; margin: 0 auto; text-align: center;">
  <img src="{{ '/assets/images/projects/lunchbox/exploded-view.jpg' | relative_url }}" alt="Exploded Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
  <p style="font-size: 0.9em; color: #666; margin-bottom: 2rem;"><em>Exploded view detailing component placement and modular architecture.</em></p>

  <img src="{{ '/assets/images/projects/lunchbox/circuit-diagram.jpg' | relative_url }}" alt="Circuit Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
  <p style="font-size: 0.9em; color: #666; margin-bottom: 2rem;"><em>Electronic architecture and embedded control logic for the thermal system.</em></p>

  <img src="{{ '/assets/images/projects/lunchbox/cover.jpg' | relative_url }}" alt="Physical Prototype" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
  <p style="font-size: 0.9em; color: #666; margin-bottom: 2rem;"><em>Assembled physical prototype undergoing initial thermal testing.</em></p>
</div>
