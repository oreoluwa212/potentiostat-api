# Portable Potentiostat Project

## Introduction

Welcome to the Portable Potentiostat project! This repository contains the backend code designed to manage authentication, handle data exchange between the frontend interface and the Raspberry Pi hardware, and perform various functionalities for the potentiostat system. The primary goal of this project is to develop a compact and cost-effective potentiostat for electrochemical analysis, aiding researchers and engineers in their work.

## Features

- **User Authentication**: Secure user registration and login system.
- **Data Communication**: Seamless data transmission between the frontend application and Raspberry Pi hardware.
- **Electrochemical Testing**: Control and monitor electrochemical experiments remotely.
- **User Interface Integration**: Integration with a React-based frontend for user-friendly interaction.

## Technologies Used

- **Backend**: Python
- **Database**: PostgreSQL
- **Frontend**: React (Vite), TailwindCSS
- **Hardware**: Raspberry Pi 4, DAC (MCP4725), ADC (ADS1115), Resistors, Power Bank

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js
- Raspberry Pi 4 with Raspbian OS

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/oreoluwa212/potentiostat-api
    cd potentiostat-api
    ```

2. **Setup Backend**
    - Create a virtual environment and activate it:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
    - Install required packages:
      ```bash
      pip install -r requirements.txt
      ```
    - Configure PostgreSQL database settings in `config.py`.


3. **Setup Frontend**
    - Navigate to the frontend directory:
      ```bash
      git clone https://github.com/oreoluwa212/Potentiostat_Project
      ```
    - Install npm packages:
      ```bash
      npm install
      ```
    - Start the frontend server:
      ```bash
      npm run dev
      ```

4. **Setup Raspberry Pi**
    - Ensure the Raspberry Pi is set up with the necessary libraries and connected to the DAC and ADC.
    - Clone the repository on the Raspberry Pi and set up the environment similar to the backend setup.

## Usage

1. **User Authentication**
   - Register a new user account through the frontend interface.
   - Log in to access the dashboard and potentiostat controls.

2. **Running Experiments**
   - Specify the potentiostat parameters such as start voltage, stop voltage, and voltage step.
   - Send the parameters to the backend, which will relay them to the Raspberry Pi hardware.
   - Monitor the experiment progress and view the results through the frontend interface.


## Contributing

We welcome contributions to this project! Please fork the repository and submit a pull request with your improvements. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

We would like to thank our mentors, professors, and peers for their guidance and support throughout this project.

## Contact

For any questions or inquiries, please contact us at oreoluwaajayyiruth@gmail.com. 

Thank you for your interest in the Portable Potentiostat project!
