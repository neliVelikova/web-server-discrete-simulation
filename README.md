# Web Server Discrete-Event Simulation

A Python-based discrete-event simulation that models a multi-server request processing system. The project uses SimPy to simulate incoming requests, resource allocation, queue management, and server performance under varying workloads.

## Overview

The simulation represents a system where incoming requests are processed by a limited number of servers. Requests are generated randomly, wait for available resources, and are either processed or dropped if they exceed the maximum waiting time.

## Features

- Stochastic request generation using an exponential distribution
- Multi-server request processing with SimPy
- Queue and resource management
- Request timeout handling
- Performance monitoring and statistical analysis
- Visualization of queue length and server utilization over time

## Performance Metrics

The simulation tracks:

- **Processed Requests:** Number of successfully processed requests
- **Dropped Requests:** Number of requests that exceeded the maximum waiting time
- **Average Waiting Time:** Average time requests spend waiting for a server
- **Throughput:** Number of processed requests per simulation time unit
- **Maximum Queue Length:** Largest number of requests waiting simultaneously
- **Server Utilization:** Percentage of available server capacity being used

## Technologies

- Python
- SimPy
- Matplotlib
- Random module

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/web-server-discrete-simulation.git
cd web-server-discrete-simulation
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Simulation

Execute:

```bash
python web_server_simulation.py
```

The simulation prints performance statistics in the terminal and generates visualizations using Matplotlib.

## Visualizations

The simulation generates two plots:

1. Queue Length Over Time
2. Number of Busy Servers Over Time

## Purpose

This project explores discrete-event simulation concepts, stochastic processes, resource allocation, queuing systems, and performance evaluation in multi-server environments.
