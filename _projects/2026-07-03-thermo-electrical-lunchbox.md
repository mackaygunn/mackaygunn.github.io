---
layout: project
title: "Thermo-Electrical Food Compartment"
date: 2026-07-03
categories: [product-design, embedded-systems]
tags: [Thermal-Engineering, SketchUp, Arduino, Systems-Design]
image: "/assets/images/projects/lunchbox/cover.jpg"
---

## Overview
**Project Type:** Product Design • Embedded Systems • Thermal Engineering
**Duration:** 2025
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

![Exploded CAD View](/assets/images/projects/lunchbox/exploded-view.jpg)
*Caption: Exploded view detailing component placement and modular architecture.*

![Physical Prototype](/assets/images/projects/lunchbox/prototype.jpg)
*Caption: Assembled physical prototype undergoing initial thermal testing.*

![Temperature Graph](/assets/images/projects/lunchbox/testing-graph.jpg)
*Caption: Temperature vs. Time analysis validating the heating efficiency.*
