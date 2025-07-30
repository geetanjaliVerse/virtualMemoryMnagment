# virtualMemoryMnagment
Project Overview
VirtuMemSim is a Python-based interactive simulator designed to visually demonstrate the working of virtual memory management and page replacement algorithms in Operating Systems. The project aims to enhance the understanding of key memory management strategies by providing real-time visualizations and comparative analysis through a user-friendly graphical interface.

🎯 Key Features
🔁 Simulation of Page Replacement Algorithms
Supports FIFO (First-In-First-Out), LRU (Least Recently Used), and Optimal algorithms.

🎨 Real-Time Visualization
Memory frames and page tables update dynamically as the simulation runs.

📊 Algorithm Comparison Feature
Compares page faults of all algorithms for the same input and visually highlights the best-performing one using graphs.

🧠 Step-by-Step Simulation
Processes memory accesses one at a time, showing memory hits, faults, and updates.

🧼 Reset and Re-run Capability
Clears all previous data, allowing users to re-run simulations with new input.

🧩 Modular Design
Built using an MVC-inspired architecture with clear separation of GUI, logic, and analytics for better maintainability.

💻 Technologies Used
Language: Python

GUI: Tkinter

Graphing & Analytics: Matplotlib

Threading (optional): For future animation improvements

Export (optional): ReportLab for PDF output

Others: CSV for I/O operations

🧪 How It Works
User enters a sequence of memory accesses and frame count via the GUI.

Selects the desired algorithm or chooses Compare Algorithms.

Simulation begins and memory states, page hits, and faults are updated and displayed.

A summary graph is shown comparing all algorithms based on page faults.
