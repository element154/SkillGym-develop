# VPN Configuration - Devin Docs

Source: https://docs.devin.ai/onboard-devin/vpn

- Support

- Devin

- Devin

- Introducing Devin

- Your First Session

- Tutorial Library

- When to Use Devin

- Instructing Devin Effectively

- Good vs. Bad Instructions

- Prompt Templates Cheat Sheet

- How does Devin fit into my existing SDLC?

- Environment configuration

- Index a Repository

- VPN Configuration

- Knowledge Onboarding

- AGENTS.md

- Devin Review

- Devin Session Tools

- Computer Use

- Testing & Video Recordings

- Slash Commands

- Ask Devin

- Data Analyst Agent

- DeepWiki

- MCP (Model Context Protocol) Marketplace

- DeepWiki MCP

- Devin MCP

- Advanced Capabilities

- Knowledge

- Skills

- Session Insights

- Secrets & Site Cookies

- Creating Playbooks

- Using Playbooks

- Scheduled Sessions

- Deployments

- Autofix Settings - Bot Comments

- Invite your Team

- Importing Code Settings

- Integrations Overview

- Slack

- Microsoft Teams

- GitHub

- GitLab

- Bitbucket

- Linear

- Jira

- GitHub Pull Request Templates

- Self-Hosted SCM & Artifacts

- Security at Cognition

- Billing

- Common Issues

- Prerequisites Checklist

- Setting up OpenVPN

- Alternative VPN Clients

- Publicly Available VPN Clients

- Private VPN Clients

# VPN Configuration

Configure VPN access for Devin to connect to your internal network

## ​ Prerequisites Checklist

- Public Access Verification Confirm these services are not accessible via the public internet. For cloud-hosted services (e.g., Gitlab Cloud Package Registry, JFrog Artifactory Cloud), an access token is typically sufficient.

- Confirm these services are not accessible via the public internet.

- For cloud-hosted services (e.g., Gitlab Cloud Package Registry, JFrog Artifactory Cloud), an access token is typically sufficient.

- Authentication Method: Using a service account to authenticate is recommended. Credentials can be securely stored via Devin’s Secrets functionality.

## ​ Setting up OpenVPN

- Upload your config.ovpn configuration file to Devin’s workspace by dragging and dropping it into the VSCode instance

```
config.ovpn
```

- Set up OpenVPN as a system service by creating the file /etc/systemd/system/openvpn.service :

```
/etc/systemd/system/openvpn.service
```

```
[Unit] Description=OpenVPN Client Service After=network.target [Service] ExecStart=/usr/sbin/openvpn --config /path/to/config.ovpn Restart=always [Install] WantedBy=multi-user.target
```

```
[Unit] Description=OpenVPN Client Service After=network.target [Service] ExecStart=/usr/sbin/openvpn --config /path/to/config.ovpn Restart=always [Install] WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload sudo systemctl enable openvpn sudo systemctl start openvpn
```

```
sudo systemctl daemon-reload sudo systemctl enable openvpn sudo systemctl start openvpn
```

## ​ Alternative VPN Clients

### ​ Publicly Available VPN Clients

- Install the client during setup using the appropriate package manager commands: sudo apt install forticlient

```
sudo apt install forticlient
```

```
sudo apt install forticlient
```

- Configure the startup command to establish connection

### ​ Private VPN Clients

- Upload the client binary and certificate to Devin’s workspace by dragging and dropping it into the VSCode instance

- Install using: sudo dpkg -i /path/to/GlobalProtect_deb.deb

```
sudo dpkg -i /path/to/GlobalProtect_deb.deb
```

```
sudo dpkg -i /path/to/GlobalProtect_deb.deb
```

- Configure the startup command: globalprotect import-certificate --location /path/to/cert

```
globalprotect import-certificate --location /path/to/cert
```

```
globalprotect import-certificate --location /path/to/cert
```
