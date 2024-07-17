# antimal_bomb
Antimal Bomb creates a deceptive environment to trick malware into believing it is running in a virtual machine, sandbox, or analysis environment. By doing so, the malware may not execute its malicious payload, preventing further spreading and damage.

## Features

- **VM-like Registry Keys**: Creates registry keys typical of virtual machines.
- **Sandbox Artifacts**: Creates artifacts commonly found in sandbox environments.
- **User Interaction Simulation**: Simulates user activity.
- **Inactivity Simulation**: Simulates periods of inactivity.
- **Locale and Timezone Changes**: Changes system locale and timezone.
- **IP Spoofing**: Changes the IP address using VPN.
- **Hardware Identifier Spoofing**: Changes hardware identifiers such as MAC address.
- **Username Spoofing**: Modifies the system's registered owner name.
- **Process Simulation**: Runs common analysis tools.
- **CPU Temperature Simulation**: Sets a mock CPU temperature reading.
- **System Uptime Simulation**: Sets a mock system uptime value.
- **CPU Core Count Simulation**: Sets a mock CPU core count.
- **Recent Data Creation**: Creates recent files with modified metadata.

## Requirements

Administrative privileges to modify system settings and registry keys.
Python 3.x
Third-party tools (e.g., `macchanger`) for certain functionalities.

## Usage

Run the script:
    
          antimal_bomb.py
    
**Enter the required password** (default is "securepassword").

Usefulness in Emergencies on Workstations

In times of malware emergencies, this script can be quickly deployed to create a deceptive environment that tricks the malware into thinking it is being analyzed in a controlled environment. This can cause the malware to deactivate or delay its payload, giving IT teams crucial time to respond and mitigate the threat.

Future Research on Malware Control Techniques

This script serves as a foundation for future research into advanced malware evasion and deception techniques. Researchers can build upon this work to develop more sophisticated methods of deceiving malware, exploring how different types of malware react to various deception strategies.

Tabletop Exercises

For organizations looking to enhance their cybersecurity preparedness, this script can be used in tabletop exercises to simulate malware infections. By incorporating this script into training scenarios, IT teams can practice their response to a malware outbreak, improving their skills in deploying deception techniques and mitigating threats.



