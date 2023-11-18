:orphan:

.. _guide-setup:

Setup
===========

Installation of EvaDB involves setting a virtual environment using `miniconda <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_ and configuring git hooks.
To begin using:

1. Clone the repository:
   ```bash
   git clone https://github.com/georgia-tech-db/eva.git
2. Install the dependencies:
    sh script/install/before_install.sh
    export PATH="$HOME/miniconda/bin:$PATH"
    sh script/install/install.sh
3. Activate the virtual environment:
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate      # On Windows
4. Install python dependencies:
    pip install -r requirements.txt
