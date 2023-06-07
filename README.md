![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-%230A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)

# PYBROWSERMOB

This project is a fork of the original [AutomatedTester/browsermob-proxy-py](https://github.com/AutomatedTester/browsermob-proxy-py) library, which provides a Python client for the [lightbody/browsermob-proxy](https://github.com/lightbody/browsermob-proxy).

## Getting Started

### Installation

1\. Clone the repository to your local machine using Git:

```shell
$ git clone https://github.com/your-username/your-project.git
```

2\. Navigate to the project directory:

```shell
$ cd your-project
```

3\. Create a virtual environment to isolate project dependencies:

```shell
$ python3 -m venv venv
```

4\. Activate the virtual environment:

On macOS and Linux:

```shell
$ source venv/bin/activate
```

On Windows:

```shell
$ venv\Scripts\activate
```

### Setup

1\. Install the required dependencies using pip:

```shell
$ pip install -r requirements.txt
```

This will install all the necessary packages specified in the requirements.txt file.

## Setup Proxy

1\. Update the Emulator Proxy:

- Launch the emulator and navigate to "Settings -> Proxy".
- Uncheck the "Use Android Studio HTTP proxy settings" option if enabled.
- Check the "Manual proxy configuration" option.
- Update the "Hostname" field with "127.0.0.1" and set the "Port number" to "8888".
- Click on "Apply" to save the changes.

2\. Install the SSL Certificates:

- Load the EC and RSA certificates onto the emulator. This can typically be done by dragging and dropping the certificate files onto the emulator window.
- Open the settings app within the emulator.
- Navigate to the Security section.
- Look for the Encryption & Credentials option and select it.
- Choose Install a certificate from the available options.
- Select CA certificate to install a certificate authority (CA) certificate.
- Locate and select the EC certificate file to install it.
- Repeat the previous step for the RSA certificate file.

## Test

To run the tests for the forked browsermob-proxy-py project, follow the steps below:

1\. Install pytest if you haven't done so already. Open your terminal and execute the following command:

```shell
$ pip install pytest
```

2\. Start a browsermob instance by running the following command in your terminal:

```shell
$ java -jar browsermob.jar --port 9090
```

This will initiate the browsermob instance on port 9090.

3\. Open a new terminal window to run the tests. Navigate to the project directory.

```shell
$ py.test
```

This command will run the tests and display the results in the terminal window.

## Links

- [browsermob-proxy](https://github.com/lightbody/browsermob-proxy)
- [browsermob-proxy-py](https://github.com/AutomatedTester/browsermob-proxy-py)
- [browsermob-appium-sample](https://github.com/U-TOR/browsermob-appium-sample)
