README.md

# Preconfig Vector - Anki Vector Configuration Automation Script

This repository contains an automation script to configure an **Anki Vector** robot using the Python SDK. The script automatically detects the robot's IP on the network, responds to the interactive configuration script's prompts, and handles errors to ensure the configuration process completes successfully.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Script Details](#script-details)
- [Contribution](#contribution)
- [License](#license)

## Installation

### Prerequisites

- **Anki Vector SDK**: The SDK must be installed and configured on your machine.

### Installation Steps

1. **Download or clone the repository**:

    ```bash
    git clone https://github.com/yeikermate/preconfig-vector.git
    cd preconfig-vector
    ```

2. **Move the script to the Vector SDK root folder**:

   Copy the `configure_vector.py` script to the Vector SDK root directory:

   ```bash
   cp configure_vector.py /path/to/vector/sdk/

Make sure the script is located in the directory where you installed the Vector SDK.
Usage

The automation script performs the following steps:

    Automatically detects the IP address of the Vector robot using its MAC address.
    Runs the interactive configuration script (anki_vector.configure).
    Automatically responds to all prompts from the configuration script.
    Handles errors robustly, retrying the configuration if it fails.

Example Execution

To run the script from the Vector SDK root directory:

bash

python3 configure_vector.py

The script will continuously attempt to detect the robot's IP and complete the configuration until it is successful.
Script Details

    detect_vector_ip(target_mac): Function to detect the Vector robot's IP address by making an ARP request using its MAC address.
    Automation with pexpect: Uses pexpect to interact with the Vector configuration script non-interactively.
    Error Handling: The script handles common errors such as timeouts and connectivity issues, and automatically retries the configuration in case of failure.

Contribution

Contributions are welcome! If you want to contribute:

    Fork the project.
    Create a new branch (git checkout -b feature/new-feature).
    Commit your changes (git commit -m 'Add new feature').
    Push your branch (git push origin feature/new-feature).
    Open a pull request.

License

This project is licensed under the MIT License. You are free to modify and distribute the code, provided that the original author is credited.


### Key Changes Made

1. **Updated the Repository URL**: The repository URL has been changed to reflect your GitHub repository at `https://github.com/yeikermate/preconfig-vector`.
2. **Clarified the Installation Steps**: Ensured that the steps match your repository's purpose and location.
3. **Contribution and License Information**: Adjusted to encourage contributions and clarify usage rights.

Now, copy this content into your `README.md` file in your repository to provide a clear and accurate guide for u
